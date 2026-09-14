# Quyết định nhỏ trong đợt dựng học liệu 2627-1

> Các quyết định agent tự đưa ra theo hướng hợp lý (giảng viên có thể đảo lại).

- **Highlight theme**: chuẩn hoá `zenburn.css` cho mọi deck (các deck mới nhất 2526-1 đều dùng zenburn; template cũ ghi monokai là sót).
- **Tên file deck**: `lecture-XX-<ten-khong-dau>.html`, ví dụ `lecture-11-llm-du-lieu-phi-cau-truc.html` (giữ convention gạch ngang của 2526-1, chuyển sang tiếng Việt không dấu).
- **Link notebook trong index**: trỏ thẳng Colab qua `colab.research.google.com/github/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/...` — chỉ hoạt động sau khi file được publish lên `main`; trong thời gian draft sẽ 404 (chấp nhận được).
- **Title slide**: ~~ghi tên giảng viên, trợ giảng để placeholder~~ — hủy theo quyết định giảng viên 06/07/2026 (xem mục cuối): bỏ toàn bộ thông tin cá nhân GV/TA khỏi học liệu.
- **Hệ màu hộp nhấn** (theo style guide): cam `#E8890C` = điểm chốt, đỏ `#E62727` = cảnh báo/lỗi, xanh lá `#2E8B57` = khuyến nghị/ví dụ tốt, xanh lam `#1E93AB` = cấu trúc/định nghĩa/câu hỏi. Badge 🤖 "Làm với AI" dùng tím `#7A4CB0` để tách khỏi 4 màu nội dung.
- **Copy `package.json` + `gulpfile.js`** từ 2526-1 sang để giữ workflow `npm start` (speaker notes + livereload) cho ai cần.
- **VanderPlas 2nd ed**: link bản đọc online miễn phí `jakevdp.github.io/PythonDataScienceHandbook` (trang chính thức của sách; nội dung online là bản mở của sách).
- **BTL — 12 thành phố** (khảo sát thật 05/07/2026, tiêu chí ≥3 snapshot/12 tháng): Barcelona, Madrid, Lisbon, Porto, Montreal, Toronto, Vancouver, New York City, New Orleans, Buenos Aires, Santiago, Rio de Janeiro. Dự phòng: SF, Portland, Dallas, Boston, Quebec City, Brisbane, Budapest… Mỗi thành phố chốt 4 snapshot bắt buộc cách nhau ~1 quý (thành phố monthly được dùng thêm bản khác).
- **BTL — không commit dữ liệu thô** vào repo nhóm (file quá lớn, và cơ chế held-out yêu cầu script tải tự động theo config) — khác đề cũ 2526-1 vốn cho commit raw.
- **BTL — trọng số rubric**: A pipeline 30% / B dữ liệu (QA+KPI+LLM) 25% / C trực quan hoá & insight 25% / D nhóm & minh bạch AI 20%; thưởng tối đa +10%.
- **BTL — held-out**: chấm bằng snapshot phát hành trong kỳ (~09–12/2026) hoặc bản monthly không nằm trong danh sách bắt buộc; ghi rõ trong đề để nhóm thiết kế pipeline chịu được schema drift.
- **BTL — mốc nộp trung gian**: thêm mốc "bản đề xuất tuần 8" (QA/KPI/LLM dự kiến, GV phản hồi không chấm điểm) — để cứu các nhóm chọn sai hướng sớm.
- **Dữ liệu thật phát hiện khi soạn bài 8**: cột `host_since` trong snapshot Santiago 06/2026 trống 100% (Inside Airbnb thay bằng `hosts_time_as_*`); học liệu dùng `first_review` cho demo Timedelta. Mùa vụ review Santiago: **⚠️ đính chính 06/07/2026 (đợt 2, giảng viên duyệt)** — kết luận ban đầu "đỉnh T1–T4 do review trễ + T2 ngắn" là artefact của cửa sổ lệch (chỉ số gộp cả nửa đầu 2026, nửa năm lớn nhất, chỉ góp mặt cho T1–T6); tính trên các năm trọn 2022–2025, mùa vụ thật **đỉnh T7–T8 & T10–T11, đáy T2** (đô thị ngược mùa điểm nghỉ dưỡng). Đã sửa `gen_figures.py` + `mua-vu.svg` + 2 slide + notebook buổi 8 — số liệu kiểm chứng đầy đủ nằm trong lịch sử git (file QUESTIONS.md cũ, đã bỏ sau khi cả hai câu hỏi được quyết).
- **Buổi 14 — phát hiện khi kiểm chứng số liệu**: bảng `reviews` của một snapshot bị right-censoring ở đuôi (T9/2025 "mọc thêm" 21% khi nhìn từ snapshot 06/2026) và lịch sử co giãn vì listing rời sàn mang theo review (T8/2025 giảm 18% giữa 2 snapshot). Kịch bản thẩm định KL3 đổi từ "sai mùa vụ" thành "không kiểm được từ 1 snapshot" — trung thực với dữ liệu và dạy thêm được loại phán quyết thứ ba.
- **Rà soát render (Playwright, khung 960×700)**: đo scrollHeight/Width từng slide của cả 15 deck — 103 slide tràn do font gốc 40px của theme trắng quá lớn với tiếng Việt. Chỉnh hệ thiết kế trong `lecture-style.css` (font gốc 36px, hộp nhấn/pipeline/bảng gọn hơn) thay vì sửa lẻ từng slide; 6 slide còn lại sửa nội dung (tách checklist buổi 15 thành 2 slide, gọt chữ). Kết quả cuối: **0 slide tràn**, không ảnh hỏng, không lỗi JS.

