# 02 · Dòng lệnh

Script làm phần **đếm được**. Phần **đọc hiểu** — **phác họa chân dung**, insight, câu hỏi ngầm, hướng nội dung, câu mẫu trong sổ tay — là việc của agent. ⛔ Script không thay được.

---

## Một kỳ đầy đủ

```bash
# ① đọc hội thoại → phân loại + chấm điểm + nguyên liệu phác họa chân dung
python tools/id.py doc du-lieu/hoi-thoai.md --ky "19-25/10"

# ② lấy khuôn bản phác họa → AGENT đọc nguyên liệu và điền `tep`
python tools/id.py chan-dung --ky "19-25/10" --mau

# ③ soát bản phác họa
python tools/id.py chan-dung --ky "19-25/10" --kiem

# ④ ★ CỔNG 0 — NGƯỜI DÙNG duyệt, ⛔ không phải agent
python tools/id.py chan-dung --ky "19-25/10" --duyet "Tên người duyệt"

# ⑤ chạy lại: giờ mới có chân dung trong mọi bảng
python tools/id.py doc du-lieu/hoi-thoai.md --ky "19-25/10"

# ⑥ đọc số quảng cáo Facebook
python tools/id.py ads du-lieu/ads-facebook.csv --ky "19-25/10"

# ⑦ gộp thành JSON cho dashboard
python tools/id.py bao-cao --ky "19-25/10"

# ⑧ sinh khung sổ tay (sau khi ma trận đã duyệt)
python tools/so_tay.py --ky "19-25/10"

# ⑨ xem dashboard
cd dashboard && python -m http.server 8080
```

⚠️ Bước ①→⑤ chạy `doc` **hai lần** là đúng thiết kế: lần đầu chưa có chân dung nên ô `cd` để trống, lần sau gán theo bản đã duyệt. Luật *một lần chấm* vẫn giữ — mọi ô khác (nấc 5A, mã O, điểm N1–N6) đọc từ cùng một file hội thoại và cho cùng kết quả.

---

## `id.py doc`

| Ra | Nội dung |
|---|---|
| `out/cham-hoi-thoai.csv` | Một dòng mỗi hội thoại · 22 ô `✓/✗/—` · CD *(trống nếu chưa qua CỔNG 0)* · nấc · mã O · nhiệt · vì sao rơi · điểm · cờ đỏ |
| `out/doc-hoi-thoai.json` | Bản tổng hợp để `bao-cao` đọc lại |
| `out/nguyen-lieu-chan-dung.json` | ★ **Nguyên liệu phác họa chân dung**: cụm 2–3 chữ khách tự nói (đếm theo **số hội thoại**, ⛔ không theo số lần) · câu hỏi đầu từng HT đã ẩn danh · phân bố dịch vụ · nấc · rào cản |
| Màn hình | Thẻ số tổng · mức nóng · vì sao rơi · bảng chân dung *(hoặc 10 cụm chữ đông nhất nếu chưa phác họa)* · top mã O · % đạt 6 nhóm · phân bố A/B/C/D · cờ đỏ |

Nhận cả hai khuôn xuất Caresoft *(`### <a id="ht-n">` và `## n. Tên — Kênh`)*.

### ⚠ Ba chỗ script tự xử, cần biết

```
① Dòng hệ thống bị LOẠI khỏi lượt của khách:
   [Tệp đính kèm], 📞 Cuộc gọi thoại, "X đã gọi cho bạn", "Bạn có thể gọi cho X"…
   Không loại thì "bỏ sau 1 lượt" luôn ra 0%.

② Đồng hồ SLA chạy từ TIN ĐẦU TIÊN của hội thoại (kể cả dòng hệ thống)
   — đó là lúc khách bấm quảng cáo, không phải lúc khách gõ câu đầu.

③ "Khách gửi ảnh" chỉ tính khi ảnh đến SAU lời mời gửi ảnh của nhân viên.
   Bản xuất Caresoft gắn sẵn dòng ảnh vào mọi hội thoại đến từ quảng cáo.
```

### Hiệu chỉnh nhận dạng

Sửa [`tools/tu_dien.json`](../tools/tu_dien.json), ⛔ không sửa `id.py`.

⚠️ Từ khoá quá rộng làm một mã nuốt gần hết mẫu. Thêm từ xong **phải chạy lại và nhìn cột `%` của bảng mã O**. Khớp theo **ranh giới từ**, nên `mí` không khớp nhầm trong `mình`.

| Dấu hiệu | Nghĩa |
|---|---|
| Một mã `O` > 60% mẫu | Từ khoá của mã đó quá rộng — cắt bớt |
| `O-00` > 10% mẫu | Danh sách 12 mã thiếu — **báo lại**, ⛔ đừng tự thêm mã |
| `(chưa nêu)` cao | Khách vào rồi không nói gì — đó là vấn đề **quảng cáo**, không phải vấn đề từ điển |

