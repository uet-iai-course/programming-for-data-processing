# Tiến độ học liệu 2627-1

> **Bài 3 đã publish ngày 10/09/2026:** deck 61 slide, notebook bài giảng và lab mới 8 bài. Main `12b65ab`; Pages build thành công, URL công khai đã kiểm tra khớp nội dung.

> File này do agent duy trì. Đợt 1 (dựng 15 deck + 13 notebook demo + đề BTL) đã xong 05/07/2026 — chi tiết giữ nguyên bên dưới. Đợt 2 (edit-pass văn phong + học liệu giờ thực hành) bắt đầu 07/2026 — trạng thái ở mục ngay dưới đây.

## Bài 3 NumPy — đã duyệt và publish (10/09/2026)

- Deck 61 slide: cấu trúc mảng, vì sao tính nhanh, chỉ mục/lát cắt, broadcasting, thống kê/lấy mẫu. Mở đầu và kết thúc theo mẫu Bài 1–2; mục thống kê dùng giá giả lập liên hệ bài tập lớn.
- Kiểm tra 960×700: **0/61 slide tràn**, không ảnh hỏng hoặc tiêu đề lẻ dòng. Notebook bài giảng chạy **48 ô code** thành công.
- Lab mới **8 bài, 40 cell**, có dự đoán, TODO, kiểm tra và khai báo AI. Lời giải tham chiếu qua toàn bộ kiểm tra; notebook sinh viên không chứa đáp án.
- Publish chọn lọc 32 file: deck, hai notebook, SVG và script tái sinh/số đo. Main `12b65ab`, Pages built; deck, hai notebook và hình mới trả HTTP 200, khớp byte với bản được duyệt (kiểm bằng URL có tham số phiên bản).

## Trạng thái publish (main — public)