## Quyết định đợt 2 — học liệu giờ thực hành (07/2026)

- **Dữ liệu lab tuần 2**: dùng bảng `visualisations/listings.csv` của Santiago snapshot 29/06/2026 (18.534 dòng, 19 cột, giá là số trần CLP, không nén) — Python thuần đọc trực tiếp được, khác bản `data/listings.csv.gz` (giá dạng `"$1,200.00"`) mà notebook demo dùng; hai bản bổ trợ nhau, lab các tuần pandas sẽ quay lại bản `data/` như demo. Các con số trong assert gắn với snapshot cố định này.
- **Lab notebook ship dạng TODO chưa điền đáp án** (đáp án nằm trong `private/ta-guide-XX.md`); tiêu chí "chạy end-to-end trên Colab" được kiểm bằng **bản điền đáp án** (mọi cell chạy sạch, mọi assert qua). Cấu trúc ô: TODO + khối `# --- Ô kiểm tra ---` bằng assert ngay trong cùng cell.
- **Micro-exercise tuần 2 làm trên giấy** (không máy) — dạng viết hàm ngắn/đoán output phù hợp giấy, chống AI tuyệt đối; các tuần sau chọn giấy/Colab theo kỹ năng của tuần, ghi rõ trong từng đề.
- **`private/README.md`**: quy trình phát học liệu cho TA (gửi từng tuần qua Canvas Portal, không phát file đáp án cho sinh viên) + lệnh scp/tar cho giảng viên lấy thư mục.
- **Edit-pass — "nhịp tuần" (EDIT-PASS mục 6.2)**: đã grep toàn bộ deck 2–15 (`2 tiết`, `quiz`, `thực hành`, `Kế hoạch mỗi tuần`) — **không deck nào nhắc nhịp tuần lớp học** ngoài buổi 1 (giảng viên đã tự cập nhật 2 LT + 2 TH). Ghi chú trong starter "lecture-08 có chỗ nhắc nhịp tuần" không khớp hiện trạng; buổi 8 chỉ có "tuần" theo nghĩa tần suất resample (`"W"`). Không sửa gì thêm.
- **Edit-pass — sửa nhất quán nhỏ ngoài danh mục notes** (cùng tinh thần văn phong): "BTL" viết đầy đủ "bài tập lớn"; "PDSH"/"McKinney, 3rd ed." → tên sách đầy đủ; "Nghi thức 5 bước" (buổi 4) đổi thành "Thói quen 5 bước" và cập nhật các tham chiếu ở buổi 5, 9; sửa tham chiếu chéo sai "(hình ở slide 4.1)" ở buổi 8 và "checklist 4.3"/"ở 4.4"/"câu hỏi ở 1.2" (đánh số tiểu mục cũ đã bỏ); tổng kết buổi 6 liệt kê đúng 5 tham số read_csv đã dạy (bỏ `nrows` chưa dạy); "tuần sau thấy pandas" ở buổi 2 sửa thành "buổi 4" cho đúng lịch; buổi 14 sửa "#4, #5" → "KL1, KL5" khớp bảng phán quyết.
- **Buổi 15 — đồng bộ thời lượng trình bày**: deck còn ghi "Trình bày 10 phút / ~8 slide / chạy thử 10'" trong khi giảng viên đã chốt vấn đáp 20'/nhóm với trình bày ~5' (bảng timeline cùng deck + đề BTL đã sửa) → đổi thành "5 phút / ~4–5 slide" ở cả 3 chỗ.
- **`lecture-template.html`**: áp cùng bộ quy ước máy móc (Quan trọng, Làm việc với AI, Tổng quan, title slide…) để deck mới sinh ra đã đúng chuẩn — template không thuộc phạm vi 14 deck nhưng là nguồn copy.
- **Tràn khung có sẵn phát hiện trong đợt 2** (không do edit-pass): buổi 9 slide "Thông tin kỳ thi" 742px (sau lần giảng viên sửa nội dung 06/07) — gọt "trên lớp,"/"lập biên bản"; buổi 13 slide "Hình C" 701px (chớm tràn từ đợt 1) — gọt câu + ảnh 82%→78%.
- **Link lab trong index**: thêm thẻ `lab-XX.ipynb` ngay cạnh `lecture-XX.ipynb` trong cùng ô Notebook (cùng class `notebook-tag`) — không thêm cột mới để bảng không rộng ra; ghi chú dưới bảng phân biệt notebook lý thuyết vs lab; tuần 9/15 không có lab (giữ "—").
- **Một chỗ "Làm với AI" còn lại trong buổi 1** (dòng body "mỗi buổi học sẽ đều có mục "Làm với AI thì sao?"", slide Quy trình 5 bước): buổi 1 thuộc diện không-đụng nên agent không sửa; sau edit-pass, mục đó ở mọi deck đã tên "Làm việc với AI thì sao?" — giảng viên đổi nốt 1 từ này nếu muốn đồng bộ tuyệt đối.
- **Thiết kế lab đợt 2 — điểm chung**: mỗi lab dùng dữ liệu Santiago thật với bài tập KHÁC notebook demo (đối chiếu từng demo trước khi soạn); mọi con số trong assert lấy từ chạy thật trên snapshot 2026-06-29; các "phát hiện thật" đưa vào bài (204 review sau mốc danh nghĩa, LTM lệch 665 do định nghĩa mốc, corr thời tiết ~0.08, phân phối availability hai bướu, false positive "cerca de todo", ngày kỷ lục 16/03/2026); lab 11 cố ý offline (Pydantic + output mô phỏng ghi rõ là mô phỏng) để không phụ thuộc API key trong giờ học; tuần 10–14 lab có mục "🧭 BTL clinic" bám mốc đề; hình trong lab 12–13 được assert bằng thuộc tính (title/ylim/số patch/file).

