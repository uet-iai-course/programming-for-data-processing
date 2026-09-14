# Hướng dẫn làm việc trong repo này

> **Dành cho mọi coding agent** (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Zed…) **và cả người.** Đây là nguồn chân lý về quy ước của repo — đọc hết trước khi sửa bất kỳ file nào. Repo này có vài luật mà vi phạm thì tốn kém và không rút lại được (xem mục Tuyệt đối không).
>
> **Chỉ tồn tại MỘT bản nội dung.** File thật là `CLAUDE.md`; `AGENTS.md` là **symlink** trỏ vào nó — vì Claude Code chỉ đọc `CLAUDE.md`, còn `AGENTS.md` là quy ước chung mà Codex, Cursor, Copilot, Zed, Windsurf… đọc. Nếu công cụ của bạn đọc tên khác (`GEMINI.md`, `.github/copilot-instructions.md`…), hãy tạo thêm symlink: `ln -s CLAUDE.md <tên-đó>`. **Tuyệt đối không nhân bản nội dung sang file thứ hai** (kể cả bằng tìm-thay-thế tên tool): hai bản sẽ trôi lệch, agent đọc bản cũ sẽ làm sai mà vẫn tin là đúng. Trên Windows, symlink cần Developer Mode/Admin + `git config core.symlinks true`; nếu không được thì để file mới chứa đúng một dòng `Xem CLAUDE.md`.

## Tuyệt đối không

- **Không push thẳng lên `main`** khi chưa qua quy trình publish bên dưới — `main` deploy công khai tức thì, sai là không rút lại được (đã bị cache).
- **Không `git add -A` / `git commit -a`** trong repo này: nhiều lần đã suýt/đã lôi nhầm file nội bộ và công việc dang dở của phiên khác. Luôn `git add` đích danh từng file mình sửa.
- **Không sửa nội dung giảng dạy trong `2526-1/`** (archive học kỳ đã dạy) — chỉ đọc để tham khảo.
- **Không commit dữ liệu sinh viên** (phân công nhóm, điểm, link repo SV) và **không commit `2627-1/private/`** (đáp án lab, giáo án trợ giảng).
- **Không đụng file đang có thay đổi chưa commit của phiên/agent khác** — kiểm `git status` trước; nếu có, hỏi giảng viên thay vì commit gộp.

## Bản đồ tài liệu — đọc gì trước khi làm gì

| Bạn định làm gì | Đọc file nào |
|---|---|
| Bất cứ việc gì | File này (hết) |
| Soạn/sửa slide | `SLIDE_STYLE_GUIDE.md` (thiết kế, rubric A–E) + `2627-1/EDIT-PASS-NOTES.md` (văn phong + quy ước bắt buộc: thuật ngữ, hình SVG, đo tràn) |
| Biết đã duyệt/public tới buổi mấy | `2627-1/PROGRESS.md` (mục "Trạng thái publish") |
| Hiểu vì sao một quyết định lại thế | `2627-1/DECISIONS.md` (nhật ký quyết định, có ngày) |
| Đụng tới điểm số / khung chương trình | Mục "Kế hoạch 2627-1" bên dưới; thay đổi CLO–rubric–trọng số phải qua Viện/Trường |

Nhịp làm việc hiện tại: **duyệt từng buổi một** — agent rà soát trước (văn phong, thuật ngữ, số liệu, hình, đo tràn), giảng viên duyệt bằng mắt, sửa tay nếu cần, rồi mới publish buổi đó lên `main`. Đừng làm nhảy cóc nhiều buổi cùng lúc.

## Tổng quan

Repo học liệu môn **Lập trình xử lý dữ liệu** (UET.DSE2049), Viện Trí tuệ nhân tạo, Trường ĐH Công nghệ, ĐHQGHN. Giảng viên phụ trách: TS. Nguyễn Tuấn Phong. Giao tiếp với giảng viên bằng **tiếng Việt**.

