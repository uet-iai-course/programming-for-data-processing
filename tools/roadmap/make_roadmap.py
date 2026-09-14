#!/usr/bin/env python3
"""Sinh hình "Lộ trình môn học" (SVG kiểu sơ đồ tàu điện: 10 ga = 10 tuần, tuyến BTL, thanh cơ cấu điểm)
và chèn vào `<kỳ>/index.html` giữa hai marker `<!-- roadmap:start -->` … `<!-- roadmap:end -->`.

Chạy lại sau khi đổi lịch / cơ cấu điểm:  .venv/bin/python tools/roadmap/make_roadmap.py [--term 2627-1] [--stdout]
Số tuần, bài, chặng, mốc BTL và điểm khai báo ở đầu file — phần dưới chỉ là toạ độ.
GV quyết 04/09/2026: vẽ cả tuần kiểm tra giấy (T3, T9) và vị trí tuần của mốc BTL — đảo quy ước "chỉ ghi 2 bài" trước đó.
"""
from __future__ import annotations
import argparse, re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# ---- dữ liệu (chỉnh ở đây) ------------------------------------------------------------------
WEEKS = [("T1", "Bài 1–2"), ("T2", "Bài 3"), ("T3", "Bài 4–5"), ("T4", "Bài 6"), ("T5", "Bài 7–8"),
         ("T6", "Giữa kỳ"), ("T7", "Bài 10"), ("T8", "Bài 11"), ("T9", "Bài 12–13"), ("T10", "Bài 14"),
         ("sau T10", "Vấn đáp")]
MID, ORAL = 5, 10                                   # chỉ số ga lớn
PHASES = [(0, 2, "#B45309", "🐼 Nền tảng"), (3, 4, "#D97706", "🔌 Lấy dữ liệu"),
          (6, 7, "#F59E0B", "🧹 Làm sạch · LLM"), (8, 9, "#7A5C30", "📊 Trực quan hoá")]
BTL = [(1, "👥", "lập nhóm 20/09"), (10, "🏁", "final 22/11")]   # (ga, icon, nhãn) — bỏ mốc proposal 14/09/2026
QUIZ = [2, 8]                                       # ga có kiểm tra giấy 15' (T3, T9; đổi 4→3 ngày 04/09/2026; làm trong giờ thực hành từ 06/09 — hình chỉ đánh dấu tuần)
LAB = (1, 10)                                       # lab chạy từ ga T2 tới ga cuối (tuần 11)
GRADES = [(10, "#D97706", "🧪", "Thực hành"), (10, "#2563EB", "✍️", "Kiểm tra"),
          (20, "#4D7C0F", "📝", "Thi giữa kỳ"), (60, "#9D174D", "🎯", "Bài tập lớn + vấn đáp")]
C_MID, C_BTL, C_LAB, C_QUIZ, TEXT, MUTED = "#4D7C0F", "#9D174D", "#D97706", "#2563EB", "#2C1A06", "#7A5C30"
# ------------------------------------------------------------------------------------------------

E = lambda s: s.replace("&", "&amp;")
FONT = 'font-family="system-ui,-apple-system,Segoe UI,Roboto,Noto Sans,Helvetica Neue,Arial,sans-serif"'
MONO = 'font-family="ui-monospace,Menlo,Consolas,monospace"'


