# 📊 Agent-InsightDashboard-Kangnam

> **Agent đọc Insight khách hàng của Bệnh viện Thẩm mỹ Kangnam.**
>
> Đọc **chính lời khách nói trong inbox** cùng **số quảng cáo Facebook / Google**, rồi trả lời bốn câu: **khách là ai · họ đang sợ gì · họ rơi ở đâu và vì ai · kỳ tới phải làm gì**.
>
> Đầu ra dùng được ngay: **dashboard insight · ma trận ưu tiên · ngân hàng hook · sổ tay thực thi riêng cho từng nhân viên**.

`v1.0` · 2026-10-30 · Claude / ChatGPT / Gemini / Claude Code

### 📘 [**Hướng dẫn cài đặt & prompt mẫu →**](https://claude.ai/artifact/PkfQjahnMx9Vfb3KxpM7wh)
### 📈 [**Dashboard mẫu — chạy thật trên 295 hội thoại →**](https://claude.ai/artifact/79zY1N3Ltg2kk33JzLg66y)

> Trang hướng dẫn có **nút Copy từng file**: 2 thẻ bộ não · 19 file tri thức · 16 prompt mẫu lọc theo nhóm · 6 câu smoke test. Người mới vào khối thì **mở trang này trước, đừng đọc README**.
>
> Dashboard: 9 tab · hội thoại thật *(12–13/10)*, số quảng cáo mô phỏng, **tên nhân viên đã thay bằng mã `NV-nn`**.

---

## Agent này làm gì

| Việc | Nghĩa |
|---|---|
| ① **Phác họa chân dung khách** | ⛔ Không có bộ chân dung dựng sẵn — mỗi kỳ phác họa 2–7 chân dung **từ chính hội thoại đưa vào**, người dùng duyệt ở **CỔNG 0**, rồi gán từng hội thoại × 5 nấc `A1–A5` |
| ② **Đào sâu insight** | 12 mã phản đối `O`, **câu hỏi ngầm**, 5 tín hiệu nóng, vì sao khách rơi |
| ③ ★ **Chấm điểm nhân viên trực page** | 22 tiêu chí `N1.1–N6.3` · thang 100 · phân loại A/B/C/D · 6 cờ đỏ |
| ④ **Ma trận ưu tiên** | 3 khối: Tăng HOT → Giảm COLD → Tối ưu WARM, có công thức điểm |
| ⑤ **Ngân hàng hook** | 7 loại hook × 16 format, mỗi hook **truy ngược được** về một hội thoại |
| ⑥ ★ **Sổ tay thực thi cá nhân hoá** | Một trang cho mỗi người: một việc, câu mẫu dùng ngay, cách đo kỳ sau |
| ⑦ **Dashboard 9 tab** | Trang HTML cố định, mỗi kỳ chỉ thêm một file JSON — **link không đổi** |

⛔ **Đây KHÔNG phải agent chấm cuộc gọi điện thoại** *(`Agent-QC-Telesale`)*, ⛔ **không phải agent lên kế hoạch quay theo bác sĩ** *(`Agent-SeedingPlant`)*, ⛔ **không phải agent chẩn đoán ads theo 30 mã cảnh báo** *(`Agent-AdsReport`)*.

---

## Đầu vào → Đầu ra

```
① 100–300 hội thoại chat (Caresoft)  ─┐                ┌─► ③ DASHBOARD 9 TAB
② Chỉ số quảng cáo Facebook          ─┼─►  AGENT  ─────┼─► ④ MA TRẬN ƯU TIÊN  ← cổng duyệt
③ Chỉ số Google Ads  🔴 chưa có      ─┘                ├─► ⑤ NGÂN HÀNG HOOK
                                                        ├─► ⑥ SỔ TAY từng nhân viên
                                                        └─► ⑦ VIỆC CẦN XỬ LÝ (có tên người)
```

---

## ★ Ba thứ khiến bản này khác các agent trước

