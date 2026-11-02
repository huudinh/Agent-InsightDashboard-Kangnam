# KF-60 · Lead Scoring hội thoại Inbox Facebook (Kangnam / HCI) — **v1.1**

**Trạng thái: ÁP DỤNG TẠM THỜI từ 02/11/2026.** v1.0 đã được anh UY duyệt; v1.1 **đổi 9 điểm** sau khi đối chiếu với một kỳ dữ liệu thật — ⚠ **ba điểm cần duyệt lại** (đánh dấu `⚠ CHỜ DUYỆT` ở §0).
**Thay thế** `KF-60 … v1.0`. Mọi thay đổi tiếp theo ghi vào tab `9. Nhật ký điều chỉnh` của file Driver.
**File Driver đi kèm:** `KF-60_Driver_Lead_Scoring_Inbox_v1.0.xlsx` — ⚠ các ô nền vàng phải cập nhật theo §7 và §8 bản này.

**Bằng chứng dùng để sửa:** kỳ **24–29/10/2026**, **494 hội thoại** đã phân tích và truy ngược được từng `HT-nnn`
(`dashboard/data/24-29-10.json` · nguồn `KNB_1_toan_bo_24-10_den_29-10.txt` · **line Da**, Caresoft/Messenger).
⚠ Kỳ này **chỉ có line Da** — mọi kết luận về hệ số theo BL vẫn chưa có dữ liệu PTTM để kiểm (§8, §12).

---

## 0. ĐỔI GÌ Ở v1.1 — VÀ BẰNG CHỨNG NÀO BUỘC ĐỔI

| # | v1.0 | v1.1 | Vì sao đổi |
|---|---|---|---|
| ① | Ngưỡng **HOT ≥65 · WARM 35–64** | **HOT ≥50 · WARM 25–49** ⚠ CHỜ DUYỆT | Chấm thử theo bảng điểm v1.0, khách **đã cho số và đang hỏi điều kiện** chỉ đạt **≈41–51 điểm** → rơi vào WARM. Ngưỡng 65 đẩy chính nhóm phải gọi xuống hàng chờ (§7) |
| ② | Rào cản ghi chữ tự do (`gia`, `so_bien_chung`) | **Bắt buộc `O-01…O-12` + `O-00`** | Danh sách đóng của `id-D` §1, dùng chéo ở 30+ chỗ và ở 2 agent khác. v1.0 thiếu hẳn **O-08** (13.2% mẫu) và **O-06** (3.8%) |
| ③ | `compliance_issue` ghi chữ tự do | **`CĐ-1…CĐ-6`** của `id-F` §5 | Để cờ pháp chế đi đúng đường xử lý đã có, không sinh danh mục thứ hai |
| ④ | `agent_flags` tự định nghĩa | **Trỏ về `N1…N6`** của `id-F`, ⛔ không chấm lại nhân viên | v1.0 đang dựng bộ chấm nhân viên thứ hai song song với bộ 22 tiêu chí đang chạy |
| ⑤ | Hệ số BL **1,0 / 0,8 / 0,7 / 0,5** | **Hệ số giá trị đơn 1 / 2 / 3** của `id-G` §3 ⚠ CHỜ DUYỆT | Hai thang hệ số khác nhau cho cùng một lead = hàng chờ Sale và ma trận ưu tiên xếp khác nhau. Và: kỳ 24–29/10 **toàn bộ là line Da** → mọi lead bị nhân 0,5–0,7, trong hàng chờ trộn thì **không bao giờ được gọi trước** |
| ⑥ | `N1 Chưa tương tác` = «KH ≤1 tin tự viết» | **Tách N1a / N1b** | 45.3% hội thoại (224/494) bỏ sau 1 lượt, nhưng **43.9% rơi là do câu trả lời của trực page** — khách *đã được trả lời rồi mới im*. Nhóm đó ⛔ không phải N1, là **LEAD có lỗi nội dung/câu trả lời** |
| ⑦ | Không nói gì về bộ 5 tín hiệu đang chạy | **§7.3 bảng đối chiếu + luật khớp** | `id-D` §2 đang phân loại HOT/WARM/COLD bằng 5 tín hiệu và số đó đã lên dashboard. Hai định nghĩa HOT cùng tên khác ruột là lỗi nặng nhất của v1.0 |
| ⑧ | Tuần 1: xuất 300 HT mới, 2 trưởng nhóm gắn nhãn | **Dùng 494 HT đã có làm tập vàng đầu tiên**, chỉ gắn nhãn tay **120 HT phân tầng** | 494 HT đã phân loại, đã truy ngược `HT-nnn`, đã có nhãn rào cản và nguyên nhân rơi. Gắn nhãn lại từ đầu là làm lại việc đã làm |
| ⑨ | §6 theo dõi «% `HOT_CHUA_SO` theo từng nhân viên» | **Chỉ vào sổ tay riêng của người đó** (§13) | Vi phạm rào ④ của `id-F` §7: ⛔ không bảng xếp hạng cá nhân ngoài sổ tay riêng |

---

## 1. CHỖ ĐỨNG CỦA BỘ NÀY — RANH GIỚI VỚI BA SỔ ĐANG CHẠY