Nội dung là website tĩnh (không có bước build/test/lint cho học liệu): trang index + slide bài giảng Reveal.js + trang mô tả bài tập lớn. Deploy qua GitHub Pages từ nhánh `main` — **mọi thứ push lên `main` là public ngay lập tức**. Site public: **https://courses.iaidev.com/programming-for-data-processing/** — domain `courses.iaidev.com` gắn org-wide trên repo `uet-iai-course.github.io` (22/07/2026, DNS CNAME tại Cloudflare, chế độ DNS only); URL `uet-iai-course.github.io/...` cũ tự 301 về domain mới.

File `UET_Đề cương học phần_*.docx` ở root là đề cương chính thức (bản 06/2025) — nguồn chân lý về khung 15 buổi, CLO và trọng số đánh giá (20% quiz / 20% giữa kỳ / 60% bài tập lớn nhóm). Thay đổi CLO, khung rubric hoặc trọng số phải qua phê duyệt Viện/Trường; nội dung bài giảng, đề bài tập và cách tổ chức chấm thì giảng viên tự quyết được.

## Cấu trúc

- Mỗi học kỳ một thư mục: `2526-1/` = HK1 2025–2026 (đã dạy xong, coi như **archive — không sửa nội dung giảng dạy trong đó**, chỉ dùng làm nguồn copy). `2627-1/` = kỳ tới, đã dựng xong trên nhánh `2627-1-draft`, đang được giảng viên duyệt dần và public theo từng đợt (xem mục Quy trình publish).
- `index.html` (root) — trang tổng liệt kê các học kỳ; `index-pages.css` — CSS chung cho các trang index.
- Trong mỗi thư mục học kỳ: `index.html` (lịch giảng dạy, có cột link notebook Colab), `lecture-XX-ten-bai.html` (slide Reveal.js), `lecture-style.css` (CSS chung cho slide), `lecture-template.html` (template tạo bài mới), `projects/*.html` (đề bài tập lớn — tên dùng **gạch dưới**, không phải `project-*.html`; 2526-1: `project_1..4.html` + `projects/index.html`; 2627-1: chỉ `project_airbnb.html`, `projects/index.html` là redirect), `img/lecture-XX/` (hình minh hoạ), và bản Reveal.js 5.2.1 vendored (`revealjs/dist/`, `plugin/`).
- `README.md` (root) cố tình giữ **cực ngắn** (giới thiệu + link trang môn học + cách xem thử) để không phải bảo trì; mọi chi tiết vận hành nằm ở file này. Khi hai bên mâu thuẫn, tin vào cây thư mục thực tế rồi tới file này.

## Chạy preview

Website tĩnh, không có bước build/test/lint. **Luôn serve từ root repo** — bắt buộc, vì `2526-1/index.html` tham chiếu `../index-pages.css`; serve từ bên trong thư mục học kỳ sẽ làm trang index mất CSS (lỗi này hay bị chẩn đoán nhầm thành lỗi HTML rồi đi "sửa" trang đang đúng).

> ⚠️ **Bind 127.0.0.1, đừng bỏ.** Docroot là root repo nên preview phục vụ cả `2627-1/private/` (đáp án lab, giáo án) và `UET_*.docx` (có thông tin liên hệ cá nhân). Server mặc định lắng nghe mọi interface → cả mạng LAN tải được (đã kiểm chứng thật). Trên mạng trường/quán càng phải cẩn thận.

- **Mặc định** (không cần Node, không cần mạng): `python3 -m http.server 8766 --bind 127.0.0.1` → <http://localhost:8766/>
- Live-reload khi soạn slide (cần Node + tải được npm registry; sandbox không mạng thì bỏ qua, không phải lỗi cấu hình):
  `npx -y browser-sync start --server --listen 127.0.0.1 --port 8765 --files "2627-1/**/*" --files "index.html" --files "index-pages.css" --no-open --no-ui --no-notify`
  Kiểm cổng trống trước — `lsof -nP -iTCP:8765 -sTCP:LISTEN` — vì phiên khác có thể đang chiếm 8765; đang bận thì đổi `--port`, đừng giả định server ở 8765 là của mình.