def svg() -> str:
    x0, dx, ly = 70, 96, 100
    xs = [x0 + i * dx for i in range(len(WEEKS))]
    o = [f'<svg class="roadmap-svg" viewBox="0 0 1100 330" xmlns="http://www.w3.org/2000/svg" {FONT} role="img" '
         'aria-label="Lộ trình môn học: 10 tuần, thi giữa kỳ tuần 6, vấn đáp bài tập lớn sau tuần 10; '
         'điểm: thực hành 10%, kiểm tra 10%, giữa kỳ 20%, bài tập lớn 60%">',
         ]
    # ray nền + đoạn chặng
    o.append(f'<line x1="{xs[0]}" y1="{ly}" x2="{xs[-1]}" y2="{ly}" stroke="rgba(44,26,6,0.15)" stroke-width="10" stroke-linecap="round"/>')
    for a, b, col, name in PHASES:
        o.append(f'<line x1="{xs[a] - (20 if a else 0)}" y1="{ly}" x2="{xs[b] + 20}" y2="{ly}" stroke="{col}" stroke-width="10" stroke-linecap="round"/>')
        o.append(f'<text x="{(xs[a] + xs[b]) / 2:.0f}" y="{ly - 62}" text-anchor="middle" fill="{col}" font-size="13" font-weight="800">{E(name)}</text>')
    # ga
    for i, (wk, bai) in enumerate(WEEKS):
        x = xs[i]
        if i in (MID, ORAL):
            col, tint, ic, pct = (C_MID, "rgba(77,124,15,0.12)", "📝", "20%") if i == MID else (C_BTL, "rgba(157,23,77,0.12)", "🎤", "60%")
            o.append(f'<circle cx="{x}" cy="{ly}" r="22" fill="{tint}" stroke="{col}" stroke-width="3.5"/>')
            o.append(f'<text x="{x}" y="{ly + 8}" text-anchor="middle" font-size="22">{ic}</text>')
            o.append(f'<rect x="{x - 22}" y="{ly - 52}" width="44" height="20" rx="10" fill="{col}"/>')
            o.append(f'<text x="{x}" y="{ly - 38}" text-anchor="middle" fill="#fff" font-size="12" font-weight="800">{pct}</text>')
        else:
            o.append(f'<circle cx="{x}" cy="{ly}" r="9" fill="#fff" stroke="{TEXT}" stroke-width="3"/>')
        if i in QUIZ:
            o.append(f'<line x1="{x}" y1="{ly - 13}" x2="{x}" y2="{ly - 24}" stroke="{C_QUIZ}" stroke-width="2"/>')
            o.append(f'<circle cx="{x}" cy="{ly - 36}" r="12" fill="{C_QUIZ}"/>')
            o.append(f'<text x="{x}" y="{ly - 31}" text-anchor="middle" font-size="13">✍️</text>')
        o.append(f'<text x="{x}" y="{ly + 44}" text-anchor="middle" fill="{TEXT}" font-size="15" font-weight="800">{wk}</text>')
        o.append(f'<text x="{x}" y="{ly + 60}" text-anchor="middle" fill="{MUTED}" font-size="10.5">{E(bai)}</text>')
    # lab hằng tuần
    ldy = ly + 80
    o.append(f'<line x1="{xs[LAB[0]]}" y1="{ldy}" x2="{xs[LAB[1]]}" y2="{ldy}" stroke="{C_LAB}" stroke-width="2.5" stroke-dasharray="2 6" stroke-linecap="round"/>')
    o.append(f'<text x="{xs[LAB[0]] - 14}" y="{ldy + 4}" text-anchor="end" fill="{C_LAB}" font-size="11.5" font-weight="800">🧪 lab</text>')
    # tuyến BTL: rẽ sau ga BTL[0], chạy dưới, mũi tên vào ga cuối
    bty = ldy + 30
    bx = xs[BTL[0][0]] + 44
    o.append(f'<path d="M{bx - 16} {ly + 6} C{bx + 8} {ly + 30}, {bx - 8} {bty}, {bx + 24} {bty} L{xs[ORAL]} {bty} '
             f'C{xs[ORAL] + 58} {bty}, {xs[ORAL] + 58} {ly}, {xs[ORAL] + 44} {ly} L{xs[ORAL] + 40} {ly}" fill="none" stroke="{C_BTL}" '
             'stroke-width="4" stroke-linecap="butt" opacity="0.85"/>')
    o.append(f'<path d="M{xs[ORAL] + 25} {ly} L{xs[ORAL] + 42} {ly - 9} L{xs[ORAL] + 42} {ly + 9} Z" fill="{C_BTL}"/>')
    o.append(f'<text x="{bx - 16}" y="{bty + 4}" text-anchor="end" fill="{C_BTL}" font-size="11.5" font-weight="800">🎯 BTL</text>')
    for k, (g, ic, lb) in enumerate(BTL):
        mx = bx + 40 if k == 0 else xs[g]
        o.append(f'<circle cx="{mx}" cy="{bty}" r="12" fill="#fff" stroke="{C_BTL}" stroke-width="2"/>')
        o.append(f'<text x="{mx}" y="{bty + 5}" text-anchor="middle" font-size="13">{ic}</text>')
        o.append(f'<text x="{mx}" y="{bty + 28}" text-anchor="middle" fill="{C_BTL}" font-size="10.5" {MONO}>{lb}</text>')
    # thanh cơ cấu điểm
    y, h, x, w = 272, 36, 50, 1000
    for i, (p, col, ic, lb) in enumerate(GRADES):
        sw = w * p / 100 - (2 if i < len(GRADES) - 1 else 0)
        o.append(f'<rect x="{x:.0f}" y="{y}" width="{sw:.0f}" height="{h}" rx="8" fill="{col}"><title>{E(lb)}: {p}%</title></rect>')
        o.append(f'<text x="{x + sw / 2:.0f}" y="{y + h / 2 + 6}" text-anchor="middle" fill="#fff" font-weight="800" font-size="16">{ic} {p}%</text>')
        o.append(f'<text x="{x + sw / 2:.0f}" y="{y + h + 16}" text-anchor="middle" fill="{MUTED}" font-size="11.5">{E(lb)}</text>')
        x += sw + 2
    o.append("</svg>")
    return "\n".join(o)