```
id-D §2  → PHÂN LOẠI hội thoại  (5 tín hiệu)   → số lên dashboard, so được giữa các kỳ
KF-60    → XẾP HÀNG GỌI trong từng loại        → Sale gọi ai trước
id-F     → CHẤM NHÂN VIÊN       (22 tiêu chí)  → sổ tay kèm cặp
id-G §3  → XẾP ƯU TIÊN NỘI DUNG (hệ số 1/2/3)  → Marketing làm gì kỳ sau
```

★ **KF-60 ⛔ không thay `id-D`.** Nhãn HOT/WARM/COLD báo ra ngoài **vẫn là nhãn 5 tín hiệu**. Điểm 0–100 của bộ này là **thứ tự gọi bên trong một nhãn**, cộng một số luật ghi đè được phép đổi nhãn (§6).
⛔ Hai nơi cùng gọi một hội thoại là HOT theo hai cách khác nhau thì không ai còn tin con số nào.

---

## 2. ★ BA PHÁT HIỆN PHẢI ĐỌC TRƯỚC KHI CHẤM

### ① Hai tín hiệu mà cả bảng điểm dựa vào thì gần như **không bao giờ xuất hiện**

| Tín hiệu (`id-D` §2) | Số HT / 494 | % |
|---|---|---|
| ① Nêu dịch vụ cụ thể | 261 | 52.8% |
| ④ Hỏi điều kiện thực hiện | 100 | 20.2% |
| ③ Cho SĐT | 96 | 19.4% |
| ② **Mốc thời gian ≤14 ngày** | **9** | **1.8%** |
| ⑤ **Đồng ý khung giờ gọi** | **1** | **0.2%** |

⛔ **`B1` (thời điểm, 12 điểm) · `C2` (lịch hẹn, 8 điểm) · `C3` (chuẩn bị đến, 10 điểm) — 30 trên 100 điểm — treo vào hai tín hiệu chỉ xuất hiện 1,8% và 0,2%.** Kết quả: HOT = **3/494 = 0.6%**, chốt lịch 23/494 = 4.7%.

★ Nghĩa vận hành: **bộ chấm chưa thể sinh ra khách Hot cho tới khi trực page bắt đầu hỏi hai câu** — *"chị dự định làm khoảng khi nào"* và *"giờ nào chị nghe máy được"*. Đây là việc của `N5.3` (`id-F`), ⛔ không phải việc của bộ chấm. Đặt SLA 15 phút cho một hàng chờ 3 người là đặt sai chỗ.

### ② Rào cản lớn thứ ba của khách **không có trong bảng của v1.0**

| Mã `O` | Tên | Số HT | % mẫu | v1.0 có? |
|---|---|---|---|---|
| `O-00` | **Không xếp được** | 140 | **28.3%** | — |
| `O-01` | Giá & phát sinh | 134 | 27.1% | ✓ `gia` |
| `O-09` | Thời gian · khoảng cách | 70 | 14.2% | ✓ `khoang_cach` |
| `O-08` | **Không biết mình cần gì** | **65** | **13.2%** | ⛔ **thiếu** |
| `O-06` | **Nghi địa chỉ, uy tín** | **19** | **3.8%** | ⛔ **thiếu** |
| `O-03` | Sợ lộ sửa | 13 | 2.6% | ✓ |
| `O-12` | Bệnh nền | 12 | 2.4% | ⛔ thiếu |
| `O-04` · `O-07` | Đau/nghỉ · Bảo hành | 2 · 2 | 0.4% · 0.4% | ✓ · ⛔ |
| `O-02` · `O-10` | Kết quả xấu · So đối thủ | 1 · 1 | 0.2% · 0.2% | ✓ · ⛔ |
| `O-05` · `O-11` | Nghi bác sĩ · Người nhà | 0 · 0 | 0% | ✓ · ✓ |
| *(chưa nêu)* | Khách chưa nêu phản đối nào | 110 | 22.3% | — |

⚠️ **`O-00` = 28.3%, vượt xa ngưỡng 10% của `id-D` §1.** Theo luật sổ đó: **báo lại để bổ sung danh sách**, ⛔ agent không tự thêm mã. Cho tới khi có mã mới, `O-00` phải được đếm riêng và ⛔ không gộp vào `O-01`.
⚠️ `O-08` = *"em gửi ảnh bác xem"* — khách **không biết mình cần gì**. Đây là nhóm Warm dễ nuôi nhất và v1.0 không có chỗ để ghi.

### ③ Khách rơi **sau khi đã được trả lời**, không phải vì không ai trả lời

| | Số HT | % |
|---|---|---|
| Rơi do **trực page** | 217 | 43.9% |
| Khách tự dừng | 174 | 35.2% |
| **Không rơi** (có SĐT hoặc chốt lịch) | 100 | 20.2% |
| Hệ thống | 3 | 0.6% |

Kèm theo: **bỏ sau 1 lượt 45.3%** (224/494) · trả lời lượt đầu ≤2′ chỉ **35.4%** · **67% hội thoại dừng ở nấc A1** (329/494, chỉ 1 HT lên A2).
→ Luồng `N1` của v1.0 phải tách (§3). Và SLA gọi Hot 15 phút chỉ có nghĩa **sau khi** sửa được hai số trên.