- Hai lệnh trên chính là 2 cấu hình `slides` (browser-sync, Node) và `slides-static` (Python) trong `.claude/launch.json` — định dạng riêng của Claude Code, lại nằm trong `.claude/` đã gitignore nên bản clone **không có** file này; công cụ khác cứ chạy thẳng lệnh shell ở trên.
- `cd 2526-1 && npm install && npm start` (gulp serve, port 8000) — chỉ khi cần speaker notes lúc trình chiếu; docroot là thư mục học kỳ nên trang index sẽ thiếu CSS (bình thường).

### Xem từ MacBook qua Tailscale (live-reload, always-on)

Máy `dell-ts-01` chạy sẵn systemd `--user` service `preview-programming-for-data-processing`
(live-server, bind `100.83.155.60:5500`, tự chạy khi boot, tự restart) để xem trực tiếp trên
MacBook qua tailnet: mở <http://dell-ts-01.tail9c52ce.ts.net:5500/> (vd `.../2627-1/ai-policy.html`)
— **không cần bind cổng ở Mac, không cần SSH tunnel**. Sửa file bất kỳ dưới root repo → trình duyệt tự reload.

- Docroot là root repo nhưng launcher có **denylist** chặn `private/`, `*.docx`, `.git`, `.claude` → 403.
  Vì bind ra tailnet (không phải `127.0.0.1`) nên các máy admin *tải được* → denylist giữ đúng tinh thần
  luật '⚠️ Bind 127.0.0.1' ở trên. **Quan trọng khi cây làm việc đang ở nhánh draft** — lúc đó `private/`,
  `.docx` có mặt trong cây và sẽ bị chặn ở tầng HTTP.
- Quản lý: `systemctl --user {status,restart} preview-programming-for-data-processing`;
  log + "Change detected": `journalctl --user -u preview-programming-for-data-processing -f`.
- Hạ tầng đầy đủ (ACL Tailscale mở `tcp:3000-9999`, launcher `~/.config/iai-preview/…`, cách thêm app
  khác) ở `courses/CLAUDE.md` (thư mục mẹ) → mục "Dev preview qua Tailscale". Launcher + unit nằm **ngoài
  repo**, không commit.

## Chạy code Python

Dùng **`.venv/bin/python`** cho mọi script và notebook — đây là môi trường đã chốt số liệu (pandas 3.0.3). **Đừng dùng `python3` hệ thống** (pandas khác phiên bản → số lệch) và đừng dùng `.conda/bin/python3.11` (không có pandas). `.venv/` bị gitignore; máy mới tạo lại từ **`requirements.txt`** (ghim `pandas==3.0.3` + numpy/matplotlib/seaborn/plotly/duckdb/requests/pydantic/geopandas/google-genai): `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt` (hoặc `uv venv .venv && uv pip install -r requirements.txt`). Mở notebook ở local thì thêm `requirements-dev.txt` (jupyterlab, ipykernel) rồi đăng ký kernel `.venv/bin/python -m ipykernel install --user --name pfdp`.

**Dữ liệu để kiểm chứng số liệu** — dùng **đúng mốc chụp đã chốt**, không bao giờ lấy snapshot mới nhất:

- Santiago `2026-06-29` — `https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/…`, hai bản khác nhau: `visualisations/listings.csv` (18.534×19, giá đã là số) và `data/listings.csv.gz` (18.534×90, giá là chuỗi `$1,234.00`), cộng `visualisations/reviews.csv` (690.112 dòng).
- Rio `2026-06-24` — trước đây dùng cho "thành phố đối chứng" (đã bỏ 14/09/2026); vẫn là mốc chụp đối chiếu trong vài notebook.
- Dữ liệu **không nằm trong repo**; tải về `2627-1/notebooks/data/` (đã gitignore). Mọi `assert` trong `notebooks/lab-*.ipynb` gắn cứng vào mốc trên — dùng snapshot khác sẽ làm vỡ lab và khiến bạn "sửa" những con số đang đúng.