| Đợt | Ngày | Nội dung đã public |
|---|---|---|
| 1 | 22/07/2026 | Hạ tầng (`revealjs/`, `plugin/`, `lecture-style.css`, `package.json`/`gulpfile.js`) + index root & index học kỳ (buổi chưa duyệt không link) + `ai-policy.html` + **buổi 1–2 trọn bộ** (slide + notebook demo + lab) |
| 2 | 23/07/2026 | **Buổi 3 trọn bộ** (slide + notebook demo + lab + 3 hình SVG + script sinh hình); index mở link buổi 3 |
| 3 | 23/07/2026 | **Buổi 4 trọn bộ** (slide + notebook demo + lab); index mở link buổi 4. Kèm đợt này: `lecture-style.css` đổi màu điều hướng theo accent index |
| 4 | 01/08/2026 | **Buổi 5 trọn bộ** (slide + notebook demo + lab + 2 hình SVG + script sinh hình); cập nhật bản biên tập buổi 1–4, index và chính sách AI; index mở link buổi 5 |
| 5 | 02/08/2026 | **Buổi 6 trọn bộ** (slide + notebook demo + lab); cập nhật `lecture-style.css` cho pipeline ba bước; index mở link buổi 6 |
| 6 | 02/08/2026 | **Buổi 7 trọn bộ** (slide + notebook demo + lab); index mở link buổi 7 |
| 7 | 06/08/2026 | **Buổi 8 trọn bộ** (slide + notebook demo + lab + 2 hình SVG); index mở link buổi 8. Buổi 8 có 4 vòng sửa do GV phát hiện: lỗi tham chiếu slide "Kiểm tra mốc cuối", thêm slide công thức mùa vụ + slide shift, chuẩn hoá "204 dòng" |
| 8 | 10/08/2026 | Không có học liệu mới. `README.md` root rút gọn (bỏ bảng năm học/cây thư mục phải bảo trì tay, lệnh preview bind `127.0.0.1`, link domain mới) + **gỡ `2526-1/README.md`** khỏi `main` (trùng nội dung; đã xoá trên draft từ trước mà vẫn public — lần đầu dùng bước `git rm` của quy trình) |
| 9 | 12/08/2026 | **Buổi 10 trọn bộ** (slide + notebook demo + lab + hình SVG + script sinh hình); index mở link buổi 10. Duyệt phát hiện: `read_csv` dùng `usecols` cho khớp shape (18534,13), thêm slide điều tra `bedrooms` (56% phòng riêng) + slide "IQR là gì?", làm rõ slide điền theo nhóm (in mapping + trung thực mean 1,49→1,44), hình PNG→SVG kèm caption ngoại lai 97 triệu; tiện tay vá lỗi thiếu `</tr>` dòng buổi 9 trong `index.html` bản main |
| 10 | 12/08/2026 | **Buổi 11 trọn bộ** (slide + notebook demo + lab; **không có hình**); index mở link buổi 11 — buổi cờ đầu về LLM. Xác minh nguồn Google chính thức: Gemini free tier *không cần thẻ* + Interactions API 2026 (`client.interactions.create`/`output_text`/`usage`/`response_format`) + model `gemini-3.1-flash-lite`/`3.5-flash` đều đúng. Duyệt (workflow 4 chiều + kiểm chứng đối kháng, kèm GV duyệt mắt) phát hiện & sửa: baseline deck 0.081/0.412→**0.020/0.164** (kiểm 690k review thật), chi phí 100k ~$12.5→**~$9.8** (khớp token thật notebook), **định nghĩa `call_llm`** ở In[2] (trước bị dùng ở In[3]/In[4] mà chưa định nghĩa), Bài 1 hết crash (đổi schema ở cell 16 + cell 27 chịu được review bị loại), để trống scaffold Bài 2/3 (+xoá output), ghi chú cache nhúng inline, lab cell 20 TODO khớp assert, `unknown→und`. Kèm GV Việt-hoá/mài chữ toàn notebook; `ta-guide-11.md` (private) sửa token/chi phí ~$0.0013 |
| 11 | 13/08/2026 | **Buổi 12 trọn bộ** (slide + notebook demo + lab + 6 hình SVG + scatter PNG + script sinh hình); index mở link buổi 12. Duyệt (workflow soạn/kiểm đối kháng + GV duyệt mắt) phát hiện & sửa: **lỗi "kỳ cụt"** ở biểu đồ đường/anatomy (`.iloc[:-1]` chỉ bỏ 07/2026 lạc, vẫn giữ 06/2026 chưa đủ → sụt giả ~27%) → cắt `< "2026-06-01"` + `.loc["2023":].iloc[:-2]`; 7 hình PNG→SVG (scatter **giữ PNG** vì 18k điểm, SVG ~2,7 MB ≈ 18× PNG — đo thật); chỉnh vị trí 4 chú thích "giải phẫu" + thêm chú thích `alpha`; **thêm 2 slide định dạng raster/vector** (PNG/SVG/PDF) số liệu đo thật; notebook thêm §5 demo xuất 3 định dạng + in dung lượng (khớp từng KB với slide); lab thêm assert nhân 100. Kèm GV Việt-hoá deck |
| 12 | 14/08/2026 | **Buổi 13 trọn bộ** (slide + notebook demo + lab + 11 hình SVG + plotly PNG + script sinh hình); index mở link buổi 13. Duyệt (workflow 4 chiều + kiểm chứng đối kháng + GV duyệt mắt) phát hiện & sửa: **Lo Barnechea 824→791** (df lọc giá>0), **Las Condes "~1 bậc"→"~2× trung vị"** (đo thật 2,04× = 0,31 bậc), Santiago "7.000+"→"gần 7.000" (6.884); gắn nhãn **"số liệu minh hoạ"** cho chuỗi giá giả lập ở hình A/C, **bỏ kết luận bịa "Santiago tăng nhanh hơn Rio"**; **thêm hình kết quả** cho hue/plotly/FacetGrid (3 lệnh trước chỉ có code); **3 hình lỗi đủ 3 hình sửa** (thêm sua-truc-kep, sua-pie); choropleth **giản lược SVG** (`simplify` 1,6 MB→~55 KB); Việt hoá tiêu đề 3 hình AI-lỗi; thuật ngữ review→đánh giá, listing→chỗ ở, trợ giảng→giảng viên thực hành; lab sửa `assert` cherry-pick vỡ (dtype-agnostic); notebook thêm Bài Sửa A. Kèm GV Việt-hoá/mài deck |
| 13 | 14/08/2026 | **Buổi 14 trọn bộ** (slide + notebook demo + lab; **không có hình**); index mở link buổi 14 — buổi nội dung cuối (kể chuyện + thẩm định "báo cáo AI"). Duyệt (workflow 4 chiều + kiểm chứng đối kháng + GV duyệt mắt): **mọi số của báo cáo AI KL1–KL5 khớp dữ liệu thật 100%** (mean 118.200/median 59.000/846 thiếu/177 ngoại lai +44%; −27% MoM & +7% YoY; right-censoring 14.264→17.301 +21%; metro −11% & ~17% trong loại; Lo Barnechea 426.230/n=824; host 15,5/12,7). Sửa: **thêm slide "Báo cáo AI — năm kết luận"** (giới thiệu đủ KL1–KL5 theo thứ tự, tô màu 3 sai/2 đúng) vì deck chỉ mổ KL2/3/4; **bỏ tham chiếu "KL4" sớm** ở slide tương quan (mềm hoá "loại phòng là một biến gây nhiễu cần kiểm tra"); cherry-pick **nối buổi 13** (16× theo năm vs 51× theo tháng đáy COVID); notebook thêm **2 cell chốt** (thước đo 51×, Simpson thật KHÔNG đảo chiều). Thuật ngữ review→đánh giá, listing→chỗ ở, outlier→ngoại lai, VND→đồng, trợ giảng→giảng viên thực hành, Thử thách🏆→Bài tập, (🚫 đóng); lab assert Simpson dùng `round()`. Kèm GV mài chữ deck ("gấp rưỡi"→"cao hơn ~65%" = 1,65× đo thật) |
| 14 | 14/08/2026 | Sửa buổi 10 đã public: slide ghi file gốc `listings.csv.gz` Santiago 29/06/2026 có **91 cột → 90 cột** (đếm lại bằng pandas trên file thật). Không có học liệu mới; notebook/lab buổi 10 không ghi số này. |
| 15 | 14/08/2026 | Sửa `2627-1/index.html` bản main: “đầu kỳ” → “đầu kì”. Chỉ nhấc đúng một dòng — không checkout cả file (bản draft còn link buổi 9, 15 và đề BTL chưa public). |
| 16 | 17/08/2026 | **Favicon IAI Courses** (SVG mũ tốt nghiệp trong 2 cung hở navy/green, trong suốt, tự đổi trắng ở dark mode) áp cho site công khai PDP: thêm `favicon.svg` + `<link rel="icon" type="image/svg+xml">` ở `<head>` 34 trang đã publish (root index + 2627-1 + 2526-1 + projects); chỉ thêm chrome, không đụng nội dung. Cùng đợt đồng bộ favicon **toàn nền tảng courses.iaidev.com** (org landing + 4 course khác: ai-system-engineering, computational-thinking, machine-learning, programming-methodology — các repo ngoài repo này). Chưa áp: `ltxldl/ltxldl.github.io` (org khác, site PDP cũ) và `CognitionLanguageAndThought` (chưa có bản clone local). |
| 17 | 18/08/2026 | **Publish lớn cuối — đưa toàn bộ học liệu 2627-1 đã duyệt lên main.** Nhấc đích danh **61 file** (delta draft↔main = 69, loại 8 file nội bộ): thêm **buổi 15** (deck vấn đáp BTL) + **đề BTL** `projects/project_airbnb.html` + redirect `projects/index.html`; cập nhật 14 deck (buổi 1–8, 10–14), 23 notebook (13 lab + 10 demo), `ai-policy.html`, `index.html` (2627-1 + root) bản đầy đủ link, `.gitignore`, và đồng bộ chrome favicon 18 trang archive 2526-1. **KHÔNG publish**: deck ôn buổi 9 `lecture-09-on-tap-giua-ky.html` (QĐ 10 tuần: buổi 9 chỉ thi, bỏ deck ôn — index không link) và `lecture-template.html`. Kiểm chứng trước push: link nội bộ **0 hỏng**, notebook-link Colab/GitHub **0 chết**, **0 rò** tham chiếu nội bộ, 2526-1 chỉ khác đúng dòng favicon (không đụng nội dung archive), lecture-15 **0/11 tràn** (960×700), chốt chặn a/b/c sạch, + **audit đọc-only 4 chiều** (đề BTL / lecture-15 / index / 24 notebook) **0 publish-blocker**. Verify live sau deploy. |

