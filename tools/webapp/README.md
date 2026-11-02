# Web App — dashboard chạy trên Apps Script

Bản báo cáo **không phụ thuộc claude.ai**. Google phục vụ chính trang này, nên nó
cùng gốc với Google Sheet: gọi `google.script.run` là ghi được ngay.

```
Claude phân tích hội thoại  →  <tên kỳ>.json  →  thư mục Drive
                                                      ↓
                                   Web App  ──→  dashboard hiển thị
                                      ↕
                              Google Sheet (ngân hàng hook)
```

## Vì sao có bản này

Bản artifact trên claude.ai chạy trong sandbox: CSP chặn mọi lời gọi mạng và
cửa sổ thường không được cấp capability `mcp`. Trang ⛔ không tự ghi vào Sheet
được, phải lách qua «mở cửa sổ mới» rồi người dùng tự xác nhận. Ở đây không còn
cái vòng đó — cũng ⛔ không cần token, không cần connector, không cần bật pop-up.

| | artifact | web app |
|---|---|---|
| Đọc Sheet | chỉ khi được cấp `mcp` | luôn luôn |
| Ghi Sheet | mở tab rồi xác nhận tay | bấm là xong |
| Người gửi | gõ tay | tự lấy email đang đăng nhập |
| Dữ liệu kỳ | file kèm trang | file JSON trong Drive, thay lúc nào cũng được |

## Hai file

| File | Là gì |
|---|---|
| `Code.gs` | server — phục vụ trang, đọc/ghi Sheet, đọc JSON kỳ từ Drive |
| `trang.html` | **sinh tự động** bởi `dung.py` từ `dashboard/index.html` |

⛔ Đừng sửa `trang.html`. Sửa `dashboard/index.html` rồi chạy lại:

```bash
python tools/webapp/dung.py
```

`dung.py` chỉ thay **tầng truyền dữ liệu** (`fetch`/`mcp` → `google.script.run`),
toàn bộ phần vẽ dùng chung một nguồn. Nếu `dashboard/index.html` đổi tới mức
không còn khớp mốc, script dừng và nói rõ mốc nào — ⛔ không vá bừa.

## Cài

1. [script.new](https://script.new) → đặt tên project (vd *Insight Kangnam*).
2. Dán `Code.gs` đè vào file mặc định.
3. **+ → HTML** → đặt tên đúng chữ **`trang`** → dán toàn bộ `trang.html`.
4. Kiểm cấu hình ở đầu `Code.gs` (hoặc đặt Script properties cùng tên):

   | Hằng | Giá trị hiện tại |
   |---|---|
   | `SHEET_ID` | `1MJbv_M5Sh3BPntLnj9mqS8c4QNXYmwyRC_1Mj_Y4j2Q` — bảng *Insight KN* |
   | `TEN_SHEET` | `Trang tính1` — sai tên thì tự lùi về trang tính đầu |
   | `THU_MUC` | `1iBU86XL6R5BUxcDWpPTvPrvuVjUOi9jp` — thư mục Drive chứa JSON kỳ |

⚡ Ba hằng này đọc qua `cauHinh()`, tức **Script property cùng tên đè lên code**.
Đổi bảng hay đổi thư mục chỉ cần sửa Script property — ⛔ không phải deploy lại.
Thư mục chứa lẫn bảng tính hay tài liệu khác cũng được: `apiKy()` chỉ nhận `.json`.

5. Thả file kỳ vào thư mục Drive đó. Lấy sẵn ở
   [`dashboard/data/24-29-10.json`](../../dashboard/data/24-29-10.json) —
   **tên file là nhãn kỳ** hiện trên ô chọn, nên giữ dạng `24-29-10.json`.
6. **Deploy → New deployment → Web app**
   - *Execute as*: **User accessing the web app** — mỗi người ghi bằng quyền của
     chính họ, và cột *Người gửi* tự điền email thật thay vì gõ tay.
   - *Who has access*: **Anyone with Google account** (hoặc trong tổ chức).
7. Mở Web app URL.

Sửa `Code.gs` hay `trang.html` xong phải **Deploy → Manage deployments → ✏️ Edit
→ Version: New**, không thì bản cũ vẫn chạy.

## Kiểm nhanh

```
<web app url>?api=ping
→ {"ok":true,"bang":"Insight KN","sheet":"Trang tính1","dong":15,
   "toi":"ban@example.com","thu_muc":true}
```

`thu_muc:false` = chưa khai `THU_MUC`. `dong:1` = Sheet mới có mỗi dòng tiêu đề.

## Luật ghi — giữ nguyên

Server chỉ ghi hai dải **F:L** và **R:V**.

⛔ **Cột Q (Duyệt)** là ô của bác sĩ và pháp chế — không bao giờ chạm.
⛔ **Cột M–P** (Cơ hội win · Phản đối · Truy ngược · Cờ pháp chế) truy ngược về
hội thoại gốc, cũng khoá — trừ lúc tạo dòng mới.

`suaHook()` đọc giá trị đang có trước rồi chỉ thay trường được gửi lên, nên sửa
một trường ⛔ không xoá mất các ô khác trong dải.

## API phía trang gọi

| Hàm | Làm gì |
|---|---|
| `apiPing()` | tên bảng · trang tính · số dòng · email người xem |
| `apiDocHook()` | toàn bộ hook, mỗi dòng thành object có tên trường |
| `apiSua(ma, truong)` | sửa một hook |
| `apiTao(hook)` | thêm hook gõ tay, mã `KN-ART-nnn` sinh tự động |
| `apiGui(mas, nguoi, ghi_chu)` | chốt cả lô, cùng một mốc thời gian |
| `apiKy()` | danh sách kỳ trong thư mục Drive |
| `apiDuLieu(file_id)` | JSON của một kỳ |

## Menu trong Sheet

`Code.gs` cũng gắn menu **Hook Kangnam** vào bảng: *Kiểm tra dữ liệu* · *Xuất
file order* · *Khoá cột Duyệt*. Phần này chạy ⛔ không cần deploy.

## Đổi kỳ

Thả file JSON mới vào thư mục Drive. Trang đọc lại danh sách mỗi lần mở, kỳ mới
sửa gần nhất đứng đầu — ⛔ không phải deploy lại, không phải sửa code.

## Bố cục

Mặc định là bố cục `insight`. Xem bản khác bằng tham số URL:

```
<web app url>?bo_cuc=truc-page
<web app url>?bo_cuc=day-du
```