---

## 3. Bước 0 — PHÂN LUỒNG (⛔ không chấm nhiệt độ)

| Mã | Nhãn | Dấu hiệu | Chuyển cho | SLA |
|---|---|---|---|---|
| `N1a` | **Chưa tương tác thật** | Chỉ có tin tự động từ quảng cáo, hoặc ≤1 tin tự viết **và chưa được trả lời** | Nhân viên page / bot mở lời lại | 2–4h |
| `N1b` | ★ **Đã trả lời rồi khách im** | KH ≤1–2 tin tự viết nhưng **đã nhận câu trả lời** rồi dừng | ⛔ **Vẫn chấm như LEAD.** Gắn `nguyen_nhan_roi="trực page"` → `id-D` §3 + `id-F` | theo nhãn nhiệt |
| `N2` | Không phải lead | Spam, chào hàng, đối tác, tuyển dụng, báo chí | Admin page | 24h |
| `N3` | KH cũ – CSKH | Tái khám, hậu phẫu, bảo hành, lịch hẹn đã có | CSKH chi nhánh | 4h |
| `N4` | **Cảnh báo đỏ** | Khiếu nại, nghi biến chứng, đòi hoàn tiền, dọa đánh giá xấu/báo chí/kiện | Quản lý chi nhánh + quy trình khủng hoảng **+ đầu mối pháp chế** (`id-K`) | **≤30 phút** |
| `N5` | Chưa đủ điều kiện | Chưa đủ tuổi với dịch vụ PTTM, hoặc KH tự nói tình trạng không phù hợp (mang thai…) | Tư vấn an toàn, ⛔ không bán | 24h |

★ **`N1b` là luồng mới và là luồng đông nhất.** Gộp nó vào `N1a` làm hai việc sai cùng lúc: bỏ qua một lead thật, và che mất lỗi câu trả lời của trực page.
> KH cũ hỏi **dịch vụ mới** vẫn chấm như lead, kèm cờ `KH_cu_cross_sell` — nhóm LTV cao nhất.

---

## 4. Bước 1 — BẢNG ĐIỂM CỘNG (tổng tối đa 100)

Thang điểm giữ nguyên v1.0 ở ba nhóm A, B, D. **Nhóm C sửa một ô** (`C3`).

**A. Nhu cầu & mức phù hợp — tối đa 25**

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `A1` | Xác định dịch vụ ★ = tín hiệu ① | Chung chung 0 · Nhóm dịch vụ 4 · Dịch vụ cụ thể 8 |
| `A2` | Mô tả tình trạng của chính mình | Không 0 · Có mô tả 4 · **Gửi ảnh/video** 8 |
| `A3` | Khả năng đến cơ sở | Không rõ 0 · Ở gần CN / Việt kiều có ngày về 3 · Nói rõ sẽ đến, đã biết CN 5 |
| `A4` | Hỏi cho ai | Không rõ 0 · Cho chính mình / người thân cụ thể 4 |

**B. Ý định mua — tối đa 35**

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `B1` | Thời điểm dự kiến ★ = tín hiệu ② — **1.8% mẫu** | Chưa rõ 0 · 1–3 tháng 5 · ≤1 tháng 9 · ≤2 tuần hoặc gắn sự kiện 12 |
| `B2` | Hỏi giá có ngữ cảnh | Không hỏi 0 · Chỉ *"giá bao nhiêu"* 2 · Hỏi giá cho tình trạng của mình 5 · Hỏi trả góp/cọc/ưu đãi còn hạn 8 |
| `B3` | Hỏi thông tin để ra quyết định ★ = tín hiệu ④ | Không 0 · 1 chủ đề 4 · ≥2 chủ đề 8 |
| `B4` | Đang so sánh / đã tư vấn nơi khác (= `O-10`) | Không 0 · Có 7 |

**C. Cam kết hành động — tối đa 25**

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `C1` | SĐT/Zalo ★ = tín hiệu ③ | Chưa có 0 · Để lại SĐT/Zalo hợp lệ 12 |
| `C2` | Lịch hẹn | Không 0 · Hỏi lịch trống 4 · Đồng ý ngày/giờ cụ thể 8 |
| `C3` | **Chuẩn bị đến** — ⚠ **sửa ở v1.1** | Không 0 · **Hỏi địa chỉ/đường đi/gửi xe 2** · Hỏi cách chuyển cọc 5 |

⚠️ **Vì sao hạ `C3` hỏi-địa-chỉ từ 5 xuống 2:** trong kỳ này **70 HT mang `O-09`** và hỏi địa chỉ là câu mở đầu rất thường gặp của khách ở tỉnh — nhưng nhóm CD6 *(khách tỉnh)* chỉ **9.4% cho SĐT** và **4/64 đạt WARM**. Hỏi địa chỉ ⛔ không phải tín hiệu cam kết; hỏi **cách chuyển cọc** thì đúng là. Để cùng 5 điểm làm cả nhóm CD6 nhảy hạng sai.

**D. Mức tương tác — tối đa 15** *(giữ nguyên v1.0)*