| 18 | 18/08/2026 | Chỉnh index sau publish: **hero full-width toàn bộ trang index** (bỏ `max-width: 62ch` ở `.hero-text p` trong `index-pages.css` — file dùng chung 5 trang: root/2627-1/ai-policy/BTL/2526-1); rút gọn mô tả hero 2627-1; bỏ "— đọc miễn phí trực tuyến" ở tác giả McKinney/VanderPlas. 2 file (`2627-1/index.html` + `index-pages.css`); verify live OK. Ghi nhận: `lecture-15` có **WIP chưa commit của phiên/agent khác** trong working tree — KHÔNG đụng, KHÔNG publish (đúng luật). |

| 19 | 18/08/2026 | Sửa 3 trang đã public: (1) **số quiz `~5 bài` → `4 bài`** ở `ai-policy.html` + `lecture-01` (số cũ lịch 15 tuần còn sót, mâu thuẫn QĐ 10 tuần T3/5/7/9; deck 1 vốn tự mâu thuẫn dòng 434 vs 473) + cập nhật `EDIT-PASS-NOTES.md` (nội bộ, chống tái phạm); (2) **mài chữ deck vấn đáp `lecture-15`** ("Live task"→"Live task (nếu có)", bỏ tiêu đề phụ "kim tự tháp, không nhật ký", "tự hào nhất"→"thú vị nhất", "câu hỏi thật"→"câu hỏi") — vốn là WIP chưa commit của phiên/agent khác trong working tree, GV chỉ đạo publish nên commit theo. Lift 3 file public (EDIT-PASS-NOTES nội bộ không lift), lecture-15 0/11 tràn, verify live OK. |

