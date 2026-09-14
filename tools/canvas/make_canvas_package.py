#!/usr/bin/env python3
"""Sinh gói Canvas Common Cartridge (.imscc) từ bảng lịch giảng dạy trong `<kỳ>/index.html`.

Gói là *template chung* cho mọi lớp: không gắn ngày giờ, chỉ có
- Modules: 1 module / tuần (link slide, notebook Colab, notebook lab) + module "Bắt đầu" + module "Bài tập lớn";
- Trang wiki "Lịch giảng dạy" (bảng Tuần ↔ Bài, link tuyệt đối về site môn học);
- Syllabus (giới thiệu + cơ cấu điểm + link chính sách AI).

Import lên Canvas: Settings → Import Course Content → Content Type "Common Cartridge 1.x Package"
→ chọn file .imscc → "Select specific content" nếu muốn bỏ Course Settings. Re-import gói mới sẽ
*cập nhật* các module/page cũ (ID ổn định theo nội dung), không nhân đôi.

Chạy:  .venv/bin/python tools/canvas/make_canvas_package.py            # kỳ mặc định 2627-1
       .venv/bin/python tools/canvas/make_canvas_package.py --term 2627-1 --out tools/canvas/dist
Chỉ dùng thư viện chuẩn.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import zipfile
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from xml.sax.saxutils import escape

REPO = Path(__file__).resolve().parents[2]
SITE = "https://courses.iaidev.com/programming-for-data-processing/"
COURSE_TITLE = "Lập trình xử lý dữ liệu"
COURSE_CODE = "LTXLDL"

GRADING = [
    ("Thực hành — nộp bài lab", "10%", "Mở"),
    ("Kiểm tra trên lớp — 2 bài giấy 15 phút", "10%", "Đóng"),
    ("Thi giữa kỳ", "20%", "Đóng"),
    ("Bài tập lớn nhóm và vấn đáp", "60%", "Mở khi làm tại nhà; đóng khi vấn đáp"),
]

MILESTONES = [
    ("Mốc 1 — Lập nhóm, tạo repo, nhận thành phố chính + đối chứng (23:59 Chủ nhật 20/09/2026, tuần 2)", "Không cần tag"),
    ("Mốc 2 — Nộp bản cuối (23:59 Chủ nhật 22/11/2026, tuần 11)", "git tag final"),
    ("Mốc 3 — Vấn đáp ~20 phút/nhóm", "Theo lịch thi của Trường"),
]


# ----------------------------------------------------------------------------- parse index.html
@dataclass
class Link:
    text: str
    href: str


@dataclass
class Week:
    label: str                      # "1" … "10", "Sau tuần 10"
    lectures: list[Link] = field(default_factory=list)   # href rỗng = văn bản thường (vd "Thi giữa kỳ")
    notebooks: list[Link] = field(default_factory=list)  # text = "lecture-01" / "lab-01"


class ScheduleParser(HTMLParser):
    """Đọc <table class="sched">: cột 1 tuần, cột 2 bài giảng, cột 3 notebook."""

    def __init__(self) -> None:
        super().__init__()
        self.weeks: list[Week] = []
        self._in_table = False
        self._col = 0
        self._cur: Week | None = None
        self._a: Link | None = None
        self._buf: list[str] = []
        self._in_thead = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag == "table" and "sched" in cls.split():
            self._in_table = True
        if not self._in_table:
            return
        if tag == "thead":
            self._in_thead = True
        elif tag == "tr" and not self._in_thead:
            self._cur = Week(label="")
            self._col = 0
        elif tag == "td":
            self._col += 1
            self._buf = []
        elif tag == "a" and self._col in (2, 3):
            self._a = Link(text="", href=a.get("href", ""))
            self._buf = []
        elif tag == "strong" and self._col == 2:
            self._buf = []
        elif tag == "br" and self._col == 1:
            self._buf.append(" ")

    def handle_endtag(self, tag):
        if not self._in_table:
            return
        if tag == "thead":
            self._in_thead = False
        elif tag == "table":
            self._in_table = False
        elif tag == "tr" and self._cur is not None and not self._in_thead:
            if self._cur.label:
                self.weeks.append(self._cur)
            self._cur = None
        elif tag == "td" and self._col == 1 and self._cur is not None:
            self._cur.label = " ".join("".join(self._buf).split())
        elif tag == "a" and self._a is not None and self._cur is not None:
            # bỏ icon 📓/🧪 (span.tag-ic) ở đầu nhãn notebook
            self._a.text = re.sub(r"^[^\w(]+", "", " ".join("".join(self._buf).split()))
            (self._cur.lectures if self._col == 2 else self._cur.notebooks).append(self._a)
            self._a = None
            self._buf = []
        elif tag == "strong" and self._col == 2 and self._cur is not None:
            self._cur.lectures.append(Link(text=" ".join("".join(self._buf).split()), href=""))
            self._buf = []

    def handle_data(self, data):
        if self._in_table:
            self._buf.append(data)


def parse_schedule(index_html: Path) -> list[Week]:
    p = ScheduleParser()
    p.feed(index_html.read_text(encoding="utf-8"))
    if not p.weeks:
        raise SystemExit(f"Không tìm thấy bảng lịch (table.sched) trong {index_html}")
    return p.weeks


# ----------------------------------------------------------------------------- helpers
def ident(*parts: str) -> str:
    """ID ổn định theo nội dung → re-import cập nhật thay vì nhân đôi."""
    return "i" + hashlib.md5("|".join(parts).encode("utf-8")).hexdigest()


def abs_url(term_base: str, href: str) -> str:
    return href if href.startswith("http") else term_base + href


def E(s: str) -> str:
    return escape(s, {'"': "&quot;"})


XSI = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
CANVAS_NS = ('xmlns="http://canvas.instructure.com/xsd/cccv1p0" ' + XSI +
             ' xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 '
             'https://canvas.instructure.com/xsd/cccv1p0.xsd"')


# ----------------------------------------------------------------------------- build model
@dataclass
class Item:
    kind: str            # "url" | "header" | "page"
    title: str
    url: str = ""
    ref: str = ""        # resource id (url/page)
    indent: int = 0


@dataclass
class Module:
    id: str
    title: str
    items: list[Item]


def week_title(w: Week) -> str:
    nums = [m.group(1) for l in w.lectures for m in [re.match(r"Bài (\d+):", l.text)] if m]
    if nums:
        return f"Tuần {w.label} — Bài {' & '.join(nums)}"
    if w.label.isdigit():
        return f"Tuần {w.label} — " + " · ".join(l.text for l in w.lectures)
    return f"{w.label} — " + " · ".join(l.text for l in w.lectures)


def build_modules(weeks: list[Week], term: str, page_id: str) -> list[Module]:
    base = SITE + term + "/"
    mods: list[Module] = []

    start = Module(ident("mod", "start"), "Bắt đầu", [
        Item("page", "Lịch giảng dạy", ref=page_id),
        Item("url", "Trang môn học (slide, notebook, bài tập lớn)", url=base),
        Item("url", "Chính sách AI của môn", url=base + "ai-policy.html"),
        Item("url", "Đề bài tập lớn", url=base + "projects/project_airbnb.html"),
    ])
    mods.append(start)

    for w in weeks:
        items: list[Item] = []
        slides = [l for l in w.lectures if l.href]
        plain = [l for l in w.lectures if not l.href]
        for l in plain:
            items.append(Item("header", l.text))
        if slides:
            items.append(Item("header", "Bài giảng"))
            for l in slides:
                items.append(Item("url", l.text, url=abs_url(base, l.href), indent=1))
        lec_nb = [n for n in w.notebooks if n.text.startswith("lecture-")]
        lab_nb = [n for n in w.notebooks if n.text.startswith("lab-")]
        if lec_nb:
            items.append(Item("header", "Notebook bài giảng (Colab)"))
            for n in lec_nb:
                items.append(Item("url", f"Notebook {n.text}", url=abs_url(base, n.href), indent=1))
        if lab_nb:
            items.append(Item("header", "Giờ thực hành (Colab)"))
            for n in lab_nb:
                items.append(Item("url", f"Lab {n.text}", url=abs_url(base, n.href), indent=1))
        mods.append(Module(ident("mod", "week", w.label), week_title(w), items))

    btl = Module(ident("mod", "btl"), "Bài tập lớn", [
        Item("url", "Đề bài tập lớn", url=base + "projects/project_airbnb.html"),
        Item("header", "Các mốc — hạn 23:59 Chủ nhật, ngày cụ thể xem thông báo lớp"),
        *[Item("header", f"{t} · {tag}", indent=1) for t, tag in MILESTONES],
    ])
    mods.append(btl)
    return mods


# ----------------------------------------------------------------------------- render XML/HTML
def weblink_xml(title: str, url: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<webLink xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imswl_v1p1" ' + XSI +
        ' xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imswl_v1p1 '
        'http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imswl_v1p1.xsd">\n'
        f"  <title>{E(title)}</title>\n"
        f'  <url href="{E(url)}" target="_blank"/>\n'
        "</webLink>\n"
    )


def module_meta_xml(mods: list[Module]) -> str:
    out = ['<?xml version="1.0" encoding="UTF-8"?>', f"<modules {CANVAS_NS}>"]
    for pos, m in enumerate(mods, 1):
        out += [f'  <module identifier="{m.id}">', f"    <title>{E(m.title)}</title>",
                "    <workflow_state>active</workflow_state>", f"    <position>{pos}</position>",
                "    <require_sequential_progress>false</require_sequential_progress>", "    <items>"]
        for ipos, it in enumerate(m.items, 1):
            iid = ident("item", m.id, str(ipos), it.title)
            ctype = {"url": "ExternalUrl", "header": "ContextModuleSubHeader", "page": "WikiPage"}[it.kind]
            out += [f'      <item identifier="{iid}">', f"        <content_type>{ctype}</content_type>",
                    "        <workflow_state>active</workflow_state>", f"        <title>{E(it.title)}</title>",
                    f"        <position>{ipos}</position>", f"        <indent>{it.indent}</indent>"]
            if it.kind == "url":
                out += [f"        <identifierref>{it.ref}</identifierref>", f"        <url>{E(it.url)}</url>",
                        "        <new_tab>true</new_tab>"]
            elif it.kind == "page":
                out += [f"        <identifierref>{it.ref}</identifierref>"]
            out.append("      </item>")
        out += ["    </items>", "  </module>"]
    out.append("</modules>\n")
    return "\n".join(out)


def course_settings_xml(course_id: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<course identifier="{course_id}" {CANVAS_NS}>\n'
        f"  <title>{E(COURSE_TITLE)}</title>\n"
        f"  <course_code>{E(COURSE_CODE)}</course_code>\n"
        "  <default_view>modules</default_view>\n"
        "  <locale>vi</locale>\n"
        "  <time_zone>Asia/Ho_Chi_Minh</time_zone>\n"
        "</course>\n"
    )


def schedule_table_html(weeks: list[Week], term: str) -> str:
    base = SITE + term + "/"
    rows = []
    for w in weeks:
        lec = "<br>".join(
            f'<a href="{E(abs_url(base, l.href))}" target="_blank">{E(l.text)}</a>' if l.href else f"<strong>{E(l.text)}</strong>"
            for l in w.lectures)
        nb = " · ".join(f'<a href="{E(abs_url(base, n.href))}" target="_blank">{E(n.text)}</a>' for n in w.notebooks) or "—"
        rows.append(f"<tr><td>{E(w.label)}</td><td>{lec}</td><td>{nb}</td></tr>")
    return ("<table border=\"1\" style=\"border-collapse:collapse\"><thead><tr><th>Tuần</th><th>Bài giảng</th>"
            "<th>Notebook (Colab)</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table>")


def wiki_page_html(page_id: str, title: str, body: str) -> str:
    return (
        '<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n'
        f'<title>{E(title)}</title>\n<meta name="identifier" content="{page_id}"/>\n'
        '<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="active"/>\n'
        f"</head>\n<body>\n{body}\n</body>\n</html>\n"
    )


def syllabus_html(term: str, weeks: list[Week]) -> str:
    base = SITE + term + "/"
    grading = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in GRADING)
    return (
        "<html>\n<head>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Syllabus</title>\n</head>\n<body>\n"
        f"<h2>{E(COURSE_TITLE)}</h2>\n"
        f'<p>Học liệu (slide, notebook, bài tập lớn) đặt tại <a href="{E(base)}">{E(base)}</a>. '
        f'Được dùng công cụ AI theo <a href="{E(base + "ai-policy.html")}">chính sách AI của môn</a>.</p>\n'
        "<h3>Cơ cấu điểm</h3>\n"
        '<table border="1" style="border-collapse:collapse"><thead><tr><th>Đầu điểm</th><th>Trọng số</th><th>Chế độ AI</th></tr></thead>'
        f"<tbody>{grading}</tbody></table>\n"
        "<h3>Lịch giảng dạy</h3>\n"
        "<p>Mỗi tuần một module trong mục <em>Modules</em>. Ngày giờ cụ thể theo thời khoá biểu của từng lớp.</p>\n"
        + schedule_table_html(weeks, term) + "\n</body>\n</html>\n"
    )


def manifest_xml(course_id: str, mods: list[Module], page_res: str, page_href: str) -> str:
    ns = ('xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" '
          'xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" '
          'xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" ' + XSI +
          ' xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 '
          'http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd '
          'http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource '
          'http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd '
          'http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest '
          'http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd"')
    out = ['<?xml version="1.0" encoding="UTF-8"?>', f'<manifest identifier="{course_id}" {ns}>',
           "  <metadata>", "    <schema>IMS Common Cartridge</schema>", "    <schemaversion>1.1.0</schemaversion>",
           "    <lomimscc:lom><lomimscc:general><lomimscc:title>",
           f"      <lomimscc:string>{E(COURSE_TITLE)}</lomimscc:string>",
           "    </lomimscc:title></lomimscc:general></lomimscc:lom>", "  </metadata>",
           "  <organizations>", '    <organization identifier="org_1" structure="rooted-hierarchy">',
           '      <item identifier="LearningModules">']
    for m in mods:
        out += [f'        <item identifier="{m.id}">', f"          <title>{E(m.title)}</title>"]
        for ipos, it in enumerate(m.items, 1):
            iid = ident("org", m.id, str(ipos), it.title)
            ref = f' identifierref="{it.ref}"' if it.ref else ""
            out += [f'          <item identifier="{iid}"{ref}>', f"            <title>{E(it.title)}</title>", "          </item>"]
        out.append("        </item>")
    out += ["      </item>", "    </organization>", "  </organizations>", "  <resources>"]
    seen: set[str] = set()
    for m in mods:
        for it in m.items:
            if it.kind == "url" and it.ref not in seen:
                seen.add(it.ref)
                out += [f'    <resource identifier="{it.ref}" type="imswl_xmlv1p1">',
                        f'      <file href="{it.ref}.xml"/>', "    </resource>"]
    out += [f'    <resource identifier="{page_res}" type="webcontent" href="{page_href}">',
            f'      <file href="{page_href}"/>', "    </resource>",
            f'    <resource identifier="{ident("res", "settings")}" '
            'type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt">',
            '      <file href="course_settings/course_settings.xml"/>',
            '      <file href="course_settings/module_meta.xml"/>',
            '      <file href="course_settings/syllabus.html"/>',
            '      <file href="course_settings/canvas_export.txt"/>',
            "    </resource>", "  </resources>", "</manifest>\n"]
    return "\n".join(out)


# ----------------------------------------------------------------------------- main
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--term", default="2627-1", help="thư mục học kỳ (mặc định 2627-1)")
    ap.add_argument("--out", default=str(REPO / "tools/canvas/dist"), help="thư mục xuất .imscc")
    args = ap.parse_args()

    index = REPO / args.term / "index.html"
    weeks = parse_schedule(index)

    page_id = ident("page", "lich-giang-day")
    page_href = "wiki_content/lich-giang-day.html"
    mods = build_modules(weeks, args.term, page_id)
    for m in mods:                       # gán resource id cho từng link
        for it in m.items:
            if it.kind == "url":
                it.ref = ident("weblink", it.url)
    course_id = ident("course", args.term)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"ltxldl-{args.term}-canvas-template.imscc"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest_xml(course_id, mods, page_id, page_href))
        z.writestr("course_settings/canvas_export.txt", "what is the sound of one hand clapping?\n")
        z.writestr("course_settings/course_settings.xml", course_settings_xml(course_id))
        z.writestr("course_settings/module_meta.xml", module_meta_xml(mods))
        z.writestr("course_settings/syllabus.html", syllabus_html(args.term, weeks))
        z.writestr(page_href, wiki_page_html(page_id, "Lịch giảng dạy", schedule_table_html(weeks, args.term)))
        done: set[str] = set()
        for m in mods:
            for it in m.items:
                if it.kind == "url" and it.ref not in done:
                    done.add(it.ref)
                    z.writestr(f"{it.ref}.xml", weblink_xml(it.title, it.url))

    n_links = len(done)
    print(f"✔ {out}")
    print(f"  {len(weeks)} tuần → {len(mods)} module, {n_links} link, 1 trang wiki, syllabus")
    for m in mods:
        print(f"  - {m.title}  ({sum(1 for i in m.items if i.kind == 'url')} link)")


if __name__ == "__main__":
    main()
