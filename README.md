# 🎵 TechAway 2026: Basic Discord Music Bot

Dự án mã nguồn mở được phát triển trong khuôn khổ sự kiện học thuật **TechAway 2026 - Season 6** của Câu lạc bộ F-Code. 

Bot phát nhạc Discord này được thiết kế với cấu trúc mã nguồn tinh gọn và tối giản nhất. Mục tiêu của dự án là giúp các bạn sinh viên (đặc biệt là thế hệ F21) có thể dễ dàng tiếp cận, hiểu cách ứng dụng Python giao tiếp với API, xử lý luồng sự kiện bất đồng bộ (async/await) và truyền tải dữ liệu âm thanh (audio streaming) theo thời gian thực.

## 🚀 Tính năng cơ bản
- `!play <tên bài hát/link>`: Bot tự động tham gia kênh thoại, tìm kiếm và phát nhạc trực tiếp từ YouTube.
- `!pause`: Tạm dừng bài hát đang phát.
- `!resume`: Tiếp tục phát bài hát đang bị tạm dừng.
- `!stop`: Dừng toàn bộ nhạc, xóa bộ đệm và rời khỏi kênh thoại.

## 🛠️ Yêu cầu hệ thống (Prerequisites)
Để khởi chạy bot trên máy tính cá nhân (Localhost), hệ thống của bạn cần đáp ứng:
- **Python 3.8** trở lên.
- **FFmpeg**: Bộ công cụ xử lý đa phương tiện bắt buộc phải có để Discord có thể giải mã và phát âm thanh. *(Lưu ý: Cần thêm FFmpeg vào biến môi trường `Environment Variables/PATH` của Windows/macOS).*

## ⚙️ Hướng dẫn cài đặt (Installation)

**Bước 1: Sao chép (Clone) kho lưu trữ**
Mở Terminal hoặc Command Prompt và chạy lệnh sau:

```
git clone https://github.com/nguyenthaihuy0913/python-simple-musicbot.git
cd python-simple-musicbot
```
Bước 2: Cài đặt các thư viện phụ thuộc (Dependencies)
Cài đặt các thư viện cần thiết thông qua pip:
```
pip install discord.py yt-dlp PyNaCl
```
(Ghi chú: Thư viện PyNaCl là module bắt buộc để discord.py hỗ trợ tính năng Voice).

Bước 3: Cấu hình Token kết nối

Mở file main.py bằng trình soạn thảo code (VS Code, Sublime Text,...).

Cuộn xuống dòng cuối cùng của file.

Thay thế đoạn "DÁN_TOKEN_CỦA_BẠN_VÀO_ĐÂY" bằng Token Bot thực tế của bạn (Lấy từ trang Discord Developer Portal).

⚠️ CẢNH BÁO BẢO MẬT: Tuyệt đối không chia sẻ Token của bạn cho bất kỳ ai. Nếu bạn muốn đóng góp code (commit) lên lại GitHub, hãy nhớ xóa Token của mình đi trước khi push.

🏃‍♂️ Khởi chạy Bot
Sau khi hoàn tất cấu hình, khởi chạy bot bằng lệnh:

```
python main.py
```
Nếu Terminal hiển thị dòng thông báo: ✅ Khởi động thành công! Bot ... đã sẵn sàng nhận lệnh!, bạn đã có thể truy cập vào server Discord của mình, tham gia một kênh thoại bất kỳ và gõ lệnh !play để trải nghiệm.

👨‍💻 Tác giả
Thaihuy - Sinh viên F21, chuyên ngành Trí tuệ nhân tạo (AI).

Dự án chia sẻ kiến thức cộng đồng - TechAway 2026 (F-Code).