| Mã | Tiêu chí | Mức → Điểm |
|---|---|---|
| `D1` | Số tin KH tự viết | 1–2 tin 0 · 3–5 tin 3 · 6–10 tin 5 · >10 tin 6 |
| `D2` | Vẫn hỏi/trả lời tiếp **sau khi đã biết giá** | Không 0 · Có 5 |
| `D3` | Tốc độ KH trả lời (trung vị) | >1 giờ 0 · <1 giờ 2 · <10 phút 4 |

---

## 5. Bước 2 — TÍN HIỆU ÂM (tối đa −30) · giữ nguyên v1.0

| Mã | Tín hiệu | Điểm | Ghi chú v1.1 |
|---|---|---|---|
| `E1` | Biết giá rồi im lặng ≥48h | −10 | ⚠ phải ghi kèm `nguyen_nhan_roi` — xem cảnh báo dưới |
| `E2` | Phản đối giá / *"để em tính"* rồi **không** tương tác tiếp | −5 | = `O-01` |
| `E3` | Từ chối cho số sau ≥2 lần được xin | −5 | ⚠ chỉ trừ khi `N5.1` của `id-F` đạt |
| `E4` | *"Hỏi cho biết"*, hỏi hộ không rõ ai | −5 | |
| `E5` | Ở xa, không có kế hoạch đến | −5 | = `O-09`, ⛔ không trùng `C3` |

⚠️ **`E1` và `E3` là hai ô dễ chấm sai người nhất.** 43.9% hội thoại rơi vì **câu trả lời của trực page**, và `N5.1` *(xin số có lý do cụ thể)* là tiêu chí trượt nhiều. Khách im sau một câu trả lời không đóng được nỗi sợ ⛔ **không phải khách nguội** — đó là lead còn nóng bị trả lời sai.
→ Luật: **trừ `E1`/`E3` chỉ khi hội thoại có `nguyen_nhan_roi = "khách tự dừng"`.** Nếu là `"trực page"` thì ⛔ không trừ, và đẩy sang `id-F`.

---

## 6. Bước 3 — LUẬT GHI ĐÈ

| # | Luật | Thành |
|---|---|---|
| ① | Có SĐT **và** (thời điểm ≤1 tháng **hoặc** đồng ý lịch cụ thể) | **HOT** |
| ② | Hỏi **cách chuyển cọc** | **HOT** |
| ③ | ★ **mới v1.1** — Có SĐT **và** (dịch vụ cụ thể **hoặc** ≥2 chủ đề quyết định) | **HOT** |
| ④ | Khớp luật Hot nhưng **chưa có SĐT/Zalo** | nhãn **`HOT_CHUA_SO`** |
| ⑤ | **sửa v1.1** — WARM trở lên mà **chưa có SĐT** | cũng vào hàng **`HOT_CHUA_SO`** |
| ⑥ | Có SĐT nhưng **tổng nhóm B = 0** (để số vì form/khuyến mãi) | trần **WARM** |

★ **Luật ③ là cái làm hàng chờ Sale tồn tại.** Không có nó, HOT = 3/494 và cả bộ chấm không sinh ra việc gì cho Sale.
★ **Luật ⑤ nối thẳng với ô đỏ của dashboard.** `id-D` §2: ô nguy hiểm nhất là **HOT/WARM chưa có SĐT** — kỳ này **43 HT**, trong đó HOT 0 và **WARM 43**. Nhãn `HOT_CHUA_SO` của v1.0 chỉ phủ HOT nên bỏ sót đúng 43 lead đang rơi.

---

## 7. Bước 4 — HỆ SỐ THỜI GIAN · NGƯỠNG MỚI · ĐỐI CHIẾU VỚI `id-D`

### 7.1 Hệ số thời gian *(giữ nguyên v1.0)*

**Nhiệt độ hiện tại** = Điểm gốc × hệ số, tính từ **tin cuối của KH**:

| Từ tin cuối KH | ≤24h | 1–3 ngày | 4–7 ngày | >7 ngày |
|---|---|---|---|---|
| Hệ số | 1,0 | 0,85 | 0,7 | 0,5 |

⛔ Không áp hệ số nếu KH đã có lịch hẹn trong tương lai. KH nhắn tin mới thì chấm lại.

### 7.2 Ngưỡng — ⚠ CHỜ DUYỆT

| Phân loại | v1.0 | **v1.1** |
|---|---|---|
| **HOT** | ≥65 | **≥50** |
| **WARM** | 35–64 | **25–49** |
| **COLD** | <35 | **<25** |

**Chấm thử theo đúng bảng §4 trên ba loại hội thoại có thật trong kỳ:**

```
① Khách ĐÃ CHO SỐ, hỏi điều kiện, chưa nêu mốc thời gian  (nhóm 96 HT có SĐT)
   A: 8+4+0+4 = 16 | B: 0+5+8+0 = 13 | C: 12+0+2 = 14 | D: 3+0+2 = 5   → 48
   theo v1.0 → WARM.  ⛔ Đây chính là nhóm Sale phải gọi.

② Khách CHƯA CHO SỐ nhưng tả tình trạng, gửi ảnh, hỏi 2 chủ đề  (nhóm O-08 · 65 HT)
   A: 8+8+0+4 = 20 | B: 0+5+8+0 = 13 | C: 0 | D: 3+0+2 = 5             → 38
   theo v1.0 → WARM, lẫn chung với nhóm ③.

③ Khách hỏi giá rồi im  (nhóm O-01 · 134 HT, phần lớn bỏ sau 1 lượt)
   A: 4+0+0+0 = 4 | B: 0+2+0+0 = 2 | C: 0 | D: 0                        → 6
   → COLD ở cả hai bản.
```