## Kiểm slide sau khi sửa (bắt buộc)

Mở deck ở khung **960×700** rồi đo tràn **từng slide lá** — slide lá là `section` không chứa `section` con (deck có `section` bọc ngoài cho vertical stack, đếm cả hai là sai). Slide tràn khi `scrollHeight > 700` hoặc `scrollWidth > 960`. Đoạn đo chuẩn (dán vào console trình duyệt, hoặc chạy qua công cụ điều khiển trình duyệt của bạn) nằm trong `2627-1/EDIT-PASS-NOTES.md` mục 6 — đo xong phải báo dạng `0/N slide tràn`.

## Quy ước soạn học liệu

- **Slide phải tuân thủ `SLIDE_STYLE_GUIDE.md` (root)** — tiêu chuẩn thiết kế/rà soát slide (ít chữ, mỗi slide một ý, rubric rà soát A–E), kèm ghi chú chuyển thể cho môn này ở đầu file (100 phút/buổi → 30–40 slide, quy ước thuật ngữ Anh–Việt, quy tắc slide code).
- Tạo bài giảng mới: copy `lecture-template.html` → `lecture-XX-ten-bai.html`, cập nhật tiêu đề/ngày/nội dung, thêm dòng vào bảng lịch trong `index.html` của học kỳ.
- Slide: số mục chỉ dùng ở slide mở phần (`1.`, `2.` trong `<h1>`), **`<h2>` không đánh số tiểu mục**; tiêu đề bài dạng `LTXLDL | <tên bài>`. Văn phong slide theo **`2627-1/EDIT-PASS-NOTES.md`** — chuẩn giảng viên chốt sau lượt duyệt buổi 1 (07/2026); deck buổi 1 là mẫu đối chiếu, không sửa lại.
- **Ký hiệu chế độ đánh giá** trong mọi học liệu: **🚫 đóng** (không AI) / **✅ mở** (AI được phép, kèm khai báo) — emoji luôn đi kèm chữ "đóng"/"mở" ngay cạnh (tránh ✅ bị đọc thành "đã xong"). QĐ GV 22/07/2026 thay cặp khoá 🔒/🔓 cũ: hai hình khoá quá giống nhau, bản in đen trắng (bài kiểm tra giấy) không phân biệt được. Không dùng lại cặp khoá.
- Dựng học kỳ mới: copy từ học kỳ gần nhất, cập nhật `index.html` root để thêm link (đổi nhãn "Hiện hành").

## Chính sách ngôn ngữ: Việt hoá toàn bộ (từ 2627-1)

Quyết định 07/2026: toàn bộ học liệu hướng tới sinh viên phải bằng **tiếng Việt**.

- Hiện trạng: trang index, projects, README đã là tiếng Việt; **11 deck của `2526-1` là tiếng Anh** — chỉ dùng làm nguồn nội dung tham khảo; 15 deck của `2627-1` đã viết mới bằng tiếng Việt.
- Quy ước dịch: dịch phần diễn giải/tiêu đề; **giữ nguyên** thuật ngữ kỹ thuật đã thông dụng và mọi tên API/code (`DataFrame`, `groupby`, `missing values`…), lần xuất hiện đầu có thể chú thích tiếng Việt trong ngoặc. Code, output, tên file giữ nguyên. Học liệu mới viết tiếng Việt ngay từ đầu.

## Kế hoạch 2627-1 (chốt 07/2026) — nâng cấp cho thời AI

