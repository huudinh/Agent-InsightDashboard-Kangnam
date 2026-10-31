# prompt-doc-so-ads · đọc số quảng cáo & nối với hội thoại

---

```
ĐỌC SỐ ADS

FILE ADS FACEBOOK: <tên file>
FILE GOOGLE ADS: chưa có
KỲ: <tu> → <den>  ·  KỲ TRƯỚC: <...>

Theo id-E, làm năm việc:

① CHUỖI CHỈ SỐ — giữ ĐÚNG thứ tự
   Chi phí tổng → CPM → CTR → CPI → CPL → CPB → Booking/Lead
   Mỗi mắt xích ba thứ: giá trị · so MỤC TIÊU (TB 30 ngày của dịch vụ) · so KỲ TRƯỚC.
   Chưa có mốc → ghi "⚠ chưa có mốc so sánh". ⛔ Không tự đặt mốc.
   Ngày dưới 3 kết quả → ⛔ không vẽ lên đường CPB/CPL.

② ★ PHÂN RÃ CPL TRƯỚC KHI KẾT LUẬN
   CPL = (CPM/1000) ÷ (CTR × click→inbox% × inbox→lead%)
   Nói rõ thành phần nào xấu đi và đó là việc của ai:
     CTR giảm        → nội dung
     CPM tăng        → Adnet (tệp, bid, lịch) — "kỳ này KHÔNG phải vấn đề nội dung"
     click→inbox giảm→ kỹ thuật (điểm đến, lời chào tự động)
     inbox→lead giảm → TRỰC PAGE → chỉ ra bao nhiêu HT rơi do trực page và vì câu nào

③ CHẤM TỪNG NỘI DUNG 🟢🟡🔴 + bốn đường cải tiến
   🟢 CTR ≥ trung vị và CPL ≤ trung vị  → nhân bản
   🟡 một trong hai đạt                 → biến thể, đổi ĐÚNG MỘT biến
   🔴 + mã O vẫn cao                    → giữ ý, bỏ hook
   🔴 + mã O thấp                       → bỏ hẳn
   ⛔ Không đổi ≥3 biến cùng lúc.

④ NỐI HỘI THOẠI ↔ NỘI DUNG
   Mỗi nội dung: khách vào từ đó thuộc chân dung nào (theo bản đã duyệt CỔNG 0), hỏi mã O nào,
   bao nhiêu % bỏ sau 1 lượt. Gộp mọi ID cùng nội dung về MỘT dòng theo tên nội dung.
   Chiến dịch nhiều mẫu không tách được chi → bảng riêng, ⛔ không chia đều.

⑤ GOOGLE ADS
   Chưa có dữ liệu → ghi "⚠ chưa có dữ liệu Google Ads".
   ⛔ Không ước lượng. ⛔ Không lấy số Facebook gán sang.

⛔ Không so chéo CPL giữa hai line khác nhau.
⛔ Không trộn "nhân viên chạy ads" với "nhân viên trực page".
```

---

## Khi Google Ads có dữ liệu

```
ĐỌC GOOGLE ADS
FILE: du-lieu/google-ads.csv

① Chuỗi CPC → CTR → CPL theo chiến dịch, cùng khuôn với Facebook.
② Bảng SEARCH TERM: truy vấn · chi · click · chuyển đổi · MÃ O gán được ·
   quyết định (giữ / thêm từ phủ định / mở trang mới).
③ So kênh: cùng một mã O, Facebook tốn bao nhiêu và Google tốn bao nhiêu để ra 1 lead.
④ Truy vấn có người tìm mà Kangnam chưa có trang → bàn giao Agent-KN-GEO-Plant.
```
