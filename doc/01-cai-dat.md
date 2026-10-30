# 01 · Cài đặt

📘 **Bản có nút Copy từng file:** <https://claude.ai/artifact/PkfQjahnMx9Vfb3KxpM7wh>
*(2 thẻ bộ não · 19 file tri thức · 16 prompt · 6 câu smoke test — dễ dùng hơn file này)*

Ba cách dùng agent này. Chọn một.

---

## A · Claude Project *(khuyến nghị)*

1. Tạo Project mới, tên: **Insight Dashboard Kangnam**.
2. Dán toàn bộ [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md) vào ô **Custom instructions**.
3. Nạp vào **Knowledge**:
   - 11 file trong [`knowledge/`](../knowledge/)
   - 8 file trong [`prompts/`](../prompts/)
4. Nạp thêm file dữ liệu của kỳ khi chạy: hội thoại + số ads.

Nền tảng giới hạn số file → dùng [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md) *(bản gộp, sinh tự động)*.

---

## B · ChatGPT Custom GPT

Ô **Instructions** giới hạn 8.000 ký tự → dán [`SYSTEM-PROMPT-NGAN.md`](../SYSTEM-PROMPT-NGAN.md) *(5.552 ký tự)*.
Phần còn lại nạp vào **Knowledge** như cách A.

Sau mỗi lần sửa bản ngắn, chạy:

```bash
python tools/dem-ngan.py
```

---

## C · Gemini Gem

Ô **Chỉ dẫn**: dán [`SYSTEM-PROMPT.md`](../SYSTEM-PROMPT.md). Knowledge như cách A.

---

## Chuẩn bị dữ liệu mỗi kỳ

Tạo thư mục `du-lieu/` *(đã bị `.gitignore` chặn — ⛔ không commit dữ liệu khách)*:

```
du-lieu/
├── hoi-thoai.md        ① bắt buộc — xuất từ Caresoft, khuôn ở id-B §2
├── ads-facebook.csv    ② nên có   — cột ở id-B §3
└── google-ads.csv      ③ 🔴 chưa có — khung ở template/MAU_google-ads.csv
```

File mẫu để chạy thử ngay khi chưa có dữ liệu thật:

```bash
python tools/id.py doc template/MAU_hoi-thoai.md --ky "19-25/10"
python tools/id.py ads template/MAU_ads-facebook.csv --ky "19-25/10"
python tools/id.py bao-cao --ky "19-25/10"
```

---

## Dashboard

Trang `dashboard/index.html` **không bao giờ sửa**. Mỗi kỳ chỉ sinh thêm một file JSON trong `dashboard/data/`, trang tự đọc `data/index.json` và cho chọn kỳ.

Mở bằng một máy chủ tĩnh *(mở thẳng `file://` thì trình duyệt chặn `fetch`)*:

```bash
cd dashboard && python -m http.server 8080
# rồi mở http://localhost:8080
```

Muốn gửi link cho người khác: publish `dashboard/` thành một Artifact — link cố định, các kỳ sau chỉ cần cập nhật file JSON.

📈 **Bản demo đã publish:** <https://claude.ai/artifact/79zY1N3Ltg2kk33JzLg66y>
*(295 hội thoại thật 12–13/10 · số quảng cáo mô phỏng · tên nhân viên đã ẩn danh)*

⚠️ **Trước khi publish:** file JSON có **tên nhân viên thật** trong `nhan_vien.ca_nhan`. Thay bằng mã `NV-01…` nếu bản publish có người ngoài khối xem được — rào an toàn ④ của [`id-F §7`](../knowledge/id-F-cham-diem-nhan-vien.md).

---

## Kiểm sau khi cài

Hỏi agent 6 câu, trả lời sai câu nào thì nạp lại file tương ứng:

| Câu hỏi | Phải trả lời đúng | Nằm ở |
|---|---|---|
| *"Chân dung lấy ở đâu ra?"* | ⛔ Không có bộ dựng sẵn — phác họa từ chính hội thoại của kỳ, duyệt ở CỔNG 0 | `id-C` §1–2 |
| *"Năm tín hiệu nóng là gì?"* | dịch vụ · thời gian ≤14 ngày · SĐT · điều kiện · khung giờ gọi | `id-D` |
| *"CPL tăng vì CPM thì làm gì?"* | Nói thẳng "không phải vấn đề nội dung" | `id-E` |
| *"Khách hỏi bảo hành mấy năm thì trả lời sao?"* | ⛔ Không nêu số — "chính sách bảo hành bằng văn bản" | `id-K` |
| *"Nhân viên có 7 hội thoại thì xếp loại gì?"* | Chưa đủ mẫu — ⛔ không phân loại | `id-F` |
| *"Ô có 60% HT rơi do trực page thì làm nội dung gì?"* | ⛔ Không làm nội dung — sửa vận hành trước | `id-G` |