---

## `id.py chan-dung` — CỔNG 0

| Cờ | Làm gì |
|---|---|
| `--mau` | Ghi khuôn trống `out/chan-dung.json`. Thêm `--ghi-de` để ghi lại lên file cũ |
| `--kiem` | Soát: trùng mã · thiếu tên · thiếu dấu hiệu · thiếu `HT-nnn` làm bằng · `he_so_gia_tri` ngoài 1–3 · sai kỳ. Còn lỗi thì thoát mã 1 |
| `--duyet "<tên>"` | ★ Mở CỔNG 0: ghi `trang_thai: da_duyet` + tên người duyệt + thời điểm |

⛔ **Agent không chạy `--duyet`.** Lệnh này là của người dùng. Script từ chối bản `da_duyet` mà `duyet_boi` trống.

Một dòng trong `tep`:

```jsonc
{
  "ma": "CD1",                                  // CD1, CD2… ⛔ CD0 là mã dự trữ
  "ten": "Đã làm rồi, đi sửa",                  // chữ của khách
  "ho_la_ai": "...",
  "noi_so": "Hỏng lần nữa, không ai chịu trách nhiệm",
  "dau_hieu": ["sửa lại", "làm lại", "bên kia làm"],
  "khong_phai": [],                             // cụm loại trừ khi hai CD chồng chữ
  "he_so_gia_tri": 3,                           // 1 · 2 · 3
  "trich": ["HT-002"]                           // ⛔ không được rỗng
}
```

★ Script xét **từ trên xuống, dòng đầu khớp thì lấy** → xếp chân dung **hẹp trước, rộng sau**. Không khớp dòng nào → `CD0`.

---

## `id.py ads`

Đọc CSV theo cột ở `id-B §3`, ra `out/doc-ads.json` + chuỗi `CPM → CTR → CPI → CPL → CPB → Booking/Lead` trên màn hình.

⚠️ Cột `muc_tieu` luôn `null` cho tới khi có mốc TB 30 ngày của từng dịch vụ. Script ⛔ **không tự đặt mốc**.

---

## `id.py bao-cao`

Ghi `dashboard/data/<ky>.json` + cập nhật `dashboard/data/index.json`.

Ma trận luôn khởi tạo ở `trang_thai: "cho_duyet"` → tab **Ngân hàng hook** và **Sổ tay** còn khoá. Agent điền `da_duyet` sau CỔNG 1.

Chân dung chưa qua CỔNG 0 → `chan_dung.tep` rỗng, dashboard khoá tab ② lại kèm lý do, và một cảnh báo đỏ hiện ở đầu trang.

---

## `so_tay.py`

| Ra | Cho ai |
|---|---|
| `out/so-tay/ST-CN_<tên>.md` | Từng nhân viên ≥10 hội thoại |
| `out/so-tay/ST-TN_truong-nhom.md` | Trưởng nhóm — có bảng điểm cả nhóm |
| `out/so-tay/ST-ND_noi-dung.md` | Người làm nội dung — ⛔ không có tên nhân viên nào |

`--chi "<tên>"` để sinh lại một người.

Mọi chỗ `«agent điền: …»` là phần đọc hiểu — agent phải viết trước khi phát. Dùng [`prompts/prompt-so-tay.md`](../prompts/prompt-so-tay.md).

---

## Phụ trợ

```bash
python tools/gop-tham-khao.py   # gộp knowledge/ → goi/GOP-tri-thuc.md (chạy sau mỗi lần sửa)
python tools/dem-ngan.py        # canh giới hạn 8.000 ký tự của bản ngắn
python tools/trang-huong-dan.py # sinh lại tools/huong-dan.html
```

### `trang-huong-dan.py`

Generator **dùng chung** cho cả bộ agent trong `Project/Agent`. Phần riêng của gói này nằm ở
[`tools/huong-dan.json`](../tools/huong-dan.json) — ⛔ **sửa JSON, không sửa generator**.

Nút Copy trên trang **đọc thẳng file nguồn trong repo** (`doc(duong_dan)`), nên sửa `knowledge/`
rồi chạy lại là nút Copy tự khớp. Script cũng **chặn** nếu Thẻ B vượt 8.000 ký tự.

---

## Khi script báo lỗi

| Lỗi | Xử |
|---|---|
| `⛔ Không nhận ra khuôn file hội thoại` | File không đúng khuôn Caresoft — xem `id-B §2` |
| `⛔ Chưa có out/doc-hoi-thoai.json` | Chạy `id.py doc` trước |
| Tiếng Việt vỡ trên Windows | `set PYTHONIOENCODING=utf-8` trước khi chạy |
| Dashboard báo *"Không tải được danh sách kỳ"* | Chưa chạy `bao-cao`, hoặc đang mở bằng `file://` thay vì máy chủ tĩnh |
