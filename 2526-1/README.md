# Lập trình Xử lý Dữ liệu — Học kì 1, năm học 2025–2026

**@Giảng viên:** Vui lòng cập nhật các file `lecture-XX.html` cho từng buổi học khi cần. Bạn có thể dùng các bài giảng hiện có làm tham khảo.

## Nội dung học kì

| Tuần | Bài giảng |
|------|-----------|
| 1 | Bài 1: Giới thiệu |
| 2 | Bài 2: Luồng điều khiển & Cấu trúc dữ liệu |
| 3 | Bài 3: Hàm, Module & Xử lý file |
| 4 | Bài 4: Xử lý lỗi & Lập trình hướng đối tượng |
| 5 | Bài 5: NumPy — Mảng & Tính toán vector hoá |
| 6 | Bài 6: Bắt đầu với Pandas |
| 7 | Bài 7: Nạp, lưu trữ, làm sạch & chuẩn bị dữ liệu |
| 8 | Bài 8: Xử lý dữ liệu chuỗi thời gian |
| 9 | Bài 9: Trực quan hoá dữ liệu với Python |
| 10 | Bài 10.1: Xử lý chuỗi ký tự; Bài 10.2: Pandas — Tổng hợp & Groupby |

## Chạy slide

Thư mục này chứa slide bài giảng viết bằng Reveal.js, có thể serve qua GitHub Pages hoặc máy chủ web cục bộ.
Hai cách chạy dưới đây dùng hai cổng mặc định khác nhau theo cấu hình hiện tại: Node.js dùng `8000`, còn Python dùng `8765`.

### Cách 1: Node.js (hỗ trợ ghi chú giảng viên & tự động tải lại)

1. Cài [Node.js](https://nodejs.org/).
2. Trong thư mục `2526-1`, chạy `npm install` để cài dependencies.
3. Chạy `npm start` để khởi động server (port 8000).
4. Mở trình duyệt và truy cập http://localhost:8000.

### Cách 2: Python (không cần cài thêm gì)

```bash
# Nếu đang ở thư mục gốc của repo
cd 2526-1
python3 -m http.server 8765
# Mở http://localhost:8765
```

### Serve qua GitHub Pages

Không cần cấu hình gì thêm. Chỉ cần push thay đổi lên nhánh `main`, GitHub Pages sẽ tự động serve nội dung.

## Tạo bài giảng mới

1. Copy `lecture-template.html` thành file mới đặt tên theo dạng `lecture-XX-ten-bai.html`.
2. Chỉnh sửa tiêu đề, ngày và nội dung bài giảng.
3. Commit và push file mới lên repository.