def standalone_svg() -> str:
    """SVG tự đứng: nền trắng, viền bo, tiêu đề + hint ở trên, hình bên dưới (viewBox 1100×390)."""
    body = svg().replace('<svg class="roadmap-svg" viewBox="0 0 1100 330" xmlns="http://www.w3.org/2000/svg" ', "<g ", 1)
    body = body.replace("</svg>", "</g>")
    body = re.sub(r'<g (font-family="[^"]*") role="img" aria-label="[^"]*">', r'<g transform="translate(0,60)" \1>', body, count=1)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 390" width="1100" height="390" {FONT}>\n'
            '<rect x="0.5" y="0.5" width="1099" height="389" rx="24" fill="#FFFFFF" stroke="rgba(44,26,6,0.12)"/>\n'
            f'<text x="36" y="42" fill="#B45309" font-size="17" font-weight="800" letter-spacing="1">🚇 LỘ TRÌNH MÔN HỌC · LẬP TRÌNH XỬ LÝ DỮ LIỆU</text>\n'
            f'<text x="1064" y="42" text-anchor="end" fill="{MUTED}" font-size="12.5">10 tuần · mỗi tuần 3 tiết lý thuyết + 3 tiết thực hành</text>\n'
            + body + "\n</svg>\n")


def block() -> str:
    return ("<!-- roadmap:start — sinh bởi tools/roadmap/make_roadmap.py, đừng sửa tay -->\n"
            '      <h2 class="section-title"><span class="ic" aria-hidden="true">🚇</span>Lộ trình môn học</h2>\n'
            '      <div class="panel roadmap">\n'
            '        <p class="roadmap-hint">10 tuần · mỗi tuần 3 tiết lý thuyết + 3 tiết thực hành</p>\n'
            '        <div class="roadmap-wrap">\n' + svg() + "\n        </div>\n      </div>\n"
            "<!-- roadmap:end -->")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--term", default="2627-1")
    ap.add_argument("--stdout", action="store_true", help="in khối HTML ra stdout thay vì chèn vào index")
    ap.add_argument("--svg-out", metavar="FILE", help="ghi SVG độc lập (nền trắng, kèm tiêu đề) để upload Canvas / chèn slide")
    a = ap.parse_args()
    if a.stdout:
        print(block()); return
    if a.svg_out:
        out = Path(a.svg_out); out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(standalone_svg(), encoding="utf-8"); print(f"✔ {out}"); return
    idx = REPO / a.term / "index.html"
    s = idx.read_text(encoding="utf-8")
    pat = re.compile(r"<!-- roadmap:start.*?<!-- roadmap:end -->", re.S)
    if not pat.search(s):
        raise SystemExit(f"{idx}: không thấy marker roadmap:start/end — chèn tay hai marker vào chỗ muốn đặt hình rồi chạy lại")
    idx.write_text(pat.sub(lambda _: block(), s), encoding="utf-8")
    print(f"✔ đã chèn lộ trình vào {idx.relative_to(REPO)}")


if __name__ == "__main__":
    main()
