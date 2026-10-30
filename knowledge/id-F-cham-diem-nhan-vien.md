# id-F · ★★ TIÊU CHÍ CHẤM ĐIỂM & PHÂN LOẠI NHÂN VIÊN TRỰC PAGE

> Sổ nhạy cảm nhất của repo. Nó tạo ra một con số gắn với **tên một con người**.
> ⛔ Chưa đọc hết §1 và §7 thì ⛔ không được chấm.

---

## 1. VÌ SAO AGENT NÀY CHẤM ĐIỂM SỐ CÒN `Agent-QC-Telesale` THÌ KHÔNG

`Agent-QC-Telesale` cố tình **không** cho điểm số, vì cuộc gọi có `K6 · giọng & ngữ điệu` — nhóm chỉ chấm được khi có audio, và bản ghi hay mất tiếng. Điểm số ở đó tạo cảm giác chính xác mà dữ liệu không có.

Chat thì khác ở ba điểm:

```
① Bằng chứng ĐẦY ĐỦ — mọi chữ đều được lưu, không có "mất tiếng".
② Mốc thời gian CHÍNH XÁC đến giây — SLA đo được, không phải cảm nhận.
③ Không có nhóm nào phụ thuộc âm thanh — mọi tiêu chí đều đọc được từ văn bản.
```

Nhưng điểm số vẫn chỉ hợp lệ khi đi kèm **bốn rào an toàn ở §7**. ⛔ Bỏ một rào là sổ này thành công cụ kỷ luật, không còn là công cụ kèm cặp.

---

## 2. CÁCH CHẤM — HAI TẦNG

```
TẦNG 1 · từng hội thoại : mỗi tiêu chí chấm ✓ / ✗ / —
TẦNG 2 · từng nhân viên : quy ra điểm 0–100 khi đủ mẫu, rồi phân loại A/B/C/D
```

| Ký hiệu | Khi nào | Tính điểm thế nào |
|---|---|---|
| `✓` **ĐẠT** | Có bằng chứng trong hội thoại | Cộng đủ điểm tiêu chí |
| `✗` **CHƯA ĐẠT** | Có bằng chứng là **không làm** hoặc **làm sai** | 0 điểm |
| `—` **KHÔNG ÁP DỤNG** | Tình huống không phát sinh (khách không hỏi giá thì không chấm tiêu chí giá) | ⛔ **Loại khỏi mẫu số**, ⛔ không tính là trượt |

### Công thức

```
Điểm một hội thoại = (tổng điểm ✓) ÷ (tổng điểm các tiêu chí KHÔNG phải "—") × 100

Điểm một nhân viên = trung bình điểm các hội thoại của người đó trong kỳ
```

⚠️ `—` **không phải** `✗`. Gộp hai cái này là cách làm cho một nhân viên trông tệ chỉ vì khách của bạn ấy không hỏi giá.

---

## 3. SÁU NHÓM TIÊU CHÍ — THANG 100

### `N1` · PHẢN HỒI & SLA — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N1.1` | Trả lời tin đầu **≤ 2 phút** | 8 | Trong khung 8h30–22h. Ngoài khung → `—` |
| `N1.2` | Không để khách **bỏ sau 1 lượt** | 6 | Khách nhắn ≥2 lượt, hoặc NV có ít nhất 1 lượt đuổi theo |
| `N1.3` | Không bỏ sót tin khách trong ca | 3 | Mọi câu hỏi của khách đều được chạm tới |
| `N1.4` | **Theo đuổi lại** khi khách im | 3 | Có ≥1 tin chủ động sau khi khách im > 30 phút |

### `N2` · KHAI THÁC TÌNH TRẠNG — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N2.1` ★ | Hỏi tình trạng **trước khi** báo giá hoặc xin số | 8 | Có ≥1 câu hỏi tình trạng trước lần nhắc giá / xin số đầu tiên |
| `N2.2` | Có ≥2 **câu hỏi mở** | 4 | Câu hỏi không trả lời được bằng có/không |
| `N2.3` | Mời **gửi ảnh / tả vùng** cụ thể | 4 | |
| `N2.4` | **Nhắc lại** đúng điều khách vừa nói | 4 | Có ít nhất 1 lần |

> ⚠️ **`N2.1` trượt là lỗi đắt nhất trong cả bộ.** Xin số trước khi biết khách cần gì biến cuộc tư vấn thành cuộc đòi số — và khách cho số xong thì không còn lý do gì để nghe tiếp. Trong dữ liệu thật, đây là tiêu chí trượt nhiều nhất.