| # | Khác gì | Vì sao |
|---|---|---|
| ① | **Chấm thang 100 + phân loại A/B/C/D** — trong khi `Agent-QC-Telesale` cố tình **không** chấm điểm số | Chat có bằng chứng đầy đủ và mốc thời gian chính xác đến giây; không có nhóm nào phụ thuộc âm thanh. Nhưng phải đi kèm **bốn rào an toàn** ở [`id-F §7`](knowledge/id-F-cham-diem-nhan-vien.md) — bỏ một cái là sổ này thành công cụ kỷ luật, không còn là công cụ kèm cặp |
| ② | **Sổ tay thực thi cá nhân hoá** — đầu ra đầu tiên trong hệ chạm tới từng con người | Dashboard để lãnh đạo nhìn; **sổ tay để nhân viên làm**. Luật một việc: D và B **1 việc** · C **2 việc** · A **1 việc + 2 đoạn chat mẫu** |
| ③ | **Nối mắt xích `inbox→lead` của công thức CPL với bằng chứng hội thoại** | Các agent ads khác chỉ **suy đoán** mắt xích này. Agent này chỉ thẳng ra bao nhiêu HT rơi do trực page và **vì câu nào** — nhờ đó mới dám nói *"kỳ này không phải vấn đề nội dung"* |

---

## Luật quan trọng nhất

```
CPL = (CPM/1000) ÷ ( CTR × click→inbox% × inbox→lead% )

⛔ KHÔNG KẾT LUẬN "CẦN LÀM THÊM NỘI DUNG" KHI THÀNH PHẦN XẤU ĐI KHÔNG PHẢI CTR.
```

| Thành phần xấu đi | Thật ra là việc của |
|---|---|
| **CTR** giảm | Nội dung |
| **CPM** tăng | Adnet — tệp, bid, lịch |
| **click→inbox** giảm | Kỹ thuật — điểm đến, lời chào tự động |
| **inbox→lead** giảm | ★ **Trực page** → chứng minh bằng chính hội thoại |

---

## Cài đặt nhanh

