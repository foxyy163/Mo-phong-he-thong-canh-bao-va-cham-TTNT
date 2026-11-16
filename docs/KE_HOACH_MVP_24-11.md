# Kế hoạch MVP — Hạn nộp 24/11/2026

> Bản cập nhật nhằm rút gọn phạm vi sau khi hoàn thành Week 1. **Giữ nguyên** các tài liệu tác giả tại `docs/week 1/`; không xóa hoặc đổi tên tài liệu của thành viên.

## Mục tiêu

Mô phỏng cảnh báo va chạm bằng Python, Streamlit, dữ liệu CSV và hệ chuyên gia IF–THEN. **Không** làm SQL, REST API, Docker, 3D, camera, mô hình ML/DL hay backend riêng. Hệ thống phục vụ học tập, không sử dụng làm hệ thống cảnh báo xe thật.

## Cấu trúc code đang có — tiếp tục tận dụng

```text
README.md
requirements.txt
app/main.py                   # Giao diện Streamlit — TV4
src/warning_engine.py         # Bộ luật AI — TV2
src/simulator.py              # Dữ liệu và các tình huống — TV3
data/scenarios.csv            # Kịch bản CSV — TV3
src/comparison.py            # So sánh kết quả — TV5 (sẽ bổ sung)
docs/week 1/                 # 5 tài liệu và bản tổng hợp đã làm
docs/KE_HOACH_MVP_24-11.md    # Tài liệu kế hoạch hiện tại
images/                       # Giữ các ảnh README đang sử dụng
```

**Không cần thêm** `src/contracts.py`, `src/orchestrator.py`, `data_manager.py` hoặc đổi sang bộ tên file mới. TV1 tích hợp bằng cách thống nhất chữ ký hàm và kiểm tra đường dẫn import, không tạo một tầng kiến trúc mới.

## Chốt quy ước để code độc lập

- Input: `speed_kmh` (km/h), `distance_m` (m), là các số hữu hạn không âm.
- Hàm AI: `assess_risk(speed_kmh, distance_m) -> dict` (giữ tên hàm đã có trong code).
- Output: `level` nhận `SAFE | WARNING | DANGER`, `reason` (giải thích), `rule_id` (`R01`/`R02`/`R03`); có thể thêm `stopping_distance_m`, `warning_distance_m` để UI hiển thị.
- Dữ liệu sai → `ValueError` (UI bắt lỗi).

**Luật AI thống nhất theo tài liệu W1-02:**

```python
v = speed_kmh / 3.6
d_stop = v * 1.0 + v**2 / (2 * 5.0)
d_warning = 1.5 * d_stop

if distance_m == 0 or distance_m <= d_stop:
    level = "DANGER"    # R01
elif distance_m <= d_warning:
    level = "WARNING"   # R02
else:
    level = "SAFE"      # R03
```

Với `speed_kmh=0, distance_m=0` cũng trả `DANGER` theo quy ước mô phỏng. Các hằng số `t=1s, a=5m/s², k=1.5` chỉ là giả định học tập.

### Các mâu thuẫn Week 1 cần xử lý ở giai đoạn code

1. W1-02 coi `distance_m=0` là DANGER, tài liệu System Design coi là lỗi. **MVP theo W1-02**, cần ghi chú trong báo cáo.
2. Code `src/warning_engine.py` hiện dùng ngưỡng cố định và nhãn tiếng Việt; khác bộ luật W1-02. **TV2 sửa code thành công thức trên và mã chuẩn.**
3. CSV hiện chỉ có `name,speed_kmh,distance_m`, tài liệu W1-03 muốn thêm `scenario_id,expected_action`. **TV3 chuẩn hóa thành 5 cột** `scenario_id,name,speed_kmh,distance_m,expected_action` và tính lại expected theo luật mới.
4. Ví dụ `60 km/h, 25m` theo W1-02 là **DANGER**, không phải WARNING; `60 km/h, 50m` là **WARNING**.

