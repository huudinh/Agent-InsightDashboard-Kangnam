# id-I · ★ SỔ TAY THỰC THI CÁ NHÂN HOÁ

> Đầu ra cuối cùng và là thứ duy nhất **chạm tới từng con người**. Dashboard để lãnh đạo nhìn; sổ tay để nhân viên làm.
>
> ⚠️ **Khuôn trong sổ này là bản dựng tạm.** Người dùng sẽ gửi mẫu sổ tay chính thức; khi có, thay §3 và ghi lại ở `doc/CHANGELOG.md`. Mọi phần khác giữ nguyên.

---

## 1. BA LOẠI SỔ TAY

| Loại | Cho ai | Dài | Chứa tên ai |
|---|---|---|---|
| **ST-CN** | Một nhân viên trực page | **1 trang** | Chỉ người đó |
| **ST-TN** | Trưởng nhóm | 2–3 trang | Cả nhóm — ⛔ không phát ra ngoài nhóm |
| **ST-ND** | Người làm nội dung | 1–2 trang | ⛔ Không có tên nhân viên nào |

⛔ **ST-CN của người A ⛔ không bao giờ chứa tên, điểm hay hội thoại của người B.** Vi phạm là `CĐ-5` áp cho chính agent.

---

## 2. LUẬT MỘT VIỆC

```
Sổ tay loại D : ĐÚNG MỘT việc.
Sổ tay loại C : tối đa HAI việc.
Sổ tay loại B : ĐÚNG MỘT việc (nhóm yếu nhất).
Sổ tay loại A : MỘT việc nâng cấp + 2 đoạn chat mẫu để chia sẻ cho khối.
```

★ Sổ tay 7 việc là sổ tay 0 việc. Người đang làm sai 5 nhóm mà nhận danh sách 5 việc sẽ không sửa nhóm nào.
★ Việc được chọn là **nhóm `N` mất nhiều điểm nhất**, ⛔ không phải nhóm dễ sửa nhất.

---

## 3. KHUÔN `ST-CN` — SỔ TAY MỘT NHÂN VIÊN

```markdown
# SỔ TAY THỰC THI · <Tên nhân viên>
Kỳ <tu> → <den> · <n> hội thoại · <điểm>/100 · loại <A|B|C|D>

> Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.

## 1 · KỲ NÀY BẠN LÀM TỐT NHẤT ĐIỀU GÌ
<nhóm N mạnh nhất> — <% đạt> (khối: <% đạt của khối>)
Ví dụ từ chính bạn: HT-<nnn> — "<nguyên văn câu làm tốt>"

## 2 · ★ MỘT VIỆC CỦA KỲ TỚI
**<Tên việc — viết như một hành động, không phải một phẩm chất>**

Vì sao: <nhóm N yếu nhất> đạt <x>% trên <n> hội thoại áp dụng.
        Ước tính <m> lead rơi vì điều này.

Bằng chứng — 2 hội thoại của chính bạn:
  HT-<nnn> · khách hỏi "<...>" → bạn trả lời "<...>" → khách im luôn
  HT-<nnn> · <...>

Làm thế nào — câu mẫu dùng được ngay:
  ✅ "<câu đúng 1>"
  ✅ "<câu đúng 2>"
  ⛔ "<câu đang dùng, vì sao hỏng>"

Đo thế nào ở kỳ sau: <tiêu chí N>.<x> từ <a>% lên <b>%

## 3 · KHÁCH CỦA BẠN LÀ AI
Chân dung gặp nhiều nhất: <CD> · <tên> (<n>/<N> hội thoại)
Họ đang sợ: <mã O cao nhất> — <tên mã>
Câu hỏi ngầm: "<...>"
→ Ba câu trả lời sẵn cho tệp này:
  1. <...>
  2. <...>
  3. <...>

## 4 · ⛔ BA ĐIỀU TUYỆT ĐỐI KHÔNG
- ⛔ Không nêu con số bảo hành — nói "chính sách bảo hành bằng văn bản"
- ⛔ Không trả lời câu bệnh nền — chuyển "cần bác sĩ khám trực tiếp đánh giá"
- ⛔ Không cam kết kết quả chắc chắn
<thêm dòng nếu người này có cờ đỏ trong kỳ — ghi rõ HT-nnn>

## 5 · KIỂM TRƯỚC KHI ĐÓNG MỖI HỘI THOẠI
- [ ] Đã hỏi tình trạng trước khi xin số chưa?
- [ ] Đã nêu được khung giá hoặc nói rõ vì sao chưa nêu được chưa?
- [ ] Đã hỏi khung giờ nghe máy chưa?
- [ ] Đã mời lịch có ngày + giờ cụ thể chưa?
- [ ] <mục riêng theo việc ở phần 2>
```

