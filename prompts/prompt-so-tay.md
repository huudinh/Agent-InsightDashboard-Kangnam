# prompt-so-tay · viết sổ tay thực thi cá nhân hoá

> Chạy `python tools/so_tay.py --ky …` trước để có khung đã điền phần đếm được, rồi dùng prompt này điền phần đọc hiểu.

---

```
VIẾT SỔ TAY THỰC THI

KỲ: <tu> → <den>
KHUNG ĐÃ SINH: out/so-tay/

Theo id-I, điền mọi chỗ «agent điền: …» trong từng file.

LUẬT MỘT VIỆC:
  loại D : ĐÚNG MỘT việc
  loại C : tối đa HAI việc
  loại B : ĐÚNG MỘT việc (nhóm yếu nhất)
  loại A : MỘT việc nâng cấp + 2 đoạn chat mẫu để chia sẻ cho khối
★ Việc được chọn là nhóm N MẤT NHIỀU ĐIỂM NHẤT, ⛔ không phải nhóm dễ sửa nhất.
★ Sổ tay 7 việc là sổ tay 0 việc.

MỖI VIỆC PHẢI CÓ ĐỦ BỐN THỨ:
  ① viết như một HÀNH ĐỘNG, không phải một phẩm chất
  ② bằng chứng: 2 hội thoại CỦA CHÍNH NGƯỜI ĐÓ, kèm HT-nnn và nguyên văn
  ③ câu mẫu DÙNG ĐƯỢC NGAY: 2 câu ✅ và 1 câu ⛔ đang dùng kèm lý do hỏng
  ④ cách đo ở kỳ sau: tiêu chí N nào, từ bao nhiêu % lên bao nhiêu %

VIẾT VIỆC THẾ NÀO:
  ⛔ "Cần chủ động hơn"
  ✅ "Sau khi khách im 30 phút, nhắn lại một câu hỏi về tình trạng —
      không nhắn lại lời chào"
  ⛔ "Kỹ năng khai thác yếu"
  ✅ "Hỏi 1 câu về tình trạng TRƯỚC khi gõ câu xin số"
★ Mỗi việc phải kiểm được bằng ctrl-F trong hội thoại kỳ sau.
  Việc không kiểm được là việc không tồn tại.

PHẦN "KHÁCH CỦA BẠN LÀ AI":
  chân dung gặp nhiều nhất · mã O cao nhất · CÂU HỎI NGẦM ·
  ba câu trả lời sẵn cho tệp đó (⛔ không chạm O-07, O-12)

⛔ KIỂM TRƯỚC KHI PHÁT:
  [ ] Sổ của người này có chứa tên/điểm/hội thoại của người khác không?
  [ ] Lỗi hệ có bị viết thành việc của nhân viên không?
  [ ] Câu "Điểm dùng để phân việc kèm cặp…" có ở đầu mọi ST-CN không?
  [ ] Còn chỗ «agent điền» nào chưa viết không?
  [ ] Còn cờ 🔴 nào chưa gỡ không? (CỔNG 2 — id-K §7)

NHỊP PHÁT: trưởng nhóm trước → từng nhân viên bản RIÊNG → người làm nội dung.
⛔ Không phát ST-CN vào nhóm chat chung.
⛔ Không đính kèm nhiều ST-CN trong một file.
```