## Quyết định của giảng viên (06/07/2026 — cơ chế điểm 20% "bài tập trên lớp")

- **Thay micro-exercise bằng 5 bài kiểm tra giấy 15 phút ĐẦU GIỜ LÝ THUYẾT các tuần 3, 5, 7, 11, 13** (chế độ 🚫 đóng, phạm vi đến hết tuần trước). Đề do giảng viên sinh từ hệ thống ngân hàng câu hỏi riêng (IAI Assessment Hub), **ngoài repo** — lý do giảng viên chọn phương án này.
- Micro-exercise **không còn lấy điểm** và bỏ hẳn khỏi timeline giờ thực hành — lab dùng trọn ~100 phút. 13 file `micro-XX.md` giữ trong `private/` nhưng đổi vai trò thành **đề luyện tự học** (GV/TA phát qua Canvas Portal tuỳ ý, không chấm).
- Đã cập nhật theo: deck buổi 1 (bảng Cơ cấu điểm + slide Kế hoạch mỗi tuần — 2 chỗ duy nhất được đụng), `ai-policy.html`, cell "Cách làm việc" của 13 lab notebook, ghi chú dưới bảng lịch `index.html`, CLAUDE.md mục Giờ thực hành, 15 giáo án TA + README + 13 đề luyện trong private/.
- *Quyết định nhỏ của agent khi giãn timeline giáo án TA* (giảng viên đảo lại được): tuần 1–8 — khối micro (80→96/97/98) nhập vào phần bài tự làm ✅ mở tại lớp (đến phút 95, TA đi vòng hỗ trợ), chốt 95–100; tuần 10–14 — BTL clinic kéo dài đến phút 90 + 5 phút chữa chung vấn đề nổi bật, chốt 95–100; các guide tuần 2/4/6/10/12 thêm lời nhắc cuối giờ "tuần sau có bài kiểm tra 15 phút đầu giờ lý thuyết".

## Quyết định của giảng viên (06/07/2026 — chốt sau đợt dựng)