### `N3` · TRẢ LỜI ĐÚNG & MINH BẠCH — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N3.1` | **Nêu khung giá** khi khách hỏi giá | 6 | Có nêu khoảng giá hoặc nói rõ vì sao chưa nêu được. Né hẳn = `✗` |
| `N3.2` | Thông tin **khớp bảng hiện hành** | 5 | Giá · ưu đãi · thời gian khớp văn bản đang hiệu lực |
| `N3.3` | ⛔ Không **cam kết kết quả** | 5 | Không có câu hứa chắc chắn → vi phạm là **cờ đỏ `CĐ-1`** |
| `N3.4` | ⛔ Không **nói quá về bác sĩ / chứng chỉ** | 4 | Chỉ nói thông tin có trong hồ sơ → vi phạm là **cờ đỏ `CĐ-4`** |

⚠️ **`N3.1` phải tách được hai loại trượt** (xem `id-K` §3):
- *lỗi người* — đã có giá trong tay mà vẫn né;
- *lỗi hệ* — hệ thống **chưa cấp giá** cho dịch vụ đó.

⛔ Trừ điểm nhân viên cho **lỗi hệ** là sai. Loại đó chấm `—` và đẩy lên mục "việc hệ thống" của dashboard.

### `N4` · XỬ LÝ RÀO CẢN — **15 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N4.1` | **Nhận diện đúng** mã `O` khách nêu | 5 | Câu trả lời chạm đúng điều khách sợ |
| `N4.2` | **Xử đúng tầng** | 5 | Từ chối vì **giá** thì không trả lời bằng **chất lượng**, và ngược lại |
| `N4.3` | **Giữ cửa mở** | 5 | Có câu để lại đường quay lại, kể cả khi khách từ chối |

### `N5` · XIN SỐ & CHỐT — **20 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N5.1` | Xin số có **lý do cụ thể** | 6 | Nói rõ gọi để làm gì, mất bao lâu. *"Chị cho em xin số"* trống không = `✗` |
| `N5.2` | Xin lại **lần 2 khác cách** | 4 | Lần 2 không lặp nguyên văn lần 1 |
| `N5.3` | Hỏi **khung giờ nghe máy** | 4 | ★ Đây là tín hiệu ⑤ của mức nóng (`id-D` §2) |
| `N5.4` | Mời lịch **cụ thể ngày + giờ** | 6 | *"Khi nào rảnh chị qua"* = `✗`. *"Chiều mai 3h em giữ chỗ"* = `✓` |

> ⚠️ **`N5.4` nối thẳng với doanh số.** Hai câu trên là hai hội thoại khác nhau về bản chất dù phần tư vấn phía trước giống hệt.

### `N6` · NGÔN TỪ & THÁI ĐỘ — **5 điểm**

| Mã | Tiêu chí | Điểm | Đạt khi |
|---|---|---|---|
| `N6.1` | Không dán khối dài **lệch câu hỏi** | 2 | Đoạn copy-paste phải trả lời đúng điều khách vừa hỏi |
| `N6.2` | Xưng hô, chính tả, viết tắt đọc được | 2 | |
| `N6.3` | Không gắt, không ép khách | 1 | Vi phạm nặng → **cờ đỏ `CĐ-6`** |

**Tổng: 20 + 20 + 20 + 15 + 20 + 5 = 100**

---

## 4. PHÂN LOẠI A / B / C / D

| Loại | Điểm | Nghĩa vận hành | Sổ tay nhận được |
|---|---|---|---|
| 🟢 **A** | **≥ 85** | Làm chuẩn. Dùng hội thoại của người này làm mẫu cho khối | Sổ tay **mẫu lan toả** — 1 việc nâng cấp + 2 đoạn chat mẫu để chia sẻ |
| 🔵 **B** | **70 – 84** | Vững, hụt 1–2 nhóm | Sổ tay **sửa đúng một nhóm yếu nhất** |
| 🟡 **C** | **55 – 69** | Hụt nhiều nhóm, cần kèm | Sổ tay **2 việc + kịch bản mẫu + kèm cặp theo tuần** |
| 🔴 **D** | **< 55** | Đang làm mất lead đều đặn | Sổ tay **1 việc duy nhất** + ngồi cùng trưởng nhóm đọc lại 5 hội thoại |

⚠️ **Một cờ đỏ (`§5`) trong kỳ → trần điểm của hội thoại đó là 49**, và nhân viên ⛔ **không được xếp loại A** dù điểm trung bình cao.

---

## 5. SÁU CỜ ĐỎ `CĐ-1` … `CĐ-6`

> Cờ đỏ ⛔ **không phải lỗi trừ điểm thông thường**. Mỗi cờ đỏ được **báo riêng, kèm nguyên văn câu nói và `HT-nnn`**, và phải có người xử lý đích danh.