Bối cảnh: môn thiết kế "tiền-AI"; mọi bài code về nhà và cả 4 đề BTL hiện tại đều AI-giải-được trọn vẹn. Định hướng chung: chuyển mục tiêu từ "viết code" sang "chỉ đạo và kiểm chứng"; đánh giá theo **hai chế độ** — đóng (quiz, giữa kỳ trên lớp có giám sát, vấn đáp) đo nền tảng cá nhân, mở (bài về nhà, BTL) cho phép dùng AI nhưng phải khai báo và chấm dựa trên phán đoán/kiểm chứng/mức hiểu.

**Các quyết định đã chốt (07/2026):**

- Chỉ **01 đề bài tập lớn** duy nhất: **Inside Airbnb** (thay cho 4 đề của 2526-1).
- Slides **viết mới bằng tiếng Việt** theo `SLIDE_STYLE_GUIDE.md`; deck 2526-1 chỉ là nguồn nội dung tham khảo, không dịch cơ học.
- **Mỗi buổi nội dung kèm 1 notebook Colab** tiếng Việt (demo bám slide + bài tập tại lớp).
- LLM API dạy cho sinh viên: **Gemini API free tier** (miễn phí, không cần thẻ, tích hợp Colab); code viết theo pattern dễ đổi provider.
- Học liệu 2627-1 soạn trên branch **`2627-1-draft`**; public bằng **quy trình publish chọn lọc** theo từng đợt duyệt (xem mục riêng bên dưới) — KHÔNG merge cả nhánh vào `main`.
- Bài tập về nhà hàng tuần và đề thi giữa kỳ: **làm sau**, không thuộc đợt dựng học liệu này.

> ⚠️ **Lịch 2627-1 đổi 10 tuần × 3 tiết** (phòng đào tạo, 08/2026 — xem DECISIONS.md 17/08): 15 bài nội dung giữ nguyên, dạy dồn 10 tuần theo cách A (gộp 4 cặp): T1=bài 1+2, T3=bài 4+5, T5=bài 7+8, T9=bài 12+13; đơn T2=b3, T4=b6, T7=b10, T8=b11, T10=b14. **Bài 9=giữa kỳ (T6, chỉ thi, bỏ deck ôn); Bài 15=buổi riêng sau T10.** Quiz 2 bài kiểm tra giấy T3/T9 (20% "bài tập trên lớp" = 10% thực hành nộp lab + 10% kiểm tra/chuyên cần; xem DECISIONS 18/08). Đối chứng BTL công bố sớm T2; mốc BTL: lập nhóm 23:59 CN **20/09/2026** (tuần 2), `git tag final` 23:59 CN **22/11/2026** (tuần 11); bỏ mốc proposal 14/09/2026. Suy ra **tuần 1 = 07–13/09/2026**, vấn đáp sau đó. Tổng 60 tiết (30/30) giữ nguyên. **Lịch chính tắc = `2627-1/index.html`** (cột Tuần↔Bài); nơi khác gỡ số tuần cứng. **Thuật ngữ học liệu SV: đơn vị bài giảng gọi "Bài N", không "Buổi N"**; từ 06/09/2026 **cả "bài trước / bài này / bài sau / bài lab / bài học"** thay cho "buổi trước/này/sau/lab/học" (hai bài có thể chung một buổi nên "buổi trước" sai nghĩa). "Buổi" chỉ dùng khi thật sự là phiên: buổi vấn đáp, buổi học đầu tiên (ai-policy).

**Khung 15 buổi** (chủ đề theo đề cương đã phê duyệt, nội dung hiện đại hoá):

