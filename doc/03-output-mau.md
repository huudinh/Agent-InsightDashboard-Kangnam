# 03 · Đầu ra mẫu

Số dưới đây là **kết quả chạy thật** trên 300 hội thoại nâng mũi xuất từ Caresoft (12–13/10/2026), 295 hội thoại đủ điều kiện phân tích. Dùng để biết đầu ra trông thế nào và để so sánh khi hiệu chỉnh từ điển.

> ⚠️ **Lần chạy này là của bản `v1.0`, khi hệ còn một bộ bảy chân dung dựng sẵn cho dịch vụ mũi.** Từ `v1.1` bộ đó đã bỏ: chân dung được **phác họa từ chính hội thoại của kỳ** và duyệt ở **CỔNG 0** (`id-C` §1). Giữ bảng chân dung ở §4 lại vì **chính nó là bằng chứng** cho việc phải bỏ — xem ô ★ dưới bảng. Mọi phần khác của trang này *(thẻ số tổng · mức nóng · vì sao rơi · mã O · chấm điểm)* ⛔ không phụ thuộc chân dung nên vẫn đúng với bản hiện hành.

---

## 1 · Năm thẻ số tổng

| Thẻ | Giá trị | Đọc thế nào |
|---|---|---|
| Hội thoại phân tích | **295** | 300 xuất ra, 5 bị loại vì dưới 2 tin thật |
| Bỏ sau 1 lượt | **44,7%** | Gần một nửa khách nhắn một lượt rồi im |
| Có SĐT | **23,7%** | |
| Trả lời tin đầu ≤2′ | **90,5%** | Trong khung 8h30–22h · chuẩn ≥90% |
| ★ HOT/WARM chưa có SĐT | **33** | Lead nóng chưa vào tay telesale |

## 2 · Mức nóng

```
HOT    1      ← tín hiệu ② mốc thời gian và ⑤ khung giờ gọi gần như không xuất hiện
WARM 98
COLD 196
```

★ HOT = 1/295 **không có nghĩa tệp xấu**. Nó nói rằng nội dung không tạo mốc thời gian và trực page không hỏi khung giờ gọi — hai việc sửa được ngay trong kỳ.

## 3 · Vì sao rơi

| Nguyên nhân | HT | Ai sửa |
|---|---|---|
| trực page | **124** | Trực page |
| khách tự dừng | 96 | — |
| không rơi | 75 | — |

⚠️ 124/295 rơi do trực page là con số đưa thẳng vào nhóm 🔧 *"sửa vận hành trước"* của ma trận — những ô đó ⛔ **không làm nội dung**.

## 4 · Chân dung

| Mã | Chân dung | HT | HOT | WARM | Có SĐT | % có SĐT | Chốt lịch |
|---|---|---:|---:|---:|---:|---:|---:|
| `CD0` | Thăm dò — chưa rõ nhu cầu | **239** | 1 | 79 | 50 | 20,9% | 9 |
| `CD1` | Khuyết điểm | 21 | 0 | 6 | 5 | 23,8% | 1 |
| `CD3` | **Sửa lại** | 29 | 0 | 19 | 13 | **44,8%** | 2 |
| `CD4` | Nam giới | 3 | 0 | 2 | 2 | 66,7% | 1 |
| `CD6` | Khó, bệnh lý | 3 | 0 | 0 | 0 | 0% | 1 |
| `CD2` `CD5` | Hot Face · Phong thủy | 0 | | | | | |

★ Ba kết luận đọc ngay được:

```
① CD0 chiếm 239/295 (81%) — quảng cáo kéo được người vào
   nhưng KHÔNG làm họ nói tình trạng. Đây là khối ② Giảm COLD của ma trận.

② CD3 "sửa lại" chỉ 29 HT nhưng % có SĐT 44,8% — GẤP ĐÔI CD0.
   Tệp nhỏ, nóng, giá trị đơn cao. Đây là ô đáng làm nhất của khối ① Tăng HOT.

③ ★ VÀ: chính bảng này là lý do bỏ bộ chân dung dựng sẵn.
   81% mẫu rơi vào ô "chưa rõ", hai chân dung không có một người nào
   (CD2 Hot Face · CD5 Phong thủy) — bộ chân dung này không đo khách,
   nó đo chính nó. Từ v1.1: phác họa từ hội thoại, duyệt ở CỔNG 0.
```

