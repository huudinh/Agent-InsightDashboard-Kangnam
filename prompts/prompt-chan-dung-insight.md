# prompt-chan-dung-insight · phác họa chân dung & đào sâu insight

> Dùng khi chỉ cần phần khách hàng, chưa cần chấm điểm hay ads. Đây là phần **đọc hiểu** — script không làm thay.
> Chạy **hai lượt**, vì **CỔNG 0** nằm giữa: lượt ① phác họa và xin duyệt, lượt ② gán và viết thẻ insight.

---

## Lượt ① — PHÁC HỌA, dừng ở CỔNG 0

```
PHÁC HỌA CHÂN DUNG

FILE HỘI THOẠI: <tên file>
KỲ: <tu> → <den>
KỲ TRƯỚC: <tên file bản phác họa kỳ trước, hoặc "chưa có">

Theo id-C §1–2, làm đúng năm việc:

① GÁN TỪNG HỘI THOẠI — phần KHÔNG cần chân dung
   nấc 5A (đọc CÂU HỎI ĐẦU TIÊN của khách, ⛔ không đọc cả hội thoại)
   · mã O · mức nóng theo 5 tín hiệu · rào cản · vì sao rơi (ĐÚNG MỘT giá trị)
   ⚠ Ô chân dung để TRỐNG ở bước này.

② ĐỌC CHỮ CỦA KHÁCH
   Cụm chữ nào khách tự nói, lặp ở bao nhiêu HỘI THOẠI (⛔ không đếm số lần).
   ⛔ Cụm đông nhất chưa chắc là một chân dung: "nâng mũi" là DỊCH VỤ,
      không phải nỗi sợ.

③ PHÁC HỌA CHÂN DUNG CỦA KỲ — 2–7 chân dung, mỗi chân dung một bảng:
   MÃ            — CD1, CD2, … ⛔ không dùng CD0 (mã dự trữ)
   TÊN           — bằng CHỮ CỦA KHÁCH, ⛔ không bằng tính từ marketing,
                   ⛔ không lấy tên dịch vụ
   HỌ LÀ AI      — họ vào từ nội dung nào, tin đầu họ gõ gì
   NỖI SỢ        — một nỗi sợ riêng. Hai nhóm cùng nỗi sợ là MỘT chân dung
   DẤU HIỆU      — cụm chữ để nhận ra; xếp chân dung HẸP trước, RỘNG sau
   HỆ SỐ         — 1 · 2 · 3 theo giá trị đơn (id-G §3)
   TRÍCH         — ít nhất một HT-nnn làm bằng. ⛔ Không có trích = bịa = loại

④ CÒN LẠI BAO NHIÊU
   Số HT không khớp dấu hiệu nào → rơi CD0.
   ≥15 HT rơi CD0 → nói rõ: tách thêm được một chân dung, hay nhóm này
   thật sự chưa kể gì (→ lỗi của quảng cáo, ghi vào tab Phễu).

⑤ SO KỲ TRƯỚC
   Chân dung nào CÙNG NỖI SỢ với kỳ trước → GIỮ NGUYÊN MÃ cũ.
   Chân dung nào mới, chân dung nào kỳ này không còn.

⛔ DỪNG tại đây. ⛔ Không gán chân dung cho hội thoại. ⛔ Không viết thẻ insight.
⛔ Không dựng ma trận. ⛔ Không tự điền người duyệt.
Chờ tôi gõ DUYỆT CHÂN DUNG hoặc SỬA CD<n> <điều chỉnh>.
```

---

## Lượt ② — sau khi tôi duyệt

```
DUYỆT CHÂN DUNG
```
hoặc
```
SỬA CD3 gộp vào CD1 — cùng nỗi sợ
```

Rồi:

```
GÁN & VIẾT INSIGHT

Theo id-C §3–6, làm đúng sáu việc:

① GÁN CHÂN DUNG cho từng hội thoại theo dấu hiệu ĐÃ DUYỆT
   Hội thoại không khớp dấu hiệu nào → CD0.
   ★ Tổng HT các chân dung + CD0 phải BẰNG ĐÚNG cỡ mẫu phân tích (luật ④).

② BẢNG CHÂN DUNG
   CD · tên · số HT · HOT/WARM/COLD · có SĐT · % có SĐT · chốt lịch
   · bỏ 1 lượt · rơi do trực page   (+ dòng CD0)

③ BẢNG ĐẾM 12 MÃ O
   kể cả mã bằng 0. Tách riêng "(chưa nêu)" với "O-00".
   O-00 vượt 10% mẫu → BÁO LẠI để bổ sung từ điển, ⛔ đừng tự thêm mã.

④ THẺ INSIGHT cho mỗi chân dung ≥5 HT, năm ô:
   HỌ LÀ AI      — họ vào từ nội dung nào, tin đầu họ gõ gì, ở page nào
   INSIGHT       — điều họ đang tin / đang sợ, viết bằng chữ của họ
   CÂU HỎI NGẦM  — dịch câu họ gõ thành điều họ THẬT SỰ muốn biết
   TÍN HIỆU NÓNG — họ nóng lên khi nào
   HƯỚNG XỬ LÝ   — một việc cụ thể, không phải lời khuyên chung

⑤ TOP 10 CÂU CHÉP NGUYÊN VĂN
   câu hỏi đầu tiên hay nhất, đã ẩn danh, kèm HT-nnn.
   ★ Đây là nguyên liệu tốt nhất để viết hook ở bước sau.

⑥ MA TRẬN CD × 5A — hai bảng N×5 cạnh nhau (nội dung đang có · hội thoại trong kỳ),
   N = số chân dung đã duyệt + 1 dòng CD0.
   Đánh dấu ô ① LỖ HỔNG và ô ③ ĐANG PHÍ.

⑦ NỬA TRỰC PAGE TRẢ LỜI — insight tầng hai
   Điều gì trực page đang phải gõ tay nhiều lần mà đáng lẽ một clip làm?
   ⚠ Đây là đầu vào NỘI DUNG. Muốn thành điểm trừ nhân viên thì phải gắn
     tiêu chí N + HT-nnn theo id-F, ⛔ không viết nhận xét chung chung.

⑧ CỠ MẪU — đọc bao nhiêu, bỏ bao nhiêu, vì sao

⛔ Không để lọt tên thật, SĐT, ảnh, link cá nhân của khách.
⛔ Chân dung dưới 5 HT: không viết thẻ insight, chỉ ghi vào danh sách 👁 quan sát.
⛔ Không gộp hai chân dung có nỗi sợ khác nhau cho gọn bảng.
```