| Buổi | Nội dung |
|---|---|
| 1 | Tổng quan môn học & công cụ (Python, Colab/VS Code, venv/pip) + **chính sách AI của môn**, làm việc với AI có trách nhiệm |
| 2 | Kiểu dữ liệu & lập trình Python cơ bản (nén — SV đã qua Tư duy tính toán) |
| 3 | NumPy — mảng & tính toán vector hoá |
| 4 | Giới thiệu pandas |
| 5 | Series & DataFrame chuyên sâu (indexing, apply, groupby) |
| 6 | Kết nối & truy xuất dữ liệu ngoài (CSV/JSON/Parquet, API, SQL; giới thiệu DuckDB) |
| 7 | Xử lý dữ liệu chuỗi (string, regex) |
| 8 | Xử lý dữ liệu thời gian |
| 9 | Thi giữa kỳ (chỉ cần deck ôn tập ngắn) |
| 10 | Làm sạch dữ liệu có cấu trúc (missing/outlier/trùng lặp, bộ quy tắc QA) |
| 11 | **Xử lý dữ liệu phi cấu trúc bằng LLM** (Gemini API, structured output, so với baseline regex, đánh giá trên mẫu gán nhãn tay, chi phí/batching/hallucination) |
| 12 | Trực quan hoá cơ bản (matplotlib, pandas plot) |
| 13 | Trực quan hoá nâng cao (seaborn, tương tác) + phản biện biểu đồ do AI sinh |
| 14 | Kể chuyện bằng dữ liệu + thẩm định một bản phân tích do AI tạo |
| 15 | Trình bày BTL (deck hướng dẫn vấn đáp + checklist nộp bài) |

Mỗi deck nội dung (trừ buổi 9, 15) kết bằng mục **"Làm việc với AI thì sao?"** (2–3 slide: AI làm tốt gì / hay sai gì ở chủ đề này / kiểm chứng thế nào).

**Đặc tả học liệu 2627-1** (đã dựng xong 05/07/2026 — giữ để đối chiếu khi rà soát, KHÔNG phải danh sách việc còn tồn; trạng thái thật xem `2627-1/PROGRESS.md`):

1. **Chính sách AI 1 trang** (song ngữ nếu cần): công cụ được phép, nghĩa vụ khai báo, đâu là gian lận — đưa vào Buổi 1 và mọi đề bài.
2. **Slides + notebook Colab cho từng buổi** theo khung 15 buổi ở trên, viết mới theo `SLIDE_STYLE_GUIDE.md`. Cập nhật trích dẫn: McKinney 3rd ed (2022, free tại wesmckinney.com/book), VanderPlas 2nd ed (2023). Giới thiệu DuckDB (khớp CLO4).
3. **Giờ thực hành (cập nhật 06/07/2026)**: mỗi tuần có **3 tiết thực hành riêng do trợ giảng dạy** (đề cương 30/30; lịch 10 tuần), tách khỏi 3 tiết lý thuyết. Nhịp: tuần 1–8 = lab kỹ năng dùng **trọn ~100'**; tuần 9 = chữa giữa kỳ; tuần 10–14 = lab ~60' + BTL clinic ~35–40'; tuần 15 = tổng duyệt vấn đáp ("máy sạch"). **Điểm 20% "bài tập trên lớp" (đề cương) chia đôi (QĐ bộ môn 18/08/2026): 10% thực hành (nộp bài lab qua GitHub Classroom, ✅ mở, thầy Đạt tổ chức, không bắt buộc tại lớp) + 10% kiểm tra trên lớp/chuyên cần = 2 bài kiểm tra giấy 15 phút TRONG GIỜ THỰC HÀNH tuần 3 và 9** (đổi 4→3 ngày 04/09; chuyển từ đầu giờ lý thuyết sang giờ thực hành 06/09/2026 — **học liệu công khai chỉ ghi "trên lớp"**, không ghi giờ nào) (🚫 đóng; tổng 20/20/60 không đổi nên không cần Viện duyệt — cách tổ chức chấm; lịch sử: 4 bài T3/5/7/9, trước nữa 5 bài lịch 15 tuần) (phạm vi đến hết tuần trước; đề kiểm tra do GV sinh từ IAI Assessment Hub, ngoài repo). Micro-exercise cũ **không còn lấy điểm** và đã bỏ khỏi timeline giờ thực hành; 13 file `micro-XX.md` trong private/ đổi vai trò thành **đề luyện tự học** (GV/TA phát qua Canvas tuỳ ý, không chấm). Học liệu: `notebooks/lab-XX.ipynb` **public** (tuần 1–8, 10–14; khác notebook demo bài giảng); đáp án lab + giáo án TA + đề luyện **KHÔNG public** — để trong `2627-1/private/` (đã gitignore), gửi trợ giảng qua Canvas. Bài về nhà dạng "AI là đề bài" (debug lời giải AI cài lỗi, kiểm chứng kết luận, so sánh 2 lời giải, viết test cho code AI) vẫn thuộc đợt sau.
4. **Bài tập lớn — 01 đề duy nhất: Inside Airbnb**: giữ khung thu thập → QA → KPI → trực quan hoá → báo cáo + repo GitHub private + vấn đáp; mỗi nhóm 1 thành phố (bỏ thành phố đối chứng 14/09/2026); hợp phần LLM bắt buộc trên bảng `reviews` (trích xuất khía cạnh/cảm xúc bằng Gemini API, so với baseline không-LLM, đo chất lượng trên ≥100 mẫu gán nhãn tay); bớt liệt kê từng bước trong mục "Công việc" để nhóm tự đề xuất QA/KPI rồi bảo vệ; bắt buộc `AI_USAGE.md` (công cụ, prompt then chốt, AI sai ở đâu, kiểm chứng thế nào).
5. **Chấm BTL**: pipeline phải chạy lại end-to-end bằng một lệnh và được chấm trên **snapshot giữ lại** (kỳ thu thập dữ liệu nhóm chưa xử lý); vấn đáp hỏi riêng từng thành viên + mở ngẫu nhiên code yêu cầu giải thích + live task nhỏ, điểm cá nhân được phép lệch nhau; dùng **một coding agent chạy local trên máy GV** (tool nào cũng được) quét từng repo trước buổi vấn đáp để kiểm deliverables và sinh 5 câu hỏi riêng theo code của nhóm. Ràng buộc: repo SV là private, không đẩy code/dữ liệu SV lên dịch vụ bên thứ ba, và **người quyết định điểm luôn là giảng viên**.