- **Bỏ toàn bộ thông tin cá nhân GV/TA khỏi học liệu**: xoá dòng Giảng viên/Trợ giảng ở title slide 15 deck + template; đề BTL không ghi tài khoản GitHub cá nhân — danh sách tài khoản công bố trên Canvas.
- **Kênh lớp**: hệ thống Canvas của trường (thông báo, spreadsheet phân công, danh sách tài khoản GitHub GV/TA, ngày deadline cụ thể, lịch vấn đáp).
- **Cỡ nhóm BTL**: 4–5 sinh viên.
- **Thành phố châu Á**: giữ 12 thành phố chính Âu/Mỹ; thêm Bangkok/Singapore/Taipei làm **đối chứng tuỳ chọn** (2 snapshot → chỉ so sánh chéo trên snapshot mới nhất, không làm thành phố chính).
- **Deadline**: chưa có thời khoá biểu → mọi mốc ghi theo tuần học ("23:59 Chủ nhật tuần X — ngày cụ thể: xem Canvas").
- **Giữa kỳ**: viết trên giấy, có giám sát; thời lượng & cấu trúc điểm để placeholder, quyết trước ngày thi.
- **Vấn đáp BTL**: ~20 phút/nhóm — trình bày + demo pipeline ~5' · hỏi riêng từng thành viên ~10' (2–3'/người) · live task ~5'.
- **Trang đề BTL tái thiết kế (06/07/2026, theo yêu cầu GV)**: bỏ Bootstrap, dùng chung `index-pages.css` + khối style riêng cùng pattern với `ai-policy.html` (callout 6 màu, task-card, data-table cùng hệ với schedule-table); nội dung giữ nguyên; sửa nốt "trình bày ~10 phút" → "~5 phút" cho khớp phiên vấn đáp 20'.

## Quyết định của giảng viên (22/07/2026 — ký hiệu chế độ & publish chọn lọc)

- **Ký hiệu chế độ đánh giá: 🚫 đóng / ✅ mở** thay cặp khoá 🔒/🔓 — hai hình khoá quá giống nhau, bản in đen trắng (5 bài kiểm tra giấy) không phân biệt được. Thay toàn cục 37 file (slide, notebook demo, lab, ai-policy, index, đề BTL, private/); chỗ emoji đứng một mình được bổ sung chữ ("(🚫 đóng)", "✅ mở") để ✅ không bị đọc nhầm thành "đã xong". Quy ước từ nay: emoji chế độ luôn đi kèm chữ "đóng"/"mở".
- Nhân tiện sửa nốt `private/micro-01.md` còn 2 chỗ nhắc micro-exercise như hoạt động lấy điểm (đã bỏ từ 06/07) — thay bằng "bài kiểm tra giấy 15 phút đầu giờ lý thuyết".
- **Publish chọn lọc lên `main`**: giảng viên duyệt đến đâu public đến đó, không merge cả nhánh. Đợt 1 (22/07/2026): hạ tầng + index (root & học kỳ) + `ai-policy.html` + trọn bộ buổi 1–2 (slide, notebook demo, lab); index bản `main` chỉ link các buổi đã public. Quy trình chi tiết: CLAUDE.md mục "Quy trình publish chọn lọc".
- **Dịch nốt 2 thuật ngữ tiêu đề (QĐ GV 22/07, sau khi xem site public)**: bài 13 "phê bình biểu đồ" → **"phản biện biểu đồ"** (tự nhiên hơn, gắn "tư duy phản biện"); bài 14 "audit" → **"thẩm định"** (đồng bộ ~64 chỗ ở index, deck 13/14/15, notebook, lab; giữ chú thích "(audit)" ở lần xuất hiện đầu trong deck 14 và notebook 14 theo quy ước thuật ngữ). Rút gọn 1 tiêu đề slide deck 14 ("Bảng phán quyết — đầu ra thẩm định") để hết tràn sau khi chữ dài ra; đo lại deck 13/14/15: 0 tràn.
- **Buổi 5 — id Airbnb dài 18–19 chữ số (GV hỏi khi duyệt 27/07/2026)**: `978070332077815549` trong slide `set_index` là dữ liệu thật (dòng đầu snapshot Santiago 29/06/2026, Ñuñoa, 45.647 CLP). Kiểm chứng trên file thật: Airbnb đổi hệ id ~2022 — 15.178/18.534 listing (82%) có id 18–19 chữ số (review sớm nhất 2022-01-30), 3.356 (18%) còn id cũ 5–8 chữ số (review từ 2014). QĐ GV: **giữ id thật, thêm 1 câu chú thích** trên slide. *Ghi chú kỹ thuật để dành*: id 18 chữ số vượt độ chính xác float64 (`978070332077815549` → float → `...552`, lệch 3) — nếu cột id bị đọc thành float (chỉ cần có ô trống, hoặc mở bằng Excel) thì id sai âm thầm, merge theo id hỏng. Chưa đưa vào học liệu; ứng viên tốt cho buổi 6 (dtype khi đọc) hoặc buổi 10 (QA) nếu GV muốn.
- **Buổi 8 — sửa lỗi tham chiếu "Nhìn lại slide trước" (GV phát hiện 06/08/2026)**: slide "Kiểm tra mốc cuối trước khi tổng hợp" nêu 204/155/49 trong hộp *"Nhìn lại slide trước"*, nhưng không slide nào trước đó có các số này — chúng nằm ở **notebook demo** (cell 1 + 11). Lỗi có từ commit dựng gốc `2c9de77`, không phải do edit-pass. Đã sửa: thay hộp bằng **một jp-cell tự dẫn ra số** (`rv_raw.loc[rv_raw["date"] > "2026-06-29", "date"].value_counts()` → 155 + 49) rồi diễn giải bằng văn xuôi; đánh lại `jp-n` phần 2 (rolling 3→4, so kỳ trước 4→5, so cùng kỳ 5→6). Số liệu kiểm chứng lại trên file thật (690.112 dòng): đúng 204 = 155 (30/06) + 49 (01/07). **Bài học chung cho pass duyệt**: mọi hộp "Nhìn lại slide trước" phải trỏ tới số có thật ở slide liền trước — mỗi con số trên slide cần có dòng code dẫn ra nó ngay tại chỗ.

## 15/08/2026 — mở rộng bảng thành phố BTL

- **12 → 26 thành phố.** HEAD `data/listings.csv.gz` trên 41 ứng viên (cửa sổ ±10 ngày quanh ngày-trong-tháng của mốc 06/2026, bốn quý 09/2025–06/2026). 32 thành phố đủ 4 quý. Không đủ trong cửa sổ đó: San Francisco, Los Angeles, Boston, Seattle, Portland, Dallas, Mexico City, São Paulo, Bogotá.
- Danh sách chính: 12 thành phố cũ + Paris, London, Amsterdam, Berlin, Rome, Athens, Prague, Chicago, Cape Town, Melbourne, Bangkok, Singapore, Taipei, Tokyo. GeoJSON `visualisations/neighbourhoods.geojson` của mốc 06/2026: HEAD 200 cả 14 thành phố mới.
- **Châu Á đủ 4 mốc** (khác khảo sát 05/07/2026, khi Bangkok/Singapore/Taipei mới có 2). Đưa vào danh sách chính, bỏ “chỉ so mốc mới nhất / không làm thành phố chính”. Nguyện vọng đối chứng Bangkok/Singapore/Taipei/Tokyo đăng ký trên Canvas; giao sau tuần 8.
- Dự phòng đã đủ 4 quý: Austin, Hong Kong, Vienna, Budapest (còn Florence, Venice, Sydney, Brussels, Munich, Copenhagen… nếu cần).
- Cỡ `reviews.csv.gz` mốc 06/2026 (Content-Length): Paris ~322 MB, Rome ~343 MB, London ~277 MB; Tokyo/Rio/BA/NYC ~120–170 MB. Đã ghi vào cạm bẫy trên đề.

## Quyết định của giảng viên (15/08/2026 — gỡ mục lục BTL)

- Kỳ này một đề duy nhất → không giữ trang `2627-1/projects/index.html` dạng danh sách. Link trên trang môn học trỏ thẳng `project_airbnb.html`. File `projects/index.html` chỉ còn redirect (tránh 404 nếu ai mở `/projects/`).

## Quyết định của giảng viên (14/08/2026 — chốt khi rà đề BTL)

Rà soát `projects/project_airbnb.html` trước public. GV chốt bốn điểm còn mở:

- **Rubric giữ 30/25/25/20 và thang 85/70/55.** Đây là cách chấm chi tiết của học kỳ (GV được quyết *cách tổ chức chấm*). Bốn nhóm tiêu chí vẫn triển khai bốn tiêu chí đề cương; đề không còn viết "bám đề cương" như thể trọng số/thang mức trùng từng chữ. Không xin Viện đổi đề cương.
- **Nộp tuần 3 / tuần 8:** tuần 3 chỉ mời GitHub + điền link repo vào bảng tính (không tag). Tuần 8: `git tag proposal` + PDF trong `reports/` + ghi link/commit vào bảng tính. Tuần 14 giữ `git tag final`.
- **Đối chứng:** đúng **một** thành phố do GV phân. **Không công bố từ đầu** (coi như tập kiểm): tuần 3 chỉ giao thành phố chính; sau mốc đề xuất tuần 8 mới giao đối chứng. Châu Á (Bangkok/Singapore/Taipei/Tokyo) là nguyện vọng đăng ký trên Canvas, không thêm thành phố thứ ba.
- **Bỏ điểm thưởng +10%** khỏi đề. Phân tích nâng cao chỉ giúp lên ô Xuất sắc của đúng tiêu chí.

Cùng lượt (không cần hỏi thêm): tách URL `data/*.csv.gz` và `visualisations/neighbourhoods.geojson` (HEAD `/data/…geojson` = 403); cảnh báo hai bản `listings`; sửa câu "dữ liệu nhóm không trùng"; thêm cạm bẫy đã kiểm (`host_since` trống, `id` float64, `neighbourhood` ≠ cleansed, lạm phát ARS, dung lượng reviews Rio/BA/NYC); ghi CC BY 4.0; hộp Git ngắn (buổi 1 đã hứa); `.gitignore` trong cây repo; KPI khu vực dùng `neighbourhood_cleansed`.

## Quyết định của giảng viên (17/08/2026 — remap lịch 10 tuần + chuẩn hoá "Bài")

Phòng đào tạo đổi lịch 2627-1: **10 tuần × 3 tiết/tuần** (thay 15 tuần × 2 tiết). GV chốt: chỉ nén lịch, không cắt nội dung; thực hành nén song song (mỗi tuần ~3 LT + 3 TH), tổng 60 tiết (30/30) giữ nguyên; CLO + trọng số 20/20/60 không đổi.

- **Cách A — giữ 15 deck, gộp 4 cặp vào tuần dày** (không viết lại deck): T1=bài 1+2, T3=bài 4+5, T5=bài 7+8, T9=bài 12+13; tuần đơn T2=b3, T4=b6, T7=b10, T8=b11, T10=b14.
- **Bài 9 = giữa kỳ (T6), chỉ thi** — bỏ deck ôn, gỡ link `lecture-09` khỏi bảng lịch (file vẫn còn, không lên lịch).
- **Bài 15 = buổi riêng sau T10** (trình bày/vấn đáp BTL, theo lịch thi).
- **Quiz: 5 → 4 bài**, T3/5/7/9 (đầu giờ lý thuyết).
- **Đối chứng: công bố sớm ở T2** cùng thành phố chính (đảo quyết định 14/08 "giấu tới sau đề xuất" — lịch nén còn ~4 tuần nếu giấu; snapshot held-out vẫn lo tổng quát hoá). "Có thể trùng" giữ.
- **Mốc BTL:** lập nhóm + nhận thành phố (chính + đối chứng) T2; `git tag proposal` T6; `git tag final` T10; vấn đáp sau T10.
- **Chuẩn hoá "Bài" thay "Buổi"** cho đơn vị bài giảng trong học liệu SV: sweep `buổi N`→`bài N` (160 chỗ / 36 file); giữ "buổi học/này/trước" (nghĩa phiên) và "~N buổi" (số lần). Header lab = "Giờ thực hành · bài N" (đã gỡ số tuần cứng theo §7).
- **Lịch chính tắc = `2627-1/index.html`**: bảng dựng lại 1 hàng/tuần (cột Tuần↔Bài, notebook ghép cặp lecture+lab, bỏ đuôi .ipynb), thêm icon nhận diện (📅📚📖🔗🎯), khối "Tài liệu học tập" compact (bỏ chữ nghiêng).
- ⚠️ **Chưa publish** — sweep đụng nhiều file đã public trên main (toàn bộ deck + lab + notebook); phải rà + re-publish trọn bộ khi GV duyệt xong.
- **Bỏ cơ chế đăng ký nguyện vọng đối chứng châu Á** (17/08, khi rà đề): GV giao cả thành phố chính lẫn đối chứng, SV không chọn/đăng ký. Gỡ câu "Muốn đối chứng Bangkok/Singapore/Taipei/Tokyo: đăng ký trên Canvas" — không có bể đối chứng riêng, đối chứng lấy từ chính lưới 26 thành phố (4 thành phố châu Á vẫn là thành phố đầy đủ, có thể được giao làm chính hoặc đối chứng như mọi thành phố khác). Lý do đảo: "bối cảnh gần gũi" không thuyết phục (SV Việt ít đi mấy nơi đó) + cho chọn thì rườm rà.
- **Cơ cấu điểm — chia đôi phần "bài tập trên lớp" (QĐ họp bộ môn 18/08/2026):** 20% "quiz / bài tập trên lớp" của đề cương chia thành **10% thực hành** (nộp bài lab qua **GitHub Classroom**, chế độ **✅ mở** — được dùng AI có khai báo; thầy Đạt tổ chức, *không bắt buộc làm tại lớp*) + **10% kiểm tra trên lớp / chuyên cần** = **2 bài** kiểm tra giấy 15' đầu giờ lý thuyết **tuần 4 và 9** (**🚫 đóng**; giảm từ 4 bài). Tổng trọng số **20/20/60 KHÔNG đổi** so với đề cương → thuộc "cách tổ chức chấm" GV tự quyết, **không cần Viện/Trường duyệt**. Đã cập nhật (publish thẳng main): bảng Cơ cấu điểm (3→4 dòng) + slide "Hai chế độ" deck 1, `ai-policy.html` (thêm thực hành vào ✅ mở + tóm tắt, quiz 4→2), + nội bộ CLAUDE.md/EDIT-PASS-NOTES. Convention §7 vẫn giữ: công khai chỉ ghi "2 bài", mốc tuần 4/9 để nội bộ + Canvas.

## Quyết định của giảng viên (04/09/2026 — hình "Lộ trình môn học" + gói Canvas)

- **Banner "Lộ trình môn học"** đặt ngay trên bảng lịch trong `2627-1/index.html`: SVG kiểu sơ đồ tàu điện (10 ga = 10 tuần, ga lớn = giữa kỳ 20% / vấn đáp 60%, đoạn ray tô màu theo 4 chặng, tuyến BTL rẽ sau T2 với 3 mốc lập nhóm/proposal/final, đường chấm lab, thanh cơ cấu điểm 10/10/20/60). Chọn từ 3 phương án phác thảo (dải tuần / flowchart chặng / ba làn) → flowchart chặng → bản "tàu điện". Tiêu chí GV: trực quan, ít chữ. Tên "Lộ trình môn học" (bỏ "Cả môn trong một hình").
- Hình **sinh bằng `tools/roadmap/make_roadmap.py`** (dữ liệu tuần/chặng/mốc/điểm khai báo đầu file), chèn giữa marker `<!-- roadmap:start/end -->` — đổi lịch thì sửa script rồi chạy lại, không sửa tay SVG.
- **Công khai tuần kiểm tra giấy (T3, T9)** trên hình (dấu ✍️) và **vị trí tuần của mốc BTL** — GV chủ động yêu cầu ("chưa có kiểm tra buổi 4 và buổi 9 à?"). Đảo quy ước §7 EDIT-PASS-NOTES "công khai chỉ ghi 2 bài"; §7 cần cập nhật theo khi rà lại.
- **Lab chạy từ tuần 2 đến tuần 11** (lệch 1 tuần so với lý thuyết) — GV chốt khi duyệt hình; đường chấm lab vẽ T2 → ga cuối.
- **Gói Canvas template** (`tools/canvas/make_canvas_package.py`, commit 2a35d02): Common Cartridge không gắn ngày, module/tuần + trang lịch + syllabus, dùng chung cho mọi lớp; GV đã import thành công.
- **Kiểm tra giấy: tuần 4 → tuần 3** (GV chốt khi duyệt hình lộ trình, 04/09/2026). Hai bài giờ ở **T3 và T9**. Đã sửa: CLAUDE.md (mục Kế hoạch + Giờ thực hành), EDIT-PASS-NOTES §7, `tools/roadmap/make_roadmap.py` (QUIZ), `tools/canvas/README.md`. Dòng lịch sử 18/08 trong DECISIONS/PROGRESS giữ nguyên.

## Quyết định của giảng viên (06/09/2026 — kiểm tra giấy chuyển sang giờ thực hành)

- **2 bài kiểm tra giấy 15 phút làm trong GIỜ THỰC HÀNH** (tuần 3 và 9), không còn "đầu giờ lý thuyết". **Học liệu công khai chỉ ghi "kiểm tra trên lớp"**, không nói giờ nào (GV: "cứ ghi chung chung là thi trên lớp").
- Đã rà toàn cây draft (`đầu giờ`, `kiểm tra giấy`, `quiz`, `15 phút`): sửa `ai-policy.html` (mục Chế độ đóng), `lecture-01` (slide "Kế hoạch mỗi tuần": tách kiểm tra thành bullet riêng, bỏ khỏi bullet Lý thuyết), CLAUDE.md (Giờ thực hành), EDIT-PASS-NOTES §7 (thêm luật không ghi giờ), comment `tools/roadmap/make_roadmap.py`. Dấu ✍️ trên hình lộ trình giữ ở ga T3/T9 (chỉ đánh dấu tuần). Dòng lịch sử trong DECISIONS/PROGRESS giữ nguyên. `private/` không có trong cây local — giáo án TA tuần 3/9 nếu ghi "đầu giờ lý thuyết" thì sửa khi phát.
- **`ai-policy.html` mục 2: hai card "Chế độ đóng / Chế độ mở" bỏ viền màu bên trái** (GV: "nhìn claudish quá" — chỉ bỏ dải viền màu, giữ box + tiêu đề màu). Đã thử gộp vào điều 2.1/2.2 dạng văn bản nhưng GV muốn giữ box. Slide "Kế hoạch mỗi tuần" deck 1 đo lại: 0/34 tràn.

## Quyết định của giảng viên (06/09/2026 — "bài trước/này/sau" thay "buổi …")

- GV thấy slide "Buổi trước" ở deck 2 và yêu cầu đổi: **mọi tham chiếu tới đơn vị bài giảng dùng "bài"**, kể cả "bài trước / bài này / bài sau / bài lab / Mục tiêu bài học / Tóm tắt bài học / Bài giảng tiếp theo" — vì lịch 10 tuần gộp hai bài một buổi nên "buổi trước" không còn đúng. Đảo phần "giữ buổi học/này/trước (nghĩa phiên)" của quyết định 17/08.
- Sweep 42 file: 14 deck (02–15, kể cả 09 chưa lên lịch) + `lecture-template.html` + 14 notebook bài giảng + 13 lab + trang đề BTL; ~150 chỗ. Giữ "buổi" thật sự là phiên: "buổi vấn đáp", "sau buổi học" (lab-14), "buổi học đầu tiên" (ai-policy). Đo tràn 14 deck: 0 slide tràn. Deck 1 slide "Lộ trình 15 bài" đã sửa trước đó (đợt 25).

## Quyết định của giảng viên (10/09/2026: khai báo phiên bản Python cho BTL)

- Repo BTL phải commit `.python-version` ở gốc, chứa một dòng phiên bản Python đầy đủ `3.x.y` mà nhóm đã kiểm thử. `3.12.3` trong đề chỉ là ví dụ; mỗi nhóm tự chọn bản phù hợp.
- `README.md` tham chiếu `.python-version`, ghi hệ điều hành, kiến trúc máy, công cụ cài thư viện và hướng dẫn dựng môi trường/chạy lại. `requirements.txt` hoặc lockfile ghim phiên bản thư viện.
- Có thể tạo `.python-version` bằng trình soạn thảo; không bắt buộc dùng uv/pyenv. Khi dùng pip/venv, cần chọn đúng Python lúc tạo môi trường.
- Đồng bộ yêu cầu trong đề BTL, cây repo mẫu, checklist Bài 15 và phần môi trường Python của Bài 1 trên nhánh draft. Bài 1 thêm slide `.python-version` ngay sau `requirements.txt`; sửa diễn giải để không coi riêng danh sách thư viện là đủ tái lập toàn bộ môi trường.

## Quyết định của giảng viên (14/09/2026 — bỏ mốc proposal, hạn final tuần 11)

- **Bỏ Mốc 2 "git tag proposal"** (đề xuất 2–3 trang, GV phản hồi không chấm). Còn 3 mốc: (1) lập nhóm/repo/nhận thành phố **23:59 Chủ nhật 20/09/2026 (tuần 2)**, (2) `git tag final` **23:59 Chủ nhật 22/11/2026 (tuần 11)** — GV cho ngày chính thức cùng ngày, ghi thẳng lên trang đề; suy ra **tuần 1 = 07–13/09/2026** (dùng được cho lịch Canvas sau này), (3) vấn đáp **theo lịch thi của Trường** (không phải lịch GV đặt trên Canvas).
- Đã sửa: `projects/project_airbnb.html` (timeline + dòng deliverables "có tag proposal và final"), hình lộ trình (`tools/roadmap`: bỏ marker proposal, final đặt ở ga cuối "sau T10" với nhãn "final · T11"), gói Canvas (`tools/canvas`), CLAUDE.md. Lưu ý: ga cuối trên hình vừa là "final T11" vừa là vấn đáp — chấp nhận vì vấn đáp diễn ra sau khi nộp final.
- **Bỏ mục "Lỗi thường gặp"** (10 gạch đầu dòng về dữ liệu: hai bản listings, giá chuỗi, lược đồ lệch, id 18–19 chữ số…) khỏi `project_airbnb.html` phần 02 — GV yêu cầu 14/09; xoá luôn CSS `.pitfall-list`. Nội dung đó vẫn nằm rải trong lab/deck (bài 6, 10).
- **Rút gọn danh sách tệp Inside Airbnb** (phần 02 trang đề): chỉ tên tệp + vai trò vài chữ; bỏ số cột, kiểu giá, danh sách cột calendar, ghi chú geojson, "show archived data". GV: "sinh viên phải tự figure it out". Thêm câu: cấu trúc tệp và điểm lạ của mỗi bản chụp do nhóm tự khảo sát, ghi vào phần QA.

## Quyết định của giảng viên (14/09/2026 — bỏ thành phố đối chứng; chấm bằng bộ test chung, chạy lại cả LLM)

- **Bỏ "thành phố đối chứng"** (baseline city): mỗi nhóm chỉ một thành phố. Gỡ khỏi trang đề (fact-card, mốc 1, "Phân công thành phố", thu thập, QA, KPI "ba chiều"→"hai chiều", trực quan "bốn góc"→"ba góc", config `control_city`), deck 1 (caption BTL), lab-13 (checklist), gói Canvas, teaching notes, CLAUDE.md. **Giữ nguyên "phương pháp đối chứng không LLM"** (regex/từ khoá vs LLM, bài 7/10/11) — nghĩa khác, không đụng.
- **Chấm bằng một bộ test chung cho mọi nhóm**, chạy trên repo nhóm: dựng môi trường theo README → một lệnh → soát tệp đầu ra; **bước LLM chạy lại thật** với khoá API do GV đặt trong biến môi trường (đảo "GV không gọi lại API" 07/2026). `--skip-llm` + cache chỉ còn là công cụ phát triển. Held-out snapshot không còn là cơ chế riêng; bộ test có thể dùng mốc GV chọn. Rubric A đổi "mốc giữ lại" → "bộ test chung"; deck 15 "máy sạch" + đoạn chấm sửa theo. ⚠️ Giả định cần GV xác nhận: khoá API khi chấm là **của GV** (qua biến môi trường), không phải của nhóm.
- **Rút gọn các mục 2–6 của phần Công việc** (thu thập, QA, KPI, trực quan hoá, báo cáo) còn 2–3 gạch đầu dòng mỗi mục — GV: "viết ngắn hơn nữa". Rubric C "bốn góc" → "ba góc" cho khớp. Deck 10 + lab-10: gỡ "held-out", "thành phố đối chứng", "bản đề xuất" (checklist mục 3 thay bằng "kế hoạch phân tích"). Đo tràn deck 1/10/15: 0.
- **Rút gọn phần 04 "Phân tích dùng LLM"** còn 6 gạch đầu dòng + callout 2 câu (GV: "ngắn hơn nhiều, đừng hướng dẫn chi tiết"). Bỏ: đoạn dịch máy khi gán nhãn, mô tả batch/retry/cache, "vài nghìn đánh giá". Giữ yêu cầu cứng: schema/enum, Gemini free, đối chứng không LLM + ≥100 nhãn tay + accuracy/F1 + phân tích lỗi, ước tính chi phí, ≥1 KPI và 1 hình dùng LLM, nêu ≥1 lỗi thật.
- **Bảng phân công thành phố thu gọn** (`<details>` đóng mặc định, summary "Danh sách thành phố và bốn mốc chụp (26 thành phố)") — GV 14/09, trang quá dài. Đoạn dẫn "bốn mốc bản chụp… bắt buộc" vẫn hiện.
- **Rút gọn "Môi trường chạy và thư viện"** (phần 06) còn 5 gạch đầu dòng: Python 3 + thư viện tự chọn, `.python-version`, `requirements.txt` ghim, README (cài/chạy/biến môi trường khoá API), tự kiểm máy sạch. Bỏ hai đoạn fine-print (uv/pyenv, pip freeze) và mô tả OS/kiến trúc máy.
