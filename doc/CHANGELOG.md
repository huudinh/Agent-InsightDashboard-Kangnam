# CHANGELOG

## v1.0 — 2026-10-30

Dựng mới `Agent-InsightDashboard-Kangnam`.

### Có gì

- `SYSTEM-PROMPT.md` *(7.502 ký tự)* + `SYSTEM-PROMPT-NGAN.md` *(5.552 ký tự, dưới trần 8.000 của ChatGPT)*
- **11 sổ tri thức** `id-A` … `id-K`
- **8 prompt mẫu**
- **Dashboard 9 tab** — trang HTML cố định đọc `data/*.json`, link không đổi giữa các kỳ
- **4 script chạy thật**: `id.py` *(doc · ads · bao-cao)*, `so_tay.py`, `gop-tham-khao.py`, `dem-ngan.py`
- Đã chạy end-to-end trên **300 hội thoại nâng mũi thật** xuất từ Caresoft — kết quả ở `doc/03-output-mau.md`

### Ba thứ khiến bản này khác các agent trước trong hệ

| # | Khác gì | Vì sao |
|---|---|---|
| ① | **Chấm điểm thang 100 + phân loại A/B/C/D** — trong khi `Agent-QC-Telesale` cố tình không chấm điểm số | Chat có bằng chứng đầy đủ và mốc thời gian chính xác đến giây, không có nhóm nào phụ thuộc âm thanh. Nhưng phải đi kèm **bốn rào an toàn** ở `id-F §7` — bỏ một cái là sổ này thành công cụ kỷ luật |
| ② | **Sổ tay thực thi cá nhân hoá** — đầu ra đầu tiên trong hệ chạm tới từng con người | Dashboard để lãnh đạo nhìn; sổ tay để nhân viên làm. Luật một việc: D và B 1 việc · C 2 việc · A 1 việc + 2 đoạn chat mẫu |
| ③ | **Nối mắt xích `inbox→lead` của công thức CPL với bằng chứng hội thoại** | Các agent ads khác chỉ suy đoán mắt xích này. Agent này chỉ thẳng ra bao nhiêu HT rơi do trực page và vì câu nào — nhờ đó dám nói *"kỳ này không phải vấn đề nội dung"* |

### Ba chỗ hiệu chỉnh đã phải sửa khi chạy dữ liệu thật

> Ghi lại vì ai port script sang brand khác sẽ gặp lại đúng ba chỗ này.

```
① Bản xuất Caresoft gắn 3 dòng hệ thống vào MỌI hội thoại đến từ quảng cáo
   ([Tệp đính kèm], 📞 Cuộc gọi thoại, "X đã gọi cho bạn").
   Đếm chúng là lượt của khách → "bỏ sau 1 lượt" ra 0,0%. Đã lọc.

② Khớp từ khoá theo substring làm "mí" khớp nhầm trong "mình",
   kéo theo cả bảng chân dung sai. Đã đổi sang khớp RANH GIỚI TỪ.

③ Từ khoá quá rộng ("tư vấn", "giá") làm một mã O nuốt 95% mẫu.
   Đã thu hẹp. Luật: thêm từ xong PHẢI chạy lại và nhìn cột % của bảng mã O.
```

---

## 🔴 Đang bị chặn — cần cấp để mở

| # | Thứ còn thiếu | Ai cấp | Chặn gì |
|---|---|---|---|
| ① | **Mẫu sổ tay thực thi chính thức** | Người dùng *(đã hẹn gửi)* | 🟠 Khuôn `ST-CN` ở `id-I §3` là bản dựng tạm — thay khi có mẫu thật |
| ② | **Chính sách bảo hành bằng văn bản** — ba mức *(3 năm / 10 năm / trọn đời)* đang cùng lưu hành | Vận hành + pháp chế | 🔴 Mã `O-07` · cờ đỏ `CĐ-2` · mọi hook chạm bảo hành. **Cấp bách nhất** — trực page đang vi phạm trong hội thoại thật |
| ③ | **Bảng giá hiện hành** dịch vụ ngoài mắt | Vận hành / sales | 🔴 Tiêu chí `N3.1` · hook `A4` có giá · format `L11`. Chưa có thì phần lớn ô *"né giá"* phải chấm `—` là **lỗi hệ**, ⛔ không trừ điểm nhân viên |
| ④ | **Đối chiếu chứng chỉ bác sĩ** đang chạy ads | Vận hành + pháp chế | 🔴 Cờ đỏ `CĐ-4` · mọi nội dung gắn chức danh |
| ⑤ | **Dữ liệu Google Ads** | Khối Ads | 🟠 Tab ⑤ trống. Khung đọc đã dựng sẵn ở `id-B §4` + `id-E §5` |
| ⑥ | **Mốc mục tiêu TB 30 ngày** từng dịch vụ | Khối Ads | 🟠 Mọi chỉ số ads hiện ghi `⚠ chưa có mốc so sánh` |
| ⑦ | **Xác nhận quy ước tên chiến dịch** 11 chiều | Khối Ads | 🟡 Bảng giải mã ở `id-E §2` đang là **suy ra từ dữ liệu**, chưa có văn bản |
| ⑧ | **Định nghĩa format `L13`–`L16`** | Content Lead | 🟡 Bốn mã này có trong kế hoạch hook nhưng chưa ai viết định nghĩa |

⚠️ **Mục ② cấp bách nhất.** Nó không phải bất tiện nội bộ: trong 6 hội thoại mẫu đã có người trả lời khách *"bên em bảo hành trọn đời"*, và trong hội thoại thật khách hỏi `O-07` đều đặn. Hệ thống đang để nhân viên tự chọn một trong ba con số.

---

## Việc còn treo trong repo

- [ ] `id.py` chưa đọc được cột `ref`/`ad id` trong hội thoại → nối hội thoại ↔ nội dung ads hiện phải làm tay *(`id-E §6`)*
- [ ] Chưa có khối `theo_ngay` cho biểu đồ Booking × CPB theo ngày như dashboard Meta hiện hành
- [ ] `nhiet_x_sdt` trong JSON mới tách `chua`/`co`, chưa tách `SĐT mới`/`SĐT cũ`
- [ ] Chưa có script so hai kỳ *(khối `truoc` trong schema đã có chỗ, chưa có công cụ điền)*
