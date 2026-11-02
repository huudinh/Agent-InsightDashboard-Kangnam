# CHANGELOG

## v1.2 — 2026-11-02 · ★ THƯ VIỆN CHÂN DUNG KF-62 · LEAD SCORING KF-60 · ⛔ BỎ SỔ `id-C`

Hai văn bản của khối Sale nhập vào thành hai sổ: **KF-60 lead scoring** → `id-L`,
**KF-62 thư viện chân dung** → `id-M`. Sổ `id-C` bị **bỏ hẳn**: phần chân dung đã
có chỗ khác, phần còn lại gộp về `id-D`.

### Đổi gì

| Chỗ | Trước (`v1.1`) | Sau (`v1.2`) |
|---|---|---|
| Chân dung | **Phác họa theo từng kỳ**, duyệt ở `CỔNG 0`, mã `CD0…CDn` chỉ đúng trong kỳ | **Thư viện cố định KF-62** — 18 dịch vụ × 85 chân dung, mã dùng chung giữa mọi kỳ. Xếp hai bước: *dịch vụ trước, chân dung sau*, "Có" đầu tiên thắng |
| Mã dự trữ | `CD0` | `<DV>-CHUA_XAC_DINH` (biết dịch vụ, chưa biết chân dung) và `KHONG_XAC_DINH_DV` (chưa biết hỏi về gì) |
| Lead scoring | ⛔ không có | `id-L` — 19 tiêu chí `A1…E5`, **4 nhóm gọi** `GỌI NGAY · XIN SỐ · NUÔI · KHÔNG`, `ưu tiên = điểm × hệ số giá trị đơn` |
| Nhãn nóng | `id-D` §2 (5 tín hiệu) | ⛔ **không đổi** — KF-60 bản `v1.1` đã **bỏ nhãn HOT/WARM/COLD riêng** của nó để khỏi có hai nhãn nóng lệch nhau |
| Hệ số giá trị đơn | BL `1,0 – 0,5` | Thang **`1 / 2 / 3`** theo dịch vụ khách hỏi (`id-G` §3) — anh UY duyệt 02/11 |
| `knowledge/id-C` | Nấc `5A` · ma trận `CD×5A` · thông điệp thắng · cơ hội win | ⛔ **Bỏ sổ.** `5A` → `id-D` §3 · ma trận → `id-D` §6 · đầu ra B3 → `id-D` §9 · thông điệp → `id-M` §8 · xếp hạng chân dung → `id-M` §7 |
| Schema | `insight-dashboard-kangnam/1` | `/2` — thêm khối `lead` |
| Dashboard | 9 tab | 10 tab — thêm **Hàng chờ Sale**; bố cục `?bo_cuc=sale` |
| Đầu vào | Caresoft | thêm **KNB 1.3.0** qua `tools/knb.py` |

### Vì sao bỏ `id-C`

```
Sau khi có id-M, id-C còn lại bốn mục — và ba trong bốn đã có chỗ đúng hơn:

§4 cơ hội win  → xếp hạng CHÂN DUNG, đúng việc id-M đã có công thức anh UY chốt.
                 Hai công thức cho một quyết định là chỗ chắc chắn lệch nhau.
§2 ma trận     → cùng MỘT luật bốn ô với bảng giao của id-D §6, chỉ cắt theo
                 cặp khác. Để hai chỗ là nhân đôi luật, không phải nhân đôi việc.
§3 thông điệp  → luật cũ cấm "lấy từ kho"; nay KF-62 CHÍNH LÀ cái kho.
                 Luật phải viết lại, không phải chuyển chỗ → id-M §8.
§1 nấc 5A      → một trong BA nhãn đọc từ cùng một hội thoại; hai nhãn kia
                 (mã O, mức nóng) đã ở id-D. Tách ra một sổ riêng không có lý do.
```

### Ba cảnh báo còn mở

```
⚠ KF-62 CỔNG ① đạt 65,6% (yêu cầu 70%) — khách gõ tên dịch vụ rồi hỏi giá
  (trung vị 44 ký tự), ⛔ không tả tình trạng. Báo cáo mỗi kỳ ghi rõ, ⛔ không
  tự nới ngưỡng.
⚠ Xếp hạng chân dung (`id-M` §7) chưa chạy được công thức chính — chưa có dòng
  CRM nào về. Đang dùng bản tạm, mọi dòng gắn `⚠ proxy`.
⚠ Thang hệ số 1/2/3 chưa thử trên kỳ có PTTM — đã xin một kỳ để đo.
```

---

## v1.1 — 2026-10-30 · ⛔ BỎ BỘ CHÂN DUNG DỰNG SẴN

Chân dung khách hàng **không còn là một danh sách cho trước**. Mỗi kỳ, agent **phác họa chân dung từ chính hội thoại được đưa vào**, người dùng duyệt ở **CỔNG 0** mới gán được.

### Vì sao

