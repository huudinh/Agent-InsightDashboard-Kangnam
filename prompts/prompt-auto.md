# prompt-auto · chạy cả kỳ một phát

> Dán vào Claude/ChatGPT/Gemini đã nạp bộ não + 11 sổ tri thức. Đính kèm file hội thoại và file ads.
> ⚠ `AUTO` đi qua **hai cổng**: CỔNG 0 duyệt chân dung, CỔNG 1 duyệt ma trận. Nó dừng ở cả hai.

---

```
AUTO

KỲ: <tu> → <den>
FILE HỘI THOẠI: <tên file đính kèm>
FILE ADS FACEBOOK: <tên file, hoặc "chưa có">
FILE GOOGLE ADS: chưa có
KỲ TRƯỚC: <tên file kết quả kỳ trước, hoặc "chưa có">

CHẶNG 1 — chạy B1 → B3 theo id-A §3, rồi DỪNG ở CỔNG 0.

In ra đúng bốn khối:

① CỠ MẪU
   đọc bao nhiêu · loại bao nhiêu · vì sao loại · khách mới / khách cũ

② NĂM THẺ SỐ TỔNG
   hội thoại mới · bỏ sau 1 lượt · có SĐT · trả lời tin đầu ≤2′ · HOT/WARM chưa có SĐT
   mỗi thẻ kèm so kỳ trước (hoặc "⚠ chưa có mốc so sánh")

③ NGUYÊN LIỆU PHÁC HỌA
   cụm chữ khách tự nói (đếm theo SỐ HỘI THOẠI) · phân bố nấc 5A · phân bố rào cản
   · 10 câu hỏi đầu đáng chú ý nhất, đã ẩn danh, kèm HT-nnn

④ BẢN PHÁC HỌA CHÂN DUNG — ⏳ CHỜ DUYỆT
   2–7 chân dung, mỗi chân dung: mã · tên (CHỮ CỦA KHÁCH) · họ là ai · NỖI SỢ
   · dấu hiệu nhận ra · hệ số giá trị đơn · HT-nnn làm bằng
   + số HT dự kiến rơi CD0, và nói rõ còn tách thêm được chân dung nào không
   + chân dung nào GIỮ NGUYÊN MÃ của kỳ trước vì cùng nỗi sợ

⛔ DỪNG tại đây. ⛔ Không gán chân dung. ⛔ Không viết thẻ insight.
⛔ Không dựng ma trận. ⛔ Không chấm điểm cá nhân. ⛔ Không tự điền người duyệt.
Chờ tôi gõ DUYỆT CHÂN DUNG.
```

---

## Sau khi xem bản phác họa

```
DUYỆT CHÂN DUNG
```
hoặc
```
SỬA CD<n> <điều chỉnh>
```

Rồi agent chạy chặng 2:

```
CHẶNG 2 — chạy B3' → B5, rồi DỪNG ở CỔNG 1.

In ra đúng bốn khối:

⑤ BẢNG CHÂN DUNG ĐÃ DUYỆT (+ dòng CD0)
   HT · HOT/WARM/COLD · có SĐT · % có SĐT · chốt lịch · bỏ 1 lượt · rơi do trực page
   ★ Tổng HT + CD0 phải BẰNG ĐÚNG cỡ mẫu phân tích
   + thẻ insight cho mỗi chân dung ≥5 HT (họ là ai · insight · câu hỏi ngầm ·
     tín hiệu nóng · hướng xử lý) — viết bằng CHỮ CỦA KHÁCH
   + ma trận CD×5A hai bảng N×5, đánh dấu ô ① LỖ HỔNG và ô ③ ĐANG PHÍ

⑥ BA VẤN ĐỀ CỐT LÕI
   xếp theo SỐ HỘI THOẠI BỊ ẢNH HƯỞNG, mỗi vấn đề: mức · số liệu · đề xuất · ai làm

⑦ CHUỖI CHỈ SỐ ADS (nếu có file)
   Chi phí tổng → CPM → CTR → CPI → CPL → CPB → Booking/Lead, mỗi mắt xích kèm mục tiêu + kỳ trước
   ★ Ô chi phí tổng kèm số nội dung · hiển thị · inbox · lead · booking của kỳ
   ⛔ Phân rã CPL TRƯỚC khi kết luận. Nếu thành phần hỏng không phải CTR thì
      nói thẳng "kỳ này không phải vấn đề nội dung".

⑧ MA TRẬN ƯU TIÊN — ba khối ① Tăng HOT → ② Giảm COLD → ③ Tối ưu WARM
   + nhóm 🔧 sửa vận hành trước + nhóm 👁 quan sát (chân dung dưới 5 HT)
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
