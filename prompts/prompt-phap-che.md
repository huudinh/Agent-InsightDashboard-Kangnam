# prompt-phap-che · soát CỔNG 2 trước khi phát

> Chạy **trước khi** phát sổ tay, đăng hook, hay gửi dashboard ra ngoài khối.

---

```
SOÁT CỔNG 2

BẢN CẦN SOÁT: <dán nội dung, hoặc tên file>

Theo id-K, soát từng dòng theo 12 điểm pháp chế L01–L12 và bảng chặn §6.

IN RA BA KHỐI:

🔴 CHẶN — không phát được
   dòng · vi phạm điểm nào · vì sao · CÂU THAY THẾ dùng được ngay

🟡 HỎI LẠI
   dòng · cần ai duyệt · chờ gì

🟢 SẠCH
   số dòng

SÁU THỨ HAY LỌT NHẤT:
  ① con số bảo hành ("trọn đời", "10 năm", "3 năm" cho dịch vụ ngoài mắt)
     → thay bằng "chính sách bảo hành bằng văn bản"
  ② giá dịch vụ ngoài mắt khi chưa có bảng giá hiện hành
     → bỏ số, hoặc đổi thành "báo giá theo tình trạng sau khi bác sĩ khám"
  ③ chức danh / số năm / số ca của bác sĩ chưa đối chiếu chứng chỉ
     → bỏ tên bác sĩ, nói theo kỹ thuật
  ④ câu trả lời bệnh nền / chống chỉ định
     → "trường hợp này cần bác sĩ khám trực tiếp đánh giá"
  ⑤ cam kết kết quả chắc chắn
     → mô tả điều kiện, không hứa kết quả
  ⑥ số giấy phép sai cơ sở, hoặc nội dung local cơ sở ngoài 2 bệnh viện
     → gắn đúng giấy phép của cơ sở xuất hiện trong bài

⛔ Còn MỘT dòng 🔴 thì ⛔ không phát bản đó.
   Gỡ dòng ra hoặc thay câu, rồi soát lại từ đầu.
```

---

## Nhắc ba thứ đang chặn cả hệ

| # | Thứ còn thiếu | Ai cấp | Chặn gì |
|---|---|---|---|
| ① | **Chính sách bảo hành bằng văn bản** — ba mức đang cùng lưu hành | Vận hành + pháp chế | 🔴 Mọi nội dung và mọi câu trả lời chạm `O-07` |
| ② | **Bảng giá hiện hành** dịch vụ ngoài mắt | Vận hành / sales | 🔴 Hook `A4` có giá · format `L11` · tiêu chí `N3.1` |
| ③ | **Đối chiếu chứng chỉ** bác sĩ đang chạy ads | Vận hành + pháp chế | 🔴 Mọi nội dung gắn chức danh / số năm / số ca |

★ Mục ① cấp bách nhất: nó vừa chặn nội dung, vừa là cờ đỏ `CĐ-2` mà trực page đang vi phạm trong hội thoại thật.