| Nền tảng | Dán vào | File |
|---|---|---|
| **Claude Project** | Custom instructions | [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |
| **ChatGPT Custom GPT** | Instructions *(trần 8.000 ký tự)* | [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) · 5.552 ký tự |
| **Gemini Gem** | Chỉ dẫn | [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |

Rồi nạp **11 file [`knowledge/`](knowledge/)** + **8 file [`prompts/`](prompts/)** vào Knowledge.
Nền tảng chỉ cho nạp ít file → dùng [`goi/GOP-tri-thuc.md`](goi/GOP-tri-thuc.md).

Chi tiết: [`doc/01-cai-dat.md`](doc/01-cai-dat.md)

---

## 11 sổ tri thức

| Sổ | Nội dung |
|---|---|
| [`id-A`](knowledge/id-A-vai-tro-quy-trinh.md) | Vai trò · 8 bước · **ba cổng chặn** · AUTO · ngưỡng mẫu · luật một lần chấm |
| [`id-B`](knowledge/id-B-doc-dau-vao.md) | Ba dòng đầu vào · cột bắt buộc · ẩn danh · quy ước mã |
| ★★ [`id-C`](knowledge/id-C-chan-dung-5A.md) | **Phác họa chân dung từ hội thoại · CỔNG 0** × hành trình `5A` · ma trận lỗ hổng phễu |
| ★ [`id-D`](knowledge/id-D-dao-sau-insight.md) | **12 mã `O` · 5 tín hiệu nóng · vì sao rơi · câu hỏi ngầm · bảng giao "yếu gì"** |
| ★ [`id-E`](knowledge/id-E-to-chuc-ads-chi-so.md) | **Tổ chức Ads** — 11 chiều cắt số · chuỗi chỉ số · phân rã CPL · VIEW/PERF · Google Ads |
| ★★ [`id-F`](knowledge/id-F-cham-diem-nhan-vien.md) | **Tiêu chí chấm điểm `N1–N6` · A/B/C/D · 6 cờ đỏ · 4 rào an toàn** |
| ★ [`id-G`](knowledge/id-G-ma-tran-uu-tien.md) | **Ma trận ưu tiên** — 3 khối, công thức điểm, nhóm *sửa vận hành trước* |
| [`id-H`](knowledge/id-H-ngan-hang-hook.md) | Ngân hàng hook — 7 loại × 16 format · 3 cách viết, 1 cách sai |
| ★ [`id-I`](knowledge/id-I-so-tay-thuc-thi.md) | **Sổ tay thực thi** — 3 loại · luật một việc · viết việc thế nào cho sửa được |
| [`id-J`](knowledge/id-J-dashboard-schema.md) | Dashboard 9 tab · schema JSON · 4 luật hiển thị |
| ★ [`id-K`](knowledge/id-K-module-kangnam-phap-che.md) | **Module đơn vị Kangnam** · 12 điểm pháp chế · ba thứ đang chặn |

★ **Đổi thương hiệu → thay đúng [`id-K`](knowledge/id-K-module-kangnam-phap-che.md), ⛔ không sửa lõi `id-A`…`id-J`.**

---

## Dòng lệnh

```bash
# đọc hội thoại → phân loại CD · 5A · mã O · nhiệt · vì sao rơi · chấm N1–N6
python tools/id.py doc du-lieu/hoi-thoai.md --ky "19-25/10"

# đọc số quảng cáo Facebook → chi → CPM→CTR→CPI→CPL→CPB
python tools/id.py ads du-lieu/ads-facebook.csv --ky "19-25/10"

# gộp thành JSON cho dashboard
python tools/id.py bao-cao --ky "19-25/10"

# sinh khung sổ tay từng người (sau khi ma trận đã duyệt)
python tools/so_tay.py --ky "19-25/10"

# xem dashboard
cd dashboard && python -m http.server 8080

# sinh lại trang hướng dẫn sau khi sửa knowledge/ hoặc prompts/
python tools/trang-huong-dan.py
```

> Nút Copy trên trang hướng dẫn **đọc thẳng file nguồn trong repo** — sửa `knowledge/` rồi chạy lại là nút Copy tự khớp, không bao giờ lệch với repo.

Chi tiết: [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md) · Kết quả mẫu: [`doc/03-output-mau.md`](doc/03-output-mau.md)

> ⚠️ Script làm phần **đếm được**. Phần **đọc hiểu** — insight, câu hỏi ngầm, hướng nội dung, câu mẫu trong sổ tay — là việc của agent. Script để lại `«agent điền: …»` đúng chỗ cần người.

---

## 8 prompt mẫu

| Prompt | Dùng khi |
|---|---|
| [`prompt-auto.md`](prompts/prompt-auto.md) | Chạy cả kỳ một phát, dừng ở cổng duyệt |
| ★ [`prompt-chan-dung-insight.md`](prompts/prompt-chan-dung-insight.md) | Chỉ cần phần khách hàng |
| ★ [`prompt-cham-diem.md`](prompts/prompt-cham-diem.md) | Chấm & phân loại trực page |
| [`prompt-doc-so-ads.md`](prompts/prompt-doc-so-ads.md) | Đọc số ads & nối với hội thoại |
| [`prompt-ma-tran.md`](prompts/prompt-ma-tran.md) | Dựng ma trận ưu tiên (cổng 1) |
| [`prompt-hook.md`](prompts/prompt-hook.md) | Viết ngân hàng hook (sau cổng 1) |
| ★ [`prompt-so-tay.md`](prompts/prompt-so-tay.md) | Viết sổ tay từng người |
| [`prompt-phap-che.md`](prompts/prompt-phap-che.md) | Soát cổng 2 trước khi phát |

---

## Mười luật bất biến

| # | Luật | Vì sao |
|---|---|---|
| ① | **Truy ngược** — mọi insight, hook, điểm trừ phải chỉ về `HT-nnn` hoặc một con số | Không truy ngược được = bịa |
| ② | **Phân rã CPL trước khi kết luận** | CPL tăng vì CPM mà đổi hook là chữa nhầm bệnh |
| ③ | **Một lần chấm** — một hội thoại chấm đúng một lần | Chấm lại giữa chừng làm hai phần báo cáo nói hai con số |
| ④ | **Tổng phải khớp** cỡ mẫu | |
| ⑤ | **Ngưỡng mẫu** — <10 HT không kết luận · <10 HT/người không phân loại | |
| ⑥ | **`—` không phải `✗`** | Gộp hai cái này làm một người trông tệ chỉ vì khách của họ không hỏi giá |
| ⑦ | ★ **Lỗi hệ không trừ điểm người** | Phần lớn ô *"né giá"* là do hệ thống chưa cấp bảng giá |
| ⑧ | ★ **Điểm để kèm cặp, không để kỷ luật** | ⛔ Không có bảng xếp hạng cá nhân ngoài sổ tay riêng |
| ⑨ | **Chưa đo hiện `—`, không hiện `0`** · chưa có mốc thì ghi `⚠`, ⛔ không tự đặt | `0` là đã đo và bằng không — hai thứ khác nhau |
| ⑩ | **Ẩn danh** — ⛔ không để lọt tên, SĐT, ảnh, link cá nhân của khách | |

---

## ⛔ Tuyệt đối không

- ⛔ **Nêu con số bảo hành** — ba mức *(3 năm / 10 năm / trọn đời)* đang cùng lưu hành, chưa có văn bản
- ⛔ **Trả lời câu bệnh nền / chống chỉ định** thay bác sĩ
- ⛔ **Gắn chức danh, số năm, số ca của bác sĩ** chưa đối chiếu chứng chỉ
- ⛔ **Nêu giá dịch vụ ngoài mắt** khi chưa có bảng giá hiện hành — và ⛔ không lấy số từ hook cũ làm nguồn giá
- ⛔ **Cam kết kết quả** · ⛔ **dìm đối thủ** · ⛔ dùng ảnh khách chưa có consent
- ⛔ **Trộn** `nhân viên chạy ads` với `nhân viên trực page`
- ⛔ **Nhận xét một nhân viên** mà không gắn được tiêu chí `N` + `HT-nnn`
- ⛔ Để **sổ tay của người này** chứa tên, điểm hay hội thoại của người khác
- ⛔ **Viết hook, sinh sổ tay** khi ma trận chưa được duyệt
- ⛔ **Phát bản còn cờ 🔴**

---

## 🔴 Đang bị chặn — cần cấp để mở

| # | Thứ còn thiếu | Ai cấp | Chặn gì |
|---|---|---|---|
| ① | **Mẫu sổ tay thực thi chính thức** | Người dùng *(đã hẹn gửi)* | 🟠 Khuôn `ST-CN` hiện là bản dựng tạm |
| ② | **Chính sách bảo hành bằng văn bản** | Vận hành + pháp chế | 🔴 Mã `O-07` · cờ đỏ `CĐ-2` · mọi hook chạm bảo hành |
| ③ | **Bảng giá hiện hành** dịch vụ ngoài mắt | Vận hành / sales | 🔴 Tiêu chí `N3.1` · hook `A4` có giá · format `L11` |
| ④ | **Đối chiếu chứng chỉ bác sĩ** đang chạy ads | Vận hành + pháp chế | 🔴 Cờ đỏ `CĐ-4` |
| ⑤ | **Dữ liệu Google Ads** | Khối Ads | 🟠 Tab ⑤ trống — khung đọc đã dựng sẵn |
| ⑥ | **Mốc mục tiêu TB 30 ngày** từng dịch vụ | Khối Ads | 🟠 Mọi chỉ số ads ghi `⚠ chưa có mốc so sánh` |
| ⑦ | **Xác nhận quy ước tên chiến dịch** 11 chiều | Khối Ads | 🟡 Bảng giải mã đang là *suy ra từ dữ liệu* |
| ⑧ | **Định nghĩa format `L13`–`L16`** | Content Lead | 🟡 Có trong kế hoạch hook nhưng chưa ai viết định nghĩa |

⚠️ **Mục ② cấp bách nhất.** Trong hội thoại thật đã có nhân viên trả lời khách *"bên em bảo hành trọn đời"*. Hệ thống đang để mỗi người tự chọn một trong ba con số — đó không phải lỗi thái độ, đó là lỗ hổng vận hành.

---

## Cây thư mục

```
Agent-InsightDashboard-Kangnam/
├── SYSTEM-PROMPT.md          bộ não đầy đủ
├── SYSTEM-PROMPT-NGAN.md     bản ≤8.000 ký tự cho ChatGPT
├── knowledge/                11 sổ id-A … id-K
├── prompts/                  8 prompt mẫu
├── goi/GOP-tri-thuc.md       bản gộp (sinh tự động)
├── template/                 dữ liệu mẫu để chạy thử
├── tools/                    id.py · so_tay.py · tu_dien.json · gop-tham-khao.py · dem-ngan.py
│                             trang-huong-dan.py + huong-dan.json → huong-dan.html
├── dashboard/                index.html (cố định) + data/*.json (mỗi kỳ một file)
├── doc/                      cài đặt · dòng lệnh · output mẫu · changelog
└── out/                      kết quả — ⛔ KHÔNG commit
```

⛔ `out/`, `du-lieu/`, file hội thoại gốc, ảnh khách — [`.gitignore`](.gitignore) đã chặn.
"# Agent-InsightDashboard-Kangnam" 