★ Ngưỡng 65 của v1.0 **không có hội thoại nào trong kỳ đạt tới** ngoài 23 ca đã chốt lịch. Ngưỡng 50 đưa nhóm ① lên HOT, giữ nhóm ② ở WARM — đúng thứ tự việc.
⚠️ **Ba con số 50 / 25 / hệ số `C3`=2 là suy ra từ MỘT kỳ, MỘT line (Da), và ⛔ chưa đối chiếu với booking thật** — chưa có dòng CRM về. Chúng là **ngưỡng tạm**, phải thay bằng số đo từ booking ở tuần 5–6 (§12). ⛔ Đừng trích ba con số này ra khỏi ngữ cảnh đó.

### 7.3 ★ ĐỐI CHIẾU VỚI 5 TÍN HIỆU — LUẬT KHỚP

Nhãn báo ra ngoài **là nhãn `id-D`**. Điểm KF-60 là thứ tự gọi bên trong nhãn.

| Nhãn `id-D` (5 tín hiệu) | Số HT kỳ này | KF-60 làm gì |
|---|---|---|
| 🔴 HOT 4–5 tín hiệu | 3 | Gọi trước, xếp trong nhóm theo điểm ưu tiên §8 |
| 🟠 WARM 2–3 tín hiệu | 117 | ★ **Điểm KF-60 chia đôi nhóm này**: ≥50 → hàng gọi; 25–49 → chuỗi chăm sóc |
| ⚪ COLD 0–1 tín hiệu | 374 | Remarketing; ⛔ chỉ kéo lên khi khớp luật ghi đè §6 |

**Luật khớp — kiểm mỗi kỳ:**
```
① Hội thoại KF-60 ≥50 mà id-D xếp COLD  → đưa vào danh sách SOÁT TAY.
   Quá 5% mẫu  → ⛔ một trong hai bộ đang chấm sai, DỪNG, không phát hàng chờ.
② Hội thoại id-D xếp HOT mà KF-60 <25    → luôn luôn soát tay, không có ngoại lệ.
③ Mọi dòng trong hai danh sách trên phải gắn HT-nnn.
```
⛔ **Luật tối thượng của `id-D` áp cho cả bộ này: một hội thoại không truy ngược được về `HT-nnn` là một hội thoại bịa.**

---

## 8. Bước 5 — ĐIỂM ƯU TIÊN GỌI

```
Ưu tiên = Nhiệt độ × hệ số giá trị đơn
```
Riêng khách Hot, nhiệt độ tính **tối thiểu bằng ngưỡng Hot**. Điểm này ⛔ không đổi phân loại.

**Hệ số giá trị đơn — ⚠ CHỜ DUYỆT · lấy đúng thang `id-G` §3:**

| Bậc | Giá trị đơn ước tính | Hệ số |
|---|---|---|
| Thấp | < 5 triệu | **1** |
| Trung | 5 – 15 triệu | **2** |
| Cao | ≥ 15 triệu | **3** |
| ⚠ Chưa có giá, hoặc khách chưa nêu dịch vụ | | **1** ⚠ |

⚠️ Hệ số đi theo **dịch vụ khách hỏi**, ⛔ không theo BL và ⛔ không theo chân dung — **trừ** khi bản phác họa chân dung của kỳ đã khai `he_so_gia_tri` (`id-C` §2); khi có, số đó thắng, vì là kết luận của người đã đọc cả tệp. Kỳ 24–29/10 đã khai: CD1 `2` · CD3 `2` · CD4 `2` · CD2/CD5/CD6/CD7/CD0 `1`.

**Vì sao bỏ thang BL 1,0–0,5 của v1.0:**
```
① Kỳ 24–29/10 toàn bộ là line Da → mọi lead bị nhân 0,5–0,7.
   Trong một hàng chờ trộn với PTTM, không lead nào của line này được gọi trước.
② Giá trị đơn đi theo DỊCH VỤ, không theo BL: một ca implant toàn hàm
   và một ca tẩy trắng cùng nằm trong "Nha khoa 0,8".
③ Repo đã có một thang hệ số đang chạy. Hai thang = hai thứ tự ưu tiên.
```
⚠️ Hệ số **ước từ bảng giá chuẩn, không phải doanh thu thật** → mọi ô dùng hệ số gắn `⚠`. Khi hệ thống cấp bảng giá hiện hành (`id-K` §3) thì thay số thật và ghi vào `doc/CHANGELOG.md`.
★ Beauty & Spa là cửa vào hệ sinh thái: **khách Hot của B&S vẫn gọi trong SLA**, chỉ xếp sau khi trùng giờ.

---

## 9. ĐẦU RA AI CHO MỖI HỘI THOẠI