| 20 | 18/08/2026 | **Cơ cấu điểm mới (QĐ họp bộ môn 18/08)** — chia 20% "bài tập trên lớp" của đề cương thành **10% thực hành** (nộp bài lab qua GitHub Classroom, ✅ mở, thầy Đạt tổ chức) + **10% kiểm tra trên lớp/chuyên cần** (2 bài giấy 15', 🚫 đóng, tuần 4&9; giảm từ 4 bài). Tổng **20/20/60 không đổi** → không cần Viện duyệt (cách tổ chức chấm). Public: `lecture-01` (bảng Cơ cấu điểm 3→4 dòng + slide "Hai chế độ" thêm thực hành vào ✅ mở) + `ai-policy.html` (thêm thực hành vào ✅ mở + tóm tắt, quiz 4→2). lecture-01 **0/34 tràn**, verify live OK. Nội bộ (không lift): CLAUDE.md/DECISIONS.md/EDIT-PASS-NOTES.md. Convention §7 giữ: công khai chỉ "2 bài", mốc tuần 4/9 để nội bộ + Canvas. |

| 21 | 25/08/2026 | Publish `SLIDE_STYLE_GUIDE.md` (rubric thiết kế slide — sạch, không mốc thi/đáp án) lên main. Kèm **viết lại `ai-policy.html`** thành văn bản quy định (điều khoản đánh số 1–6, bỏ emoji trang trí, thêm bảng cơ cấu điểm 10/10/20/60, "bạn"→"sinh viên"); đưa lên **cả draft** cho khỏi lệch nguồn. Giữ nội bộ: CLAUDE/AGENTS/DECISIONS/PROGRESS/EDIT-PASS-NOTES + bỏ `lecture-09` (QĐ chỉ thi) + `lecture-template`. Verify live sau deploy. |
| 22 | 04/09/2026 | **Banner "Lộ trình môn học"** trên `2627-1/index.html` (section riêng dưới hero, trước "Lịch giảng dạy"): SVG sơ đồ tàu điện 10 ga = 10 tuần, chặng tô màu, ga lớn giữa kỳ 20% / vấn đáp 60%, tuyến BTL (lập nhóm T2 · proposal T6 · final T10), đường lab T2→T11, dấu ✍️ kiểm tra **T3/T9** (đổi 4→3 ngày 04/09), thanh điểm 10/10/20/60. Sinh bằng `tools/roadmap/make_roadmap.py` (chỉ trên draft). Chỉ nhấc `index.html`; `tools/` không lên main. |
| 23 | 04/09/2026 | Chỉnh bố cục banner: tiêu đề "🚇 Lộ trình môn học" ra ngoài box thành `section-title` (đồng bộ với Lịch giảng dạy / Tài liệu học tập); box chỉ còn hint + SVG. Chỉ nhấc `2627-1/index.html`. |
| 24 | 06/09/2026 | Kiểm tra giấy chuyển sang giờ thực hành, **công khai chỉ ghi "kiểm tra trên lớp"** (bỏ "đầu giờ lý thuyết"): `ai-policy.html` (mục Chế độ đóng) + `lecture-01` (slide "Kế hoạch mỗi tuần", kiểm tra thành bullet riêng, 0/34 tràn). Kèm: hai box chế độ trong ai-policy bỏ viền màu bên trái. |
| 25 | 06/09/2026 | `lecture-01` slide "Lộ trình 15 buổi" → **"Lộ trình 15 bài"** (cột Bài, caption "Mỗi bài"), theo chuẩn "Bài N"; 0/34 tràn. |
| 26 | 06/09/2026 | **"buổi trước/này/sau/lab/học" → "bài …"** trong 13 deck (02–08, 10–14), 27 notebook (lecture + lab), đề BTL — 39 file, ~134 chỗ (lịch 10 tuần gộp hai bài một buổi nên "buổi trước" sai nghĩa). Không nhấc `lecture-09`, `lecture-template` (chưa từng lên main). Đo tràn 14 deck: 0. |
| 27 | 10/09/2026 | **BTL: môi trường tái lập và lựa chọn thư viện.** Publish đúng 3 file: `projects/project_airbnb.html`, `lecture-01-tong-quan-va-chinh-sach-ai.html`, `lecture-15-trinh-bay-btl.html`. Yêu cầu `.python-version` ghi Python `3.x.y`, `requirements.txt`/lockfile ghim thư viện, README hướng dẫn dựng môi trường; BTL tự chọn phiên bản và có thể dùng thư viện ngoài pandas. Làm rõ cache/`--skip-llm`, sửa thứ tự LLM trước KPI phụ thuộc LLM. Bài 1 thêm slide `.python-version`; đồng bộ checklist Bài 15. Kiểm: Bài 1 **0/35**, Bài 15 **0/11** slide tràn (960×700); file và tài nguyên hiển thị trên main khớp bản đã kiểm; liên kết nội bộ của 3 trang + index không lỗi; chốt chặn a/b/c sạch. Main `98818e5`, Pages build thành công; 3/3 URL public HTTP 200 và nội dung khớp file đã publish. |
| 28 | 10/09/2026 | **Bài 3 NumPy, bản duyệt mới:** deck 61 slide, notebook bài giảng, lab 8 bài và hình/script đi kèm (32 file). Kiểm 0/61 slide tràn; 48 ô code bài giảng chạy đúng, lab kiểm bằng lời giải tham chiếu. Chốt chặn không có file nội bộ, chỉ thay học liệu Bài 3; main `12b65ab`, Pages built, 4 URL kiểm trả HTTP 200 và nội dung khớp. |

Chưa public (còn lại trên draft): deck ôn buổi 9 `lecture-09-on-tap-giua-ky.html` (QĐ chỉ thi), `lecture-template.html`, và tài liệu nội bộ (`CLAUDE.md`/`AGENTS.md`/`SLIDE_STYLE_GUIDE.md`/`DECISIONS.md`/`PROGRESS.md`/`EDIT-PASS-NOTES.md`, `private/`). Toàn bộ học liệu hướng tới sinh viên đã public. `2627-1-draft` là nguồn chân lý; publish = nhấc đích danh file đã duyệt (quy trình: CLAUDE.md).

## Đợt 2 — sửa văn phong + học liệu giờ thực hành — ✅ HOÀN THÀNH (06/07/2026)

| Deliverable | Trạng thái |
|---|---|
| **Bộ mẫu tuần 2** (lab-02.ipynb + ta-guide-02 + micro-02) | ✅ commit đầu tiên của đợt — chờ giảng viên duyệt mẫu |
| Việc A: `.pipeline` sửa gốc CSS + bỏ inline | ✅ font-size 0.7em ở rule gốc, bỏ 2 inline buổi 1 |
| Việc A: edit-pass văn phong deck 2–15 + đo tràn | ✅ 14 deck + template theo EDIT-PASS-NOTES; đo từng deck sau sửa và đo chốt cả 15 deck: **0/443 slide tràn 960×700**; sửa thêm 2 tràn có sẵn (buổi 9, 13) + đồng bộ "trình bày 5 phút" buổi 15 (chi tiết: DECISIONS.md) |
| Việc A: pass nhẹ markdown 13 notebook demo | ✅ 36 cell (BTL→bài tập lớn, nghi thức→thói quen, hôm nay→buổi này, bỏ 😉, nghĩa vụ→trách nhiệm, Tang vật→Hình lỗi khớp deck 13) |
| Việc B: **13 lab notebook** (tuần 1–8, 10–14) | ✅ public, cấu trúc mục tiêu → warm-up → hướng dẫn (TODO + assert số thật) → tự làm ✅ mở; tuần 10–14 kèm mục 🧭 BTL clinic; **mỗi lab chạy end-to-end bằng bản điền đáp án** (kiểm 2 lần: khi dựng + lượt chốt cuối) |
| Việc B: **15 giáo án TA + 13 đề luyện (2 biến thể A/B + đáp án + thang 10)** | ✅ trong `2627-1/private/` — KHÔNG lên git (đã kiểm: 0 file private được track). *06/07: đề micro đổi vai trò thành đề luyện tự học không chấm — điểm 20% chuyển sang 5 bài kiểm tra giấy đầu giờ lý thuyết (xem DECISIONS)* |
| Index học kỳ: link lab từng buổi | ✅ thẻ lab-XX.ipynb cạnh notebook demo + ghi chú (link Colab hoạt động sau khi file được publish lên `main`) |
| Rà soát cuối | ✅ 15 deck 0 tràn · 26 notebook JSON hợp lệ · 13 lab đủ cấu trúc bắt buộc · link nội bộ index không hỏng · `git status`/`git ls-files` sạch private/ |

**Phát hiện đã được giảng viên quyết (06/07):** hình "chỉ số mùa vụ đỉnh T1–T4" của deck buổi 8 là artefact cửa sổ dữ liệu lệch (kèm số kiểm chứng + đề xuất sửa); lab/TA guide đợt này đã viết trung lập để không lan truyền con số sai.

**Lấy thư mục private/ (KHÔNG có trên git):** học liệu trợ giảng nằm ở `2627-1/private/` trên máy làm việc này — xem `2627-1/private/README.md`:

```bash
scp -r <user>@<máy-này>:~/teaching/programming-for-data-processing/2627-1/private/ ./2627-1-private/
# hoặc: tar czf private-2627-1.tar.gz -C 2627-1 private/
```

Nội dung private/: `ta-guide-01..15.md` (mục tiêu, timeline 100', đáp án đầy đủ + số thật, lỗi SV hay gặp) và `micro-01..08,10..14.md` — **đề luyện tự học** (hai biến thể + đáp án + thang điểm 10; từ 06/07 KHÔNG lấy điểm, GV/TA phát qua Canvas Portal tuỳ ý). Gửi giáo án cho TA qua Canvas Portal **theo từng tuần** (xem private/README.md).

**Việc giảng viên cần làm cho cơ chế điểm mới:** sinh **5 đề kiểm tra giấy 15 phút** từ IAI Assessment Hub trước các tuần **3, 5, 7, 11, 13** (phạm vi mỗi đề: đến hết tuần liền trước; chế độ 🚫 đóng).

## 1. Hạ tầng & khung — ✅

- ✅ Skeleton `2627-1/` (revealjs 5.2.1 + plugin copy từ 2526-1; img/ notebooks/ projects/)
- ✅ `lecture-style.css` — pattern chuẩn hoá: badge 📖/🤖, hộp nhấn key/warn/good, two-col, figure+caption, compact-table, pipeline, jp-cell; hệ mật độ đã tinh chỉnh sau rà soát render (font gốc 36px)
- ✅ `lecture-template.html` mới theo SLIDE_STYLE_GUIDE.md (minh hoạ đủ pattern)
- ✅ `index.html` học kỳ (lịch 15 buổi + link Colab + BTL + chính sách AI) · `index.html` root đã thêm thẻ 2627-1 "Hiện hành"

## 2. Chính sách AI — ✅

- ✅ `ai-policy.html`: hai chế độ 🚫 đóng/✅, công cụ được phép, 3 nghĩa vụ, ranh giới gian lận, hậu quả

## 3. Bài tập lớn Inside Airbnb — ✅

- ✅ Khảo sát thật insideairbnb.com (05/07/2026): 12 thành phố đạt chuẩn ≥3 snapshot/12 tháng (Barcelona, Madrid, Lisbon, Porto, Montreal, Toronto, Vancouver, NYC, New Orleans, Buenos Aires, Santiago, Rio), ngày snapshot + dataRoot ghi trong đề; schema `reviews`/`listings`/`calendar` xác minh (phát hiện: schema drift 79→90 cột, `calendar` mất cột giá, `host_since` trống 100% ở bản 06/2026, giá chuỗi theo nội tệ)
- ✅ `projects/project_airbnb.html`: nhóm tự đề xuất QA/KPI và bảo vệ; hợp phần LLM bắt buộc (Gemini structured output + baseline + ≥100 nhãn tay + chi phí + `--skip-llm`); `AI_USAGE.md`; chấm held-out snapshot; vấn đáp cá nhân; rubric 4 tiêu chí × 4 mức (30/25/25/20); placeholder deadline/phân công
- ✅ `projects/index.html`
- ✅ Thành phố châu Á: đã quyết (06/07/2026): giữ 12 thành phố chính; Bangkok/Singapore/Taipei thêm làm đối chứng tuỳ chọn

## 4. Slide + notebook từng buổi — ✅ 15/15 deck, 13/13 notebook

| Buổi | Deck | Notebook | Ghi chú |
|---|---|---|---|
| 1. Tổng quan & chính sách AI | ✅ 34 slide | ✅ | quy trình 5 bước làm việc với AI |
| 2. Python cơ bản | ✅ 34 | ✅ | lăng kính dữ liệu; `clean_price` ra đời |
| 3. NumPy | ✅ 36 | ✅ | 3 hình sinh script (speed/broadcast/axis) |
| 4. Làm quen pandas | ✅ 35 | ✅ | dữ liệu Santiago thật xuyên suốt từ đây |
| 5. Series & DataFrame chuyên sâu | ✅ 32 | ✅ | 2 hình (split-apply-combine, merge-how) |
| 6. Kết nối & truy xuất dữ liệu | ✅ 31 | ✅ | Parquet đo thật, API Open-Meteo, DuckDB |
| 7. Chuỗi & regex | ✅ 28 | ✅ | amenities/explode; baseline cho buổi 11 |
| 8. Dữ liệu thời gian | ✅ 26 | ✅ | mùa vụ + COVID từ 690k review thật |
| 9. Ôn tập giữa kỳ | ✅ 16 | — | 21 câu tự kiểm + 2 câu mẫu |
| 10. Làm sạch dữ liệu | ✅ 33 | ✅ | bộ quy tắc QA + qa_report chuẩn BTL |
| 11. LLM & phi cấu trúc | ✅ 40 | ✅ | Interactions API 2026 xác minh từ SDK; chạy trọn không cần key nhờ cache |
| 12. Trực quan hoá cơ bản | ✅ 27 | ✅ | 7 hình sinh script từ dữ liệu thật |
| 13. Trực quan hoá nâng cao | ✅ 30 | ✅ | choropleth geojson thật + 3 "hình AI lỗi" |
| 14. Kể chuyện & thẩm định AI | ✅ 25 | ✅ | thẩm định 5 kết luận AI, số liệu thật 100% |
| 15. Vấn đáp BTL | ✅ 16 | — | checklist nộp + kịch bản vấn đáp |

Mỗi deck nội dung kết bằng mục "Làm với AI thì sao?" (đã kiểm tự động). Mọi hình đều có script tái sinh trong `img/lecture-XX/scripts/`.

## 5. Rà soát toàn cục — ✅

- ✅ **Render 960×700** (Playwright/Chromium, đo scrollHeight/Width từng slide của cả 15 deck): **0 slide tràn**, 0 ảnh hỏng, 0 lỗi JS. (Ban đầu 103 slide tràn — nguyên nhân hệ thống là font gốc 40px; đã chỉnh hệ mật độ trong CSS + sửa nội dung 6 slide.)
- ✅ **13/13 notebook** chạy sạch end-to-end lần chốt trong môi trường mới (pandas 3.0.3; buổi 11 chạy trọn không cần API key nhờ cache)
- ✅ **Link nội bộ**: toàn bộ href/src trong index/deck/projects đều tồn tại (link Colab dạng `blob/main/...` sẽ hoạt động sau khi file được publish lên `main`)
- ✅ **Cấu trúc bắt buộc từng deck** (kiểm tự động): footer, title slide GV, agenda "Hôm nay", "Tổng kết", mục AI + badge, zenburn, `lang="vi"` — đủ 100%
- ✅ Rubric A–E áp khi viết từng deck; mọi output code trong slide đối chiếu với kết quả chạy thật (nhiều số nháp đã bị thay bằng số thật trong quá trình kiểm)

## Giảng viên cần làm (cập nhật 06/07/2026 — sau khi đã điền các quyết định)

> Các placeholder đã được xử lý ngày 06/07/2026 theo quyết định của giảng viên (xem cuối DECISIONS.md): bỏ thông tin GV/TA, kênh lớp = Canvas, nhóm 4–5 SV, mốc deadline theo tuần học, vấn đáp ~20'/nhóm, giữa kỳ viết giấy. Placeholder duy nhất còn lại: thời lượng & cấu trúc điểm giữa kỳ (deck buổi 9).

1. **Công bố trên Canvas đầu kỳ**: spreadsheet phân công nhóm/thành phố, danh sách tài khoản GitHub của GV/TA (để nhóm mời vào repo), ngày cụ thể cho các mốc tuần 3/8/14/15 (khi có thời khoá biểu), lịch vấn đáp buổi 15.
2. **Điền thời lượng & cấu trúc điểm giữa kỳ** vào deck buổi 9 (`{{cập nhật trước ngày thi}}`) — trước ngày thi.
3. Soạn **bài tập về nhà hàng tuần + đề thi giữa kỳ** (đợt sau, theo kế hoạch). Riêng **học liệu giờ thực hành + edit-pass văn phong**: đã lên kế hoạch đợt 2 (07/07/2026) — xem `2627-1/EDIT-PASS-NOTES.md`
4. Duyệt nội dung theo từng buổi → publish chọn lọc lên `main` (quy trình trong CLAUDE.md; KHÔNG merge cả nhánh)
5. (Khuyến nghị) Trước học kỳ: xem lại quota free tier Gemini trong AI Studio và chạy notebook buổi 11 một lần với API key thật

- Bài 3, lượt sửa ví dụ 10/09/2026: bỏ ngữ cảnh thành phố/giá/phí, dùng phép cộng theo hàng và cột; đồng bộ biến, hình và notebook. Kiểm tra: 0/48 slide tràn, 35 ô code chạy thành công; chưa publish.

- Bổ sung SIMD và nhiều luồng vào Bài 3 (10/09/2026): 2 slide sau cơ chế vòng lặp NumPy; phân biệt SIMD với nhiều luồng, ví dụ x*2 và nhân ma trận qua BLAS; notebook có phần đọc tương ứng và nguồn. Kiểm tra cuối: 0/50 slide tràn, không có hình hỏng hoặc code bị cắt. Chưa publish.

- Lượt tiếp Bài 3 (10/09/2026): GV nhận xét mục 1–2 đã ổn hơn, yêu cầu rà mục 3 và thêm hàm xác suất/thống kê tiêu biểu. Đã sắp shape/indexing → reshape → strides → view/chuyển vị; làm rõ bài tập view. Thêm mục 5 gồm 5 slide nội dung (mean/median, var/std, phân vị, default_rng/integers, random/normal/choice) và slide mở mục, đồng bộ notebook. Kiểm tra: 0/57 slide tràn, hình tải đủ, 41 ô code chạy thành công. Chờ GV xem mục 3 và phần mới; chưa publish.

- Điều chỉnh tiếp phần thống kê theo góp ý GV: bỏ mạch liệt kê API; thay bằng đại diện dữ liệu, độ phân tán, mô phỏng hai xúc xắc và giới hạn của kết luận. 4 slide nội dung + mở mục; danh mục hàm chuyển phụ lục tự học notebook. Kiểm tra 0/56 slide tràn, 43 ô code chạy thành công. Chưa publish.

- Rà toàn bộ Bài 3 theo hướng tư duy và lập luận (10/09/2026): đưa nhu cầu tính toán trước cú pháp; nối cách lưu mảng với giới hạn dtype, quan hệ phần tử với broadcasting; sửa bài tập để yêu cầu dự đoán, giải thích và kiểm chứng. Giữ cấu trúc cột đầu/cuối theo Bài 1–2, đồng bộ notebook; một số output hiện sau lần bấm để dành chỗ dự đoán. Đã xem ảnh toàn bộ 56 slide: 0/56 slide tràn ở 960×700, không có hình hỏng hoặc code bị cắt; 16 cặp code/output khớp và 43 ô code notebook chạy thành công. Chờ GV duyệt, chưa publish.

- Theo yêu cầu GV, thêm một slide nhắc lại thông dịch/biên dịch trong mục 2, trước cơ chế chọn mã theo dtype; nối bytecode CPython và tham chiếu list với vòng lặp số học NumPy đã biên dịch. Đồng bộ phần đọc notebook, dẫn nguồn Python/NumPy trong notes. Đã xem slide mới và kiểm tra 0/57 slide tràn, không hình hỏng/code bị cắt. Chưa publish.

- Thay bảng chữ ở slide thông dịch/biên dịch bằng SVG hai luồng xử lý, mũi tên vòng lặp và cùng ba giá trị 10, 12, 11; chỉ giữ một câu caption. Chi tiết diễn giải giữ trong notes/notebook. Chưa publish.

- Bỏ slide “Một dòng code, mấy lượt tính?” khỏi cuối mục 2: chi tiết mảng trung gian chưa cần cho mạch giải thích tốc độ. Giữ nội dung notebook với nhãn đọc thêm tuỳ chọn.

- Sắp lại mục 3 theo góp ý GV: strides → bài tập địa chỉ → view/lát cắt → sửa qua view → bài tập view → chuyển vị → reshape. Ví dụ indexing giữ/mất chiều chuyển sang broadcasting và đổi thành lấy cột để cộng theo hàng, có hệ quả cụ thể (4,) lỗi so với (4,1) ghép đúng. Đồng bộ thứ tự notebook. Kiểm tra: 0/56 slide tràn, đã xem bố cục các slide đổi; 43 ô code notebook chạy thành công, 16 cặp code/output slide khớp. Chưa publish.

- Bổ sung 3 slide cuối mục 3 về chỉ mục nâng cao: lọc bằng mask (hình), ghép từng cặp chỉ mục so với np.ix_ (hình), bài tập phân biệt view và bản sao khi cùng chọn hai cột. Notebook thêm kiểm chứng và phần đọc thêm gán trực tiếp/stride âm. Đã xem 3 slide mới; 0/59 slide tràn, không tiêu đề lẻ dòng, 47 ô code notebook chạy thành công. Chưa publish.

- GV chỉnh mạch mục 3: giới thiệu chỉ mục/lát cắt trước view. Đổi tên mục thành “Chỉ mục và lát cắt”, thêm 2 slide hình về A[2,1] và A[:2,1:], rồi view → sửa qua view → strides và bài tập → các ứng dụng/chọn nâng cao. Đồng bộ notebook. Đã xem hai hình mới, 0/61 slide tràn, 48 ô code notebook chạy thành công. Chưa publish.

- Duyệt riêng toàn bộ 20 slide có hình theo yêu cầu GV: xem từng ảnh ở 960×700, kiểm nhãn/chữ/mũi tên và phần diễn giải. Bỏ 7 caption lặp, rút 4 caption; giữ định nghĩa cần thiết. Xem lại 11 slide thay đổi sau khi bố cục dịch chuyển. Kiểm cuối: 0/61 slide tràn, không hình hỏng/code cắt/tiêu đề lẻ dòng. Chưa publish.

- Chốt lại mạch mục 3: giữ indexing/slicing trước view; đặt “Từ chỉ mục đến ô nhớ” liền “View bỏ qua các ô bằng cách nào?”, đưa bài tập địa chỉ ra sau cặp giải thích này. Giữ vai trò riêng của hai hình, không thêm slide. Đồng bộ notebook; 0/61 slide tràn.

### Rà soát lab Bài 3 theo deck đã duyệt — 10/09/2026 (draft)

- Viết lại `notebooks/lab-03.ipynb`: 8 bài về cấu trúc/strides, lát cắt, view/bản sao, mask/chỉ mục, broadcasting, sửa phép tính theo hàng, đo thời gian, thống kê và lấy mẫu.
- Dùng mảng nhỏ tự tạo, giá giả lập có đơn vị; bỏ yêu cầu tải Santiago và các bài where/phân vị/bootstrap khỏi phần lõi. Đề có ô dự đoán, TODO, kiểm tra và khai báo AI; không có đáp án trong notebook sinh viên.
- Kiểm chứng lời giải tham chiếu cho 7 ô TODO và toàn bộ ô kiểm tra: đạt. Notebook 40 cell, schema hợp lệ, không lưu output. Chưa publish thay đổi lab lên main.