## Phân công — mỗi người một issue

| Workstream | Tiếp nối tài liệu | File/trách nhiệm | Điều kiện hoàn thành |
|---|---|---|---|
| TV1 — tích hợp & báo cáo | W1-01 / architecture.md | README, kiểm tra module và ghép báo cáo Word | Chạy app và 3 kịch bản mẫu; báo cáo tổng hợp được |
| TV2 — luật cảnh báo | W1-02 / warning_rules.md | src/warning_engine.py | 3 mức đúng công thức và trường hợp biên |
| TV3 — mô phỏng CSV | W1-03 / simulation_scenarios.md | src/simulator.py, data/scenarios.csv | ≥3 kịch bản, so sánh expected/actual |
| TV4 — giao diện | W1-04 / ui_design.md | app/main.py | Nhập tay/chọn kịch bản, hiển thị nhãn-màu-lý do |
| TV5 — đối chiếu & kết quả | W1-05 / requirements_testplan.md | src/comparison.py (tạo mới), docs/code/TV5.md | So sánh expected/actual, chạy thử 3 mức và báo cáo kết quả |

Mỗi thành viên phải tự viết phần **đóng góp trong báo cáo Word** và hiểu code của mình để vấn đáp.

## Timeline

- **17/11:** 5 người xác nhận công thức, contract, dữ liệu mẫu; nhận issue.
- **18–20/11:** Mỗi người sửa đúng file được giao trên `main`, tự chạy thử, thêm Markdown giải thích, đồng bộ Git rồi commit/push; bình luận link commit vào issue.
- **21/11:** TV1 review tích hợp; cả nhóm hỗ trợ fix.
- **22/11:** Chạy thủ công các tình huống, chụp ảnh demo thực, mỗi người nộp nội dung báo cáo.
- **23/11:** Chốt Word theo mẫu, tập vấn đáp và đóng gói mã nguồn.
- **24/11:** Nộp báo cáo Word + source code/link GitHub trước giờ đóng bài.

## Lệnh chạy sau khi hoàn thiện

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## Báo cáo theo yêu cầu giảng viên

1. Tên đề tài
2. Mục lục
3. Phân công công việc: tên, MSSV, đóng góp kỹ thuật **thực tế**
4. Phân tích bài toán
5. Thuật toán sử dụng (công thức, pseudocode hoặc sơ đồ)
6. Giao diện và kết quả chạy thật
7. Phụ lục (nếu cần)
8. Tài liệu tham khảo

**Đóng góp mới nên nêu ở mức phù hợp:** ứng dụng luật IF–THEN với ngưỡng phụ thuộc tốc độ; minh họa kết quả qua các tình huống. Không tuyên bố phát minh thuật toán hay có dữ liệu cảm biến thật.

## Bàn giao code kèm Markdown

Mỗi người tạo `docs/code/TV1.md` … `docs/code/TV5.md` trong PR riêng, trả lời ngắn: (1) Mình làm chức năng gì? (2) Hàm nào chính? (3) Input/Output? (4) Cách chạy? (5) Một ví dụ kết quả thực tế? (6) Mình có thể giải thích dòng xử lý quan trọng nào? Không chép lý thuyết dài. Các tài liệu gốc Week 1 vẫn giữ nguyên.

## Git Workflow

Week 1 Markdown giữ nguyên trên `main`. Từ giai đoạn code, mỗi người chỉ sửa file được giao và `docs/code/TVx.md`, tự chạy thử, `git pull --ff-only origin main` trước khi sửa/và trước khi push; commit đúng file, push trực tiếp `main`, bình luận link commit vào issue. TV1 kiểm tra kết quả trước khi đóng issue. Nếu lỗi non-fast-forward hoặc conflict thì dừng và báo nhóm trưởng, **không force push/ghi đè file người khác**.