- **`ht_id`** — ⛔ bắt buộc, dạng `HT-nnn`. Không có thì bỏ hội thoại khỏi mẫu.
- **Dịch vụ quan tâm** + cờ `KH_cu_cross_sell`.
- **Rào cản**: `O-01…O-12`, không xếp được thì `O-00` **và đếm riêng** — ⛔ đừng tự thêm mã.
- **Nguyên nhân rơi**: ⛔ **đúng một** trong `nội dung · trực page · hệ thống · khách tự dừng · không rơi` (`id-D` §3).
- **Bằng chứng**: 1–3 câu chat ngắn, **đã ẩn danh**, cho mỗi tiêu chí có điểm.
- **Câu tiếp theo đề xuất** (1–2 câu).
- **Cờ chất lượng tư vấn**: ⛔ **không chấm lại nhân viên** — chỉ ghi dữ kiện thô và trỏ về mã `N` của `id-F`.
- **Cờ pháp chế**: `CĐ-1…CĐ-6`. ⛔ `O-07` (bảo hành) và `O-12` (bệnh nền) — agent ⛔ không tự trả lời.

### Mẫu JSON v1.1

```json
{
  "ht_id": "HT-001",
  "conversation_id": "",
  "page_id": "",
  "ad_id": "",
  "route": "LEAD | N1a | N1b | N2 | N3 | N4 | N5",
  "service": {"bl": "Da", "service": "Trị nám", "he_so_gia_tri": 2},
  "cd": "CD3",
  "nac": "A1",
  "cross_sell_existing_customer": false,
  "scores": {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0},
  "criteria_hits": [
    {"code": "B1", "level": "≤2 tuần / gắn sự kiện", "points": 12,
     "evidence": "tháng 12 em cưới", "ht_id": "HT-001"}
  ],
  "base_score": 0,
  "override": "NONE | HOT_RULE | HOT_SO_DV | HOT_CHUA_SO | CAP_WARM",
  "hours_since_last_customer_msg": 0,
  "has_future_appointment": false,
  "temperature": 0,
  "class_kf60": "HOT | WARM | COLD",
  "tin_hieu": {"1_dich_vu": false, "2_thoi_gian": false, "3_sdt": false,
               "4_dieu_kien": false, "5_khung_gio": false},
  "class_id_d": "HOT | WARM | COLD",
  "lech_nhan": false,
  "has_phone": false,
  "priority": 0,
  "ma_o": ["O-01", "O-09"],
  "ma_o_00": false,
  "nguyen_nhan_roi": "trực page",
  "next_best_message": "",
  "du_kien_truc_page": {"da_xin_so": true, "phan_hoi_dau_phut": 3,
                        "tra_loi_cau_hoi_gia": true, "tro_ve": ["N5.1", "N3.1"]},
  "co_phap_che": [],
  "confidence": 0.0
}
```

⚠️ `class_id_d` và `class_kf60` **phải cùng có mặt**, và `lech_nhan = true` khi chúng lệch nhau — đó là đầu vào của luật khớp §7.3.

### Prompt lõi cho AI

> Bạn là chuyên viên chấm điểm lead của hệ thống y tế – thẩm mỹ Kangnam/HCI. Đọc toàn bộ hội thoại Messenger giữa KHÁCH và NHÂN VIÊN.
>
> Chỉ chấm dựa trên lời hoặc hành động của KHÁCH; lời nhân viên chỉ dùng làm ngữ cảnh và để ghi `du_kien_truc_page`.
>
> Làm đúng thứ tự:
> 0. Phân luồng `N1a` · `N1b` · `N2`–`N5` hoặc `LEAD`. **Khách đã nhận câu trả lời rồi mới im là `N1b`, vẫn chấm như LEAD.**
> 1. Chấm A, B, C, D theo bảng tiêu chí; mỗi tiêu chí chọn **đúng một** mức.
> 2. Trừ điểm nhóm E — ⛔ chỉ trừ `E1`/`E3` khi `nguyen_nhan_roi = "khách tự dừng"`.
> 3. Áp 6 luật ghi đè.
> 4. Nhân hệ số thời gian → `class_kf60`. Đồng thời chấm 5 tín hiệu `id-D` → `class_id_d`. Lệch nhau thì `lech_nhan = true`.
> 5. Tính điểm ưu tiên bằng hệ số giá trị đơn 1/2/3.
>
> Gán rào cản bằng `O-01…O-12`; không xếp được thì `O-00`, ⛔ **tuyệt đối không tự đặt mã mới**.
> Gán **đúng một** nguyên nhân rơi.
> Với mỗi tiêu chí có điểm, trích câu chat làm bằng chứng kèm `HT-nnn`; **không có bằng chứng thì cho 0**.
> ⛔ Không suy diễn SĐT: chỉ tính khi thấy dãy số hợp lệ hoặc số/tên Zalo.
> ⛔ Không ghi lại thông tin sức khỏe chi tiết ngoài dịch vụ quan tâm; ⛔ bỏ hết tên, SĐT, ảnh của khách trong phần bằng chứng.
> ⛔ Không tự trả lời `O-07` (bảo hành) và `O-12` (bệnh nền).
> Trả về đúng JSON mẫu, không thêm chữ.