## Quy trình publish chọn lọc lên `main` (từ 22/07/2026)

`main` (public, GitHub Pages) chỉ chứa học liệu **giảng viên đã duyệt**; `2627-1-draft` là nguồn chân lý đầy đủ. Không bao giờ merge nhánh — mỗi đợt publish là "nhấc file đã duyệt":

1. Tạo worktree riêng cho `main` — `git worktree add ../ptdp-main main` (môi trường không ghi được ngoài repo thì `git worktree add .worktrees/main main`, nhớ thêm `.worktrees/` vào `.gitignore`). Không `git switch main` ngay trên cây làm việc chính (đang giữ công việc dở của `2627-1-draft`).
   ⚠️ **Worktree `main` KHÔNG chứa file hướng dẫn này** (nó cố tình không được publish) — nếu `cd` vào đó, công cụ của bạn mất sạch luật đúng lúc nguy hiểm nhất. Cách an toàn: đứng nguyên ở cây draft và thao tác bằng `git -C ../ptdp-main …`.
2. `git -C ../ptdp-main checkout 2627-1-draft -- <đích danh từng file đã duyệt>`. **Cấm `git add -A`**, cấm checkout cả thư mục lớn — đích danh từng file để không lôi nhầm file chưa duyệt.
   File đã duyệt bị **xoá/đổi tên** trên draft thì phải gỡ khỏi `main` bằng lệnh riêng: `git -C ../ptdp-main rm <đường-dẫn>` — bước "nhấc file" không tự gỡ, quên là file cũ vẫn còn public.