---

## 4. KHUÔN `ST-TN` — SỔ TAY TRƯỞNG NHÓM

```markdown
# SỔ TAY TRƯỞNG NHÓM · <tên nhóm>
Kỳ <tu> → <den>

## 1 · PHÂN BỐ NHÓM
A: <n> · B: <n> · C: <n> · D: <n> · chưa đủ mẫu: <n>

## 2 · BA TIÊU CHÍ YẾU NHẤT CỦA NHÓM
<N>.<x> — <y>% đạt — đây là nội dung buổi đào tạo 15 phút kỳ tới

## 3 · AI KÈM AI
<người loại A> kèm <người loại D> — về đúng tiêu chí <N>.<x>
(người A đạt <a>%, người D đạt <b>% trên cùng tiêu chí)

## 4 · CỜ ĐỎ CẦN XỬ TRONG 48 GIỜ
<mã CĐ> · <người> · HT-<nnn> · nguyên văn: "<...>" · xử thế nào

## 5 · VIỆC KHÔNG PHẢI CỦA NHÓM BẠN
<các ô "—" do lỗi hệ> → đã đẩy lên mục hệ thống của dashboard
```

★ Mục 5 là mục giữ cho trưởng nhóm không bị đổ oan những việc mà hệ thống mới sửa được.

---

## 5. KHUÔN `ST-ND` — SỔ TAY NGƯỜI LÀM NỘI DUNG

```markdown
# SỔ TAY NỘI DUNG · kỳ <tu> → <den>

## 1 · <n> Ô ĐƯỢC CHỌN (ma trận đã duyệt <ngày>)
<bảng: # · khối · CD · nấc · điểm · hướng nội dung · format · deadline>

## 2 · NGÂN HÀNG HOOK KỲ NÀY — <n> hook
<bảng theo khuôn id-H §4>

## 3 · NỘI DUNG PHẢI DỪNG
<các nội dung 🔴 KÉM + mã O thấp → bỏ hẳn>

## 4 · Ô ĐANG PHÍ
<ô ③ của ma trận CD×5A — nhiều nội dung, ít người hỏi>

## 5 · ⛔ CỜ PHÁP CHẾ TRƯỚC KHI SẢN XUẤT
<danh sách 🔴 🟡 kèm câu thay thế>
```

---

## 6. VIẾT VIỆC THẾ NÀO CHO SỬA ĐƯỢC

| ⛔ Viết thế này | ✅ Viết thế này |
|---|---|
| *"Cần chủ động hơn"* | *"Sau khi khách im 30 phút, nhắn lại một câu hỏi về tình trạng — không nhắn lại lời chào"* |
| *"Kỹ năng khai thác yếu"* | *"Hỏi 1 câu về tình trạng **trước** khi gõ câu xin số"* |
| *"Chưa biết chốt"* | *"Thay 'khi nào rảnh chị qua' bằng 'chiều mai 15h em giữ chỗ cho chị nhé'"* |
| *"Thái độ chưa tốt"* | *"Bỏ câu 'chị đọc kỹ giúp em' — thay bằng nhắc lại đúng điều chị vừa hỏi"* |

★ Mỗi việc phải kiểm được bằng **ctrl-F trong hội thoại kỳ sau**. Việc không kiểm được là việc không tồn tại.

---

## 7. NHỊP PHÁT

| Khi nào | Ai nhận | Qua đâu |
|---|---|---|
| Ngay sau CỔNG 2 | Trưởng nhóm — `ST-TN` | Bản riêng |
| Sau khi trưởng nhóm đọc xong | Từng nhân viên — `ST-CN` | **Bản riêng của từng người** |
| Cùng lúc | Người làm nội dung — `ST-ND` | Chung |

⛔ Không phát `ST-CN` vào nhóm chat chung. ⛔ Không đính kèm nhiều `ST-CN` trong một file.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Mỗi `ST-CN` có **đúng số việc** theo loại A/B/C/D không?
- [ ] Việc được chọn có phải nhóm `N` **mất nhiều điểm nhất** không?
- [ ] Mỗi việc có **câu mẫu dùng được ngay** không, hay chỉ có lời khuyên?
- [ ] Mỗi việc có **cách đo ở kỳ sau** không?
- [ ] Có `ST-CN` nào chứa tên người khác không?
- [ ] Câu *"Điểm dùng để phân việc kèm cặp…"* có ở đầu mọi `ST-CN` không?
- [ ] Lỗi hệ có bị viết thành việc của nhân viên không?