(Đính kèm vào prompt bảng tiêu chí mới nhất xuất từ tab `2. Tiêu chí` của file Driver, **và** bảng 12 mã `O` của `id-D` §1.)

---

## 10. ACTION PLAN THEO PHÂN LOẠI (SLA)

| Nhãn | Ai xử lý | SLA | Việc cần làm |
|---|---|---|---|
| `N4` Cảnh báo đỏ | Quản lý CN + CSKH + pháp chế | **≤30 phút** | Quy trình khủng hoảng, ⛔ không tranh luận trên inbox |
| **HOT** | Sale senior theo BL | Gọi ≤15 phút (giờ làm việc); ngoài giờ thì trước 9h sáng hôm sau | Chốt lịch tư vấn bác sĩ / đặt cọc, gửi case thật **cùng nhóm tình trạng** |
| **`HOT_CHUA_SO`** ★ | Nhân viên trực page | ≤15 phút | Xin số theo kịch bản `N5.1`, gắn với giá trị cho khách (*"bác sĩ xem ảnh và gọi tư vấn riêng"*) |
| **WARM** ≥50 | Sale/CSKH online | 24h | Gọi sau nhóm HOT |
| **WARM** 25–49 | Sale/CSKH online | 24–72h | Chuỗi chăm sóc Zalo **theo mã `O`**, mời tư vấn bác sĩ online |
| **COLD** | Marketing (CDP) | Tự động | Remarketing, chuỗi nội dung TOF/MOF 7–14 ngày |
| `N1a` | Bot/nhân viên page | 2–4h | Mở lời lại 1 lần; không phản hồi thì coi như Cold |
| `N1b` ★ | Trực page + Marketing | theo nhãn nhiệt | Chấm như lead **và** ghi lỗi câu trả lời về `id-F` / `id-D` §7 |

### ★ THỨ TỰ SỬA — ⛔ ĐỪNG ĐẢO

```
① Trực page hỏi MỐC THỜI GIAN và KHUNG GIỜ GỌI   (tín hiệu ② 1.8% · ⑤ 0.2%)
   → không có bước này thì hàng chờ HOT vẫn chỉ vài người, SLA 15 phút vô nghĩa.
② Trả lời lượt đầu ≤2 phút                        (đang 35.4%)
③ Không bỏ khách sau 1 lượt                       (đang 45.3% bị bỏ)
④ Rồi mới siết SLA gọi Hot.
```

**Gắn với bộ chấm chiến dịch (KF-49/50):**
- Lấy `ad_id` từ tham chiếu hội thoại click-to-Messenger, nối về chiến dịch.
- Theo dõi **% Hot+Warm/tổng inbox** và **% Hot** theo chiến dịch.
- ⚠ Đề xuất **chờ duyệt**: thay một phần trọng số Lead→Booking bằng % Hot — ⛔ chỉ sau khi luật khớp §7.3 chạy sạch một kỳ.

---

## 11. LỘ TRÌNH TRIỂN KHAI 6 TUẦN

| Tuần | Việc | Đầu ra |
|---|---|---|
| 1 | ★ **Dùng 494 HT của 24–29/10 làm tập vàng đầu tiên** — đã phân loại, đã truy ngược `HT-nnn`. 2 trưởng nhóm Sale gắn nhãn tay **độc lập** trên **120 HT phân tầng** (theo CD và theo nhãn nhiệt). ⚠ Tập này **chỉ có line Da** → xin thêm **1 kỳ PTTM** trước khi kết luận gì về hệ số | Tập vàng 120 HT + 1 kỳ PTTM đang chờ |
| 2 | AI chấm cùng 120 HT, so với nhãn người | Khớp ≥80%; **độ chính xác Hot ≥85%**. Chạy luật khớp §7.3 — lệch >5% thì sửa tiêu chí trước khi đi tiếp |
| 3–4 | Chạy song song tại 1–2 page thí điểm **đã nối CRM** | Tỷ lệ booking theo CRM của nhóm Hot và nhóm Warm |
| 5–6 | ★ **Thay ba ngưỡng tạm ở §7.2 bằng số đo từ booking thật** | Bộ v1.2 + SOP nhân rộng |

**Chỉ số theo dõi**

| Chỉ số | Mốc kỳ 24–29/10 |
|---|---|
| Booking theo nhóm Hot / Warm / Cold — phải **giảm dần rõ rệt** | chưa có dòng CRM |
| Tín hiệu ② mốc thời gian | 1.8% → mục tiêu kỳ sau |
| Tín hiệu ⑤ khung giờ gọi | **0.2%** → mục tiêu kỳ sau |
| HOT/WARM chưa có SĐT | **43 HT** |
| Có SĐT | 19.4% |
| Bỏ sau 1 lượt | 45.3% |
| `O-00` | **28.3%** — ⛔ vượt ngưỡng 10%, đang chờ bổ sung mã |
| % Hot theo chiến dịch | chưa nối `ad_id` |

⚠ **Ba nhóm booking không tách biệt nhau thì tiêu chí chưa đúng** — ⛔ đừng siết SLA, sửa tiêu chí.