3. Sửa `2627-1/index.html` **bản trên `main`**: chỉ các buổi đã public mới có link (slide + notebook + lab); các buổi chưa public để **dạng văn bản thường, không bọc thẻ `<a>`**, kèm ghi chú "công bố dần"; link đề BTL chỉ bật khi đề đã public. Bản index trên draft luôn đầy đủ link — hai bản lệch nhau là chủ đích.
4. **Chốt chặn trước khi push** — chạy trên cây sắp push, không phải trên `origin/main`:

   ```bash
   # (a) commit sắp push có lôi nhầm tài liệu nội bộ không? — không ra gì là ĐÚNG (grep trả exit 1, đừng nối bằng &&)
   git -C ../ptdp-main ls-tree -r --name-only HEAD | grep -iE 'claude|agents|codex|cursor|gemini|starter|prompt|decisions|progress|edit-pass|questions|private|\.docx'
   # (b) đợt này thêm đúng những file nào?
   git -C ../ptdp-main diff --name-only --diff-filter=A origin/main..HEAD
   # (c) học liệu đang public tới buổi mấy? — đối chiếu bảng "Trạng thái publish" trong PROGRESS.md
   git -C ../ptdp-main ls-tree -r --name-only HEAD | grep -E '2627-1/(lecture-|notebooks/|projects/)' | sort
   ```

   `git ls-tree` **phải có `-r`** — thiếu nó chỉ liệt kê 7 mục ở cấp gốc và không bao giờ thấy file trong `2627-1/`. Và phải kiểm `HEAD` chứ **không phải `origin/main`**: `origin/main` là ref remote-tracking, chưa chứa commit bạn sắp push nên luôn "sạch" một cách giả tạo.
5. Push `main`, đợi Pages deploy rồi kiểm bằng `curl` vài URL vừa mở.
6. Quay lại nhánh `2627-1-draft`, thêm một dòng vào bảng **"Trạng thái publish"** của `2627-1/PROGRESS.md` (đợt, ngày, nội dung) và commit riêng — mọi phiên sau tra trạng thái ở đó, không cập nhật là hỏng nguồn tra cứu.

File **không bao giờ** publish lên `main` — chặn theo *loại*, không theo tên:

- **Mọi file hướng dẫn/khởi động agent ở root**: `CLAUDE.md`, `AGENTS.md` và mọi symlink trỏ vào nó, `STARTER-PROMPT-*.md`… — bất kể tên tool.
- **Tài liệu vận hành nội bộ**: `2627-1/{DECISIONS,PROGRESS,EDIT-PASS-NOTES}.md`, `2627-1/teaching-notes/` (gitignore), và mọi file `*-draft.html` (vd `2627-1/projects/project_airbnb_rubric-draft.html` — rubric BTL chưa chốt, 14/09/2026).
- **Học liệu không công khai**: `2627-1/private/` (đã gitignore).
- **Đề cương gốc**: `UET_*.docx` (có thông tin liên hệ cá nhân, đã gitignore).

## Lưu ý khác

- `.gitignore` hiện có: `node_modules/`, `package-lock.json`, `.DS_Store`, `.vscode/`, `.idea/`, `.conda/`, `.claude/`, `.venv/`, `2627-1/private/`, `/UET_*.docx`. **Thư mục cấu hình của agent phải được ignore trước khi commit** — mới chỉ có `.claude/`; nếu bạn dùng công cụ khác (`.codex/`, `.cursor/`, `.gemini/`, `.aider*`…), thêm dòng tương ứng ngay, đừng để log phiên/khoá API lọt lên repo public.
- Không commit dữ liệu sinh viên (bảng phân công nhóm, điểm, link repo SV) vào repo public này — các thứ đó để ở spreadsheet VNU như hiện tại.
- Báo cáo trung thực: đo được gì nói nấy, chưa kiểm thì nói rõ là chưa kiểm. **Mọi con số đưa vào học liệu phải kiểm chứng bằng dữ liệu thật** (tải snapshot Inside Airbnb rồi chạy lại), không ước lượng, không chép từ trí nhớ — đây là môn dạy sinh viên kiểm chứng số liệu.
