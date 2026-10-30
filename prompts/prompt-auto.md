# prompt-auto · chạy cả kỳ một phát

> Dán vào Claude/ChatGPT/Gemini đã nạp bộ não + 11 sổ tri thức. Đính kèm file hội thoại và file ads.

---

```
AUTO

KỲ: <tu> → <den>
FILE HỘI THOẠI: <tên file đính kèm>
FILE ADS FACEBOOK: <tên file, hoặc "chưa có">
FILE GOOGLE ADS: chưa có
KỲ TRƯỚC: <tên file kết quả kỳ trước, hoặc "chưa có">

Chạy B1 → B5 theo id-A §3, rồi DỪNG ở CỔNG 1.

In ra đúng sáu khối:

① CỠ MẪU
   đọc bao nhiêu · loại bao nhiêu · vì sao loại · khách mới / khách cũ

② NĂM THẺ SỐ TỔNG
   hội thoại mới · bỏ sau 1 lượt · có SĐT · trả lời tin đầu ≤2′ · HOT/WARM chưa có SĐT
   mỗi thẻ kèm so kỳ trước (hoặc "⚠ chưa có mốc so sánh")

③ BẢNG CHÂN DUNG CD0–CD6
   HT · HOT/WARM/COLD · có SĐT · % có SĐT · chốt lịch · bỏ 1 lượt · rơi do trực page
   + thẻ insight cho mỗi chân dung ≥5 HT (họ là ai · insight · câu hỏi ngầm ·
     tín hiệu nóng · hướng xử lý) — viết bằng CHỮ CỦA KHÁCH

④ BA VẤN ĐỀ CỐT LÕI
   xếp theo SỐ HỘI THOẠI BỊ ẢNH HƯỞNG, mỗi vấn đề: mức · số liệu · đề xuất · ai làm

⑤ CHUỖI CHỈ SỐ ADS (nếu có file)
   CPM → CTR → CPI → CPL → CPB → Booking/Lead, mỗi mắt xích kèm mục tiêu + kỳ trước
   ⛔ Phân rã CPL TRƯỚC khi kết luận. Nếu thành phần hỏng không phải CTR thì
      nói thẳng "kỳ này không phải vấn đề nội dung".

⑥ MA TRẬN ƯU TIÊN — ba khối ① Tăng HOT → ② Giảm COLD → ③ Tối ưu WARM
   + nhóm 🔧 sửa vận hành trước + nhóm 👁 quan sát
   TRẠNG THÁI: ⏳ CHỜ DUYỆT

⛔ DỪNG tại đây. ⛔ Không viết hook. ⛔ Không sinh sổ tay. ⛔ Không chấm điểm cá nhân.
Chờ tôi gõ DUYỆT.
```

---

## Sau khi xem ma trận

```
DUYỆT
```
hoặc
```
SỬA <mã ô> <hướng mới>
```

Rồi agent chạy tiếp B6 → B8: chấm điểm nhân viên · sinh dashboard JSON · ngân hàng hook · sổ tay từng người · soát CỔNG 2.