| Mã | Cờ đỏ | Vì sao nghiêm trọng |
|---|---|---|
| `CĐ-1` | **Cam kết kết quả chắc chắn** | Claim y khoa — rủi ro pháp lý, không chỉ rủi ro bán hàng |
| `CĐ-2` | **Nêu con số bảo hành** (*trọn đời* · *10 năm*) | Ba mức đang cùng lưu hành, chưa có văn bản (`id-K` §3) |
| `CĐ-3` | **Trả lời câu bệnh nền / chống chỉ định** thay bác sĩ | `O-12` — phải bác sĩ khám |
| `CĐ-4` | **Nói quá chức danh / bằng cấp bác sĩ** chưa đối chiếu | Hai bác sĩ đang chạy ads vẫn chưa xác minh chứng chỉ |
| `CĐ-5` | **Lộ thông tin khách khác** — nhắc tên, số, ca của người khác | Vi phạm riêng tư, mất niềm tin cả page |
| `CĐ-6` | **Dìm đối thủ / gắt với khách** | Rủi ro thương hiệu, có thể bị chụp màn hình |

---

## 6. ĐIỀU KIỆN ĐỦ MẪU

| Số HT của một nhân viên trong kỳ | Agent được làm gì |
|---|---|
| **< 5** | ⛔ Không chấm. Ghi `chưa đủ mẫu` |
| **5 – 9** | Chấm từng hội thoại, ⛔ **không cho điểm tổng, không phân loại** |
| **≥ 10** | ✅ Cho điểm tổng + phân loại A/B/C/D |
| **≥ 10 và liên tục 2 kỳ** | ✅ Được vẽ xu hướng, được so với kỳ trước |

⚠️ Nhân viên có **ca trực lệch giờ** (ca đêm, ca cuối tuần) thì tiêu chí `N1.1` phải tính theo **khung giờ của ca đó**, ⛔ không dùng khung chung 8h30–22h.

---

## 7. ★ BỐN RÀO AN TOÀN — ⛔ BỎ MỘT CÁI LÀ SỔ NÀY VÔ HIỆU

```
① ĐIỂM ĐỂ KÈM CẶP, KHÔNG ĐỂ KỶ LUẬT.
   Mọi bảng điểm phải mang đúng câu này ở chân bảng:
   "Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai."

② MỖI ĐIỂM TRỪ PHẢI CÓ BẰNG CHỨNG.
   Một ô ✗ không gắn được HT-nnn + nguyên văn câu → đổi thành "—".
   ⛔ Không có bằng chứng thì không có điểm trừ.

③ LỖI HỆ KHÔNG TRỪ ĐIỂM NGƯỜI.
   Thiếu bảng giá · page không có dịch vụ · hệ thống ngoài giờ · công cụ lỗi
   → chấm "—" và đẩy lên mục "việc hệ thống", ⛔ không trừ nhân viên.

④ KHÔNG XẾP HẠNG CÔNG KHAI TOÀN KHỐI.
   Dashboard hiện phân bố A/B/C/D và chỉ số cả đội.
   Tên + điểm cá nhân CHỈ xuất hiện trong sổ tay RIÊNG của người đó
   và bản của trưởng nhóm. ⛔ Không có bảng xếp hạng dán lên màn hình chung.
```

⚠️ Rào ③ là rào hay bị quên nhất. Trong dữ liệu thật, một phần lớn ô *"né giá"* là **lỗi hệ** — hệ thống chưa cấp giá dịch vụ ngoài mắt. Trừ điểm nhân viên vì chuyện đó là chấm sai người.

---

## 8. ĐẦU RA CHUẨN CỦA BƯỚC B6

```
① PHÂN BỐ      : số người loại A/B/C/D + số người chưa đủ mẫu
② CHỈ SỐ ĐỘI   : % đạt từng nhóm N1…N6 — đây là thứ đưa lên dashboard
③ BẢNG CÁ NHÂN : tên · số HT · điểm · loại · nhóm yếu nhất · nhóm mạnh nhất
                 (⛔ chỉ vào sổ tay riêng + bản trưởng nhóm)
④ CỜ ĐỎ        : từng cờ · ai · HT-nnn · nguyên văn · người xử lý
⑤ VIỆC HỆ THỐNG: các ô "—" do lỗi hệ, gom theo nguyên nhân
⑥ TIÊU CHÍ YẾU NHẤT CỦA KHỐI : 3 tiêu chí trượt nhiều nhất → thành nội dung đào tạo kỳ sau
```

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Mọi `✗` đều có `HT-nnn` + nguyên văn câu chưa?
- [ ] Có ô nào là **lỗi hệ** mà bị chấm `✗` không?
- [ ] `—` có bị cộng vào mẫu số không?
- [ ] Người dưới 10 HT có bị phân loại không?
- [ ] Có bảng xếp hạng cá nhân nào lọt ra ngoài sổ tay riêng không?
- [ ] Câu *"Điểm dùng để kèm cặp…"* có ở chân mọi bảng điểm không?
- [ ] Cờ đỏ có được báo riêng kèm người xử lý đích danh không?