**Điều kiện kỹ thuật:** lấy được nội dung hội thoại từ Caresoft hoặc API hộp thư Page · gộp trùng khách nhắn nhiều page (theo SĐT hoặc PSID) · thí điểm trước ở page đã nối CRM.

---

## 12. ★ RÀO AN TOÀN — KẾ THỪA `id-F` §7

```
① ĐIỂM NÀY CHẤM KHÁCH, KHÔNG CHẤM NGƯỜI.
   Mọi dữ kiện về nhân viên trong JSON là ĐẦU VÀO cho id-F, ⛔ không phải điểm.

② MỖI ĐIỂM PHẢI CÓ BẰNG CHỨNG GẮN HT-nnn.
   Không trích được câu chat → tiêu chí đó cho 0, ⛔ không đoán.

③ LỖI HỆ KHÔNG TRỪ ĐIỂM AI.
   Thiếu bảng giá · page không có dịch vụ · ngoài giờ → nguyen_nhan_roi="hệ thống",
   ⛔ không trừ khách E-gì, ⛔ không trừ nhân viên.

④ ⛔ KHÔNG XẾP HẠNG CÁ NHÂN CÔNG KHAI.
   «% HOT_CHUA_SO theo từng nhân viên» CHỈ xuất hiện trong sổ tay riêng của
   người đó và bản của trưởng nhóm. ⛔ Không dán lên màn hình chung.

⑤ ĐIỂM LÀ THỨ TỰ GỌI, ⛔ KHÔNG PHẢI QUYỀN ĐƯỢC TƯ VẤN.
   ⛔ Không dùng điểm để bỏ khách hay từ chối tư vấn y khoa.
   Khách Cold vẫn được chăm sóc tự động.
```

---

## 13. RISK / WARNING

- **Dữ liệu sức khỏe là dữ liệu nhạy cảm**: giới hạn quyền xem · che SĐT khi gửi sang công cụ AI bên ngoài nếu không cần · ⛔ không lưu ảnh ngoài hệ thống · tin chào tự động có câu xin đồng ý xử lý dữ liệu. **Cần pháp chế xác nhận trước khi chạy toàn hệ thống.**
- **Ba ngưỡng ở §7.2 và hệ số ở §8 chưa được booking kiểm.** Suy ra từ một kỳ, một line. ⛔ Đừng dùng chúng để đánh giá chiến dịch hay con người cho tới tuần 5–6.
- **Tập vàng hiện có lệch line.** 494 HT đều là line Da; CD1–CD7 là ca da/tiêm. ⛔ Không kết luận gì về PTTM từ tập này.
- **`O-00` = 28.3%** — hơn một phần tư rào cản chưa có mã. Mọi bảng đếm mã `O` kỳ này phải hiện `O-00` riêng, ⛔ không gộp.
- **AI bịa bằng chứng / đọc sai SĐT**: bắt buộc trường bằng chứng; kiểm ngẫu nhiên 5% mỗi tuần.
- **Nhân viên "làm đẹp" điểm**: điểm chỉ tính lời khách; kết quả cuối đo bằng booking.
- **Lệch theo BL**: theo dõi Hot→Booking theo từng BL; lệch thì tách ngưỡng ở v1.2.
- **Hội thoại đa ngôn ngữ**: CD1 *(khách nói tiếng nước ngoài)* có **29 HT** trong kỳ. Tiêu chí giữ nguyên; prompt phải nêu rõ AI đọc được tiếng Anh và ngôn ngữ khác.

---

## 14. TỰ KIỂM BẢN NÀY

- [ ] Mọi hội thoại có `ht_id` truy ngược được chưa?
- [ ] `class_id_d` và `class_kf60` có cùng được ghi, và `lech_nhan` có được đếm chưa?
- [ ] Danh sách lệch nhãn có vượt 5% không? Vượt thì đã **dừng** chưa?
- [ ] Rào cản có dùng đúng `O-01…O-12`/`O-00`, ⛔ không mã tự đặt?
- [ ] `O-00` vượt 10% đã **báo lại** chưa?
- [ ] `nguyen_nhan_roi` có **đúng một** giá trị, và tổng có bằng cỡ mẫu?
- [ ] `E1`/`E3` có bị trừ cho hội thoại rơi do **trực page** không?
- [ ] Ô `HOT/WARM chưa có SĐT` có lên thẻ số tổng chưa?
- [ ] Có số liệu cá nhân nào của nhân viên lọt ra ngoài sổ tay riêng không?
- [ ] Ba ngưỡng §7.2 có bị trích dẫn như con số đã kiểm không?
- [ ] Đã bỏ hết tên · SĐT · ảnh khách trong phần bằng chứng chưa?
- [ ] `O-07` và `O-12` có bị tự trả lời không?

---

### Liên quan
`id-D` §1–§3 (mã `O` · 5 tín hiệu · vì sao rơi) · `id-F` §5, §7 (cờ đỏ · rào an toàn) · `id-G` §3 (hệ số giá trị đơn) · `id-C` §2 (chân dung · `he_so_gia_tri`) · `id-K` §3 (giá · bảo hành đang chặn) · KF-49/KF-50 (chấm chiến dịch Lead v2) · KF-21/22/34 (CDP automation) · KF-11 (pháp lý truyền thông)