Bản `v1.0` chở theo bảy chân dung `CD0–CD6` dựng cho **dịch vụ nâng mũi**, nhận dạng bằng từ khoá *"mũi tẹt"*, *"nghẹt mũi"*, *"đầu mũi bóng đỏ"*. Chạy thật 295 hội thoại (`doc/03-output-mau.md` §4):

```
CD0 thăm dò     239/295 = 81% mẫu rơi vào ô "chưa rõ"
CD2 · CD5             0 HT — hai chân dung không có một người nào
```

★ Một bộ chân dung đẩy 81% khách vào ô *"chưa rõ"* thì không đo khách — nó đo chính nó. Và bộ dựng cho mũi thì sang kỳ mắt, hàm mặt, da là sai hẳn.

### Đổi gì

| Chỗ | Trước | Sau |
|---|---|---|
| `knowledge/id-C` | Bảng 7 chân dung + bảng *"thông điệp thắng"* viết sẵn cho từng CD | Phương pháp phác họa: 3 điều một chân dung phải có · `CD0` là mã dự trữ · số chân dung theo cỡ mẫu · luật giữ mã giữa các kỳ · quy trình 6 bước qua CỔNG 0 |
| `tools/tu_dien.json` | Khối `chan_dung` — 6 danh sách từ khoá về mũi | ⛔ Đã bỏ. Thêm khối `rao_can` *(nhận rào cản bằng chữ của khách, không suy từ CD)* và `_tu_dung` *(từ dừng để rút cụm chữ)* |
| `tools/id.py` | `gan_chan_dung()` khớp từ khoá · `TEN_CD` 7 tên cố định | Đọc `out/chan-dung.json` **đã duyệt**; chưa duyệt thì `cd = null`. Thêm lệnh `chan-dung` *(`--mau` · `--kiem` · `--duyet`)* và file `out/nguyen-lieu-chan-dung.json` |
| `gan_rao_can()` | *"chưa nói tình trạng"* suy từ `CD0`, *"đã làm nơi khác"* suy từ `CD3` | Nhận bằng chữ của khách. ⛔ Không nhãn nào suy ra từ chân dung — làm vậy là chấm lại hội thoại (luật ③) |
| Quy trình | 8 bước · 2 cổng | 8 bước · **3 cổng** — thêm `CỔNG 0` duyệt chân dung, nằm trong B3 |
| `AUTO` | B1→B5 rồi dừng | Hai chặng: B1→B3 dừng ở CỔNG 0 · `DUYỆT CHÂN DUNG` → B3'→B5 dừng ở CỔNG 1 |
| Dashboard tab ② | Bảng 7 dòng | Bảng `N` dòng + dòng `CD0` · nhãn `👁 quan sát` cho CD <5 HT · ghi chú người duyệt CỔNG 0 · **ô khoá kèm lý do** khi chưa phác họa |
| `so_tay.py` | Tên chân dung lấy từ bảng cố định | Lấy từ `out/chan-dung.json` của kỳ; chưa duyệt thì ghi *"chân dung chưa phác họa"* |

### Hai thứ cố ý giữ lại

```
① CD0 vẫn là mã DỰ TRỮ, không phác họa, không đổi nghĩa.
   Nhờ nó mà luật ④ "tổng phải khớp" còn đúng khi một hội thoại
   không khớp dấu hiệu nào. ⛔ CD0 vẫn KHÔNG phải "rác".

② Nấc 5A, mã O, mức nóng, rào cản, vì sao rơi, chấm điểm N1–N6
   KHÔNG phụ thuộc chân dung → gán được ngay ở B2, trước CỔNG 0.
   Nhờ vậy tab Phễu và tab Chấm điểm vẫn đọc được khi chân dung còn trống.
```

### ⚠ Việc còn lại

- `Agent-SeedingPlant` và các agent dùng chung mã cũ vẫn đang hiểu `CD1–CD6` theo bộ cố định. Trao đổi số liệu theo chân dung thì **gửi kèm `out/chan-dung.json` của kỳ** — xem `id-A` §2.
- Câu mẫu trong `tools/so_tay.py` *(`VIEC` theo nhóm `N`)* vẫn viết theo dịch vụ mũi. Chưa đổi trong bản này.

---

## v1.0 — 2026-10-30

Dựng mới `Agent-InsightDashboard-Kangnam`.

### Có gì

- `SYSTEM-PROMPT.md` *(7.502 ký tự)* + `SYSTEM-PROMPT-NGAN.md` *(5.552 ký tự, dưới trần 8.000 của ChatGPT)*
- **11 sổ tri thức** `id-A` … `id-K`
- **8 prompt mẫu**
- **Dashboard 9 tab** — trang HTML cố định đọc `data/*.json`, link không đổi giữa các kỳ
- **5 script chạy thật**: `id.py` *(doc · ads · bao-cao)*, `so_tay.py`, `gop-tham-khao.py`, `dem-ngan.py`, `trang-huong-dan.py`
- **Trang hướng dẫn cài đặt & prompt mẫu** — sinh từ `tools/huong-dan.json` bằng generator dùng chung của bộ agent; nút Copy đọc thẳng file nguồn trong repo
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