## 5 · Mã phản đối

| Mã | Tên | HT | % |
|---|---|---:|---:|
| `O-08` | Không biết mình cần gì | 135 | 45,8% |
| `O-01` | Giá & phát sinh | 109 | 36,9% |
| `O-09` | Thời gian · khoảng cách | 27 | 9,2% |
| `O-00` | Không xếp được | 32 | 10,8% ⚠ |
| `(chưa nêu)` | Khách chưa nêu phản đối nào | 72 | 24,4% |

⚠️ `O-00` 10,8% vượt ngưỡng 10% → tín hiệu **bổ sung từ điển**, ⛔ không tự thêm mã mới.
⚠️ `(chưa nêu)` 24,4% là chuyện khác hẳn: khách vào rồi không nói gì. Đó là vấn đề **quảng cáo**, không phải vấn đề từ điển. ⛔ Hai con số này ⛔ không được gộp.

## 6 · Chấm điểm — % đạt của cả khối

| Nhóm | | % đạt |
|---|---|---:|
| `N1` | Phản hồi & SLA | 76,6% |
| `N2` | **Khai thác tình trạng** | **35,4%** 🔴 |
| `N3` | Trả lời đúng & minh bạch | 92,6% |
| `N4` | Xử lý rào cản | 73,4% |
| `N5` | **Xin số & chốt** | **28,5%** 🔴 |
| `N6` | Ngôn từ & thái độ | 99,5% |

**Phân bố:** C 11 · D 2 · chưa đủ mẫu 11

★ Hai nhóm thủng là `N2` và `N5` — và chúng kể đúng một câu chuyện:

> Trực page **xin số trước khi biết khách cần gì** (`N2.1`), rồi **không hỏi khung giờ nghe máy, không mời lịch có ngày giờ** (`N5.3`, `N5.4`).
> Đó cũng chính là lý do tín hiệu ⑤ gần như bằng 0 và HOT chỉ có 1 ở §2.

⚠️ `N3` đạt 92,6% **không phải vì trực page trả lời đúng** — mà vì `N3.2` *"thông tin khớp bảng hiện hành"* luôn chấm `—` *(cần người đối chiếu bảng giá, script không làm được)*. Đọc `%` phải kèm cột *không áp dụng*.

## 7 · Sổ tay sinh ra

```
13 bản ST-CN + 1 ST-TN + 1 ST-ND
11 người chưa đủ 10 hội thoại → ⛔ không phân loại, ⛔ không sinh sổ
```

Một trang `ST-CN` loại C trông như thế này *(đã rút gọn)*:

```markdown
# SỔ TAY THỰC THI · <tên>
Kỳ 12-13/10 · 11 hội thoại · 62.3/100 · loại **C**

> Điểm dùng để phân việc kèm cặp. Không phải căn cứ kỷ luật hay xếp hạng công khai.

## 2 · ★ HAI VIỆC CỦA KỲ TỚI

### 1. Hỏi MỘT câu về tình trạng trước khi gõ câu xin số
Vì sao: nhóm N2 đạt 34.1% trên 11 hội thoại áp dụng (cả khối 35.4%).
Bằng chứng:
- HT-056 · trượt N2.2, N2.3, N2.4 · khách thuộc CD0 · khách tự dừng
- HT-113 · trượt N2.2, N2.3 · khách thuộc CD1 · khách tự dừng
Câu dùng được ngay:
- ✅ Trước đây mình đã can thiệp vùng mũi lần nào chưa ạ?
- ⛔ "Chị cho em xin số điện thoại" — gõ ngay khi chưa biết khách cần gì
Đo kỳ sau: N2 từ 34.1% lên 49%
```

## 8 · Cờ đỏ — chạy trên file mẫu 6 hội thoại

```
CĐ-2   <NV>   HT-003   « bảo hành trọn đời »
CĐ-3   <NV>   HT-004   « bệnh đó không ảnh hưởng »
```

★ Hai cờ này không phải lỗi thái độ — chúng là hệ quả trực tiếp của hai thứ **hệ thống chưa cấp**: chính sách bảo hành bằng văn bản, và hướng dẫn trả lời ca có bệnh nền. Xem `id-K §3`.
