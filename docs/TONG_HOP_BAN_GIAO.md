# Tổng hợp bàn giao và kiểm tra tích hợp

**Ngày kiểm tra:** 20/11/2026. **Hạn nộp:** 24/11/2026.

## Hiện trạng

| Thành viên | Phần việc | Dấu hiệu bàn giao |
|---|---|---|
| TV1 | Kiến trúc và tích hợp | Có README rà soát chi tiết; nghiệm thu trình duyệt và báo cáo cuối chưa xác nhận |
| TV2 | Luật IF–THEN | Có code `src/warning_engine.py` và README |
| TV3 | CSV và kịch bản | Có `src/simulator.py`, `data/scenarios.csv`, README và minh chứng |
| TV4 | Streamlit | Có `app/main.py`, README và ảnh kết quả |
| TV5 | So sánh | Có `src/comparison.py`, README và minh chứng |

## Phân tích luồng code

- `load_scenarios()`: trả về `list[dict]` với 5 cột chuẩn.
- `assess_risk(speed_kmh,distance_m)`: trả `level/reason/rule_id/stopping_distance_m/warning_distance_m`.
- `compare_scenarios(scenarios)`: trả bảng thêm `actual_level/status` và các trường giải thích.
- `app/main.py`: import đúng cả ba hàm và hiển thị Streamlit.

## Thử nghiệm thực tế

Chạy `python -m src.comparison` trên bản code từ `main`:

| Kịch bản | Dự kiến | Thực tế | Kết quả |
|---|---|---|---|
| SC01 | SAFE | SAFE | PASS |
| SC02 | WARNING | WARNING | PASS |
| SC03 | DANGER | DANGER | PASS |
| SC04 | WARNING | WARNING | PASS |
| SC05 | DANGER | DANGER | PASS |

**Tổng:** PASS 5, FAIL 0, ERROR 0.

Notebook tổng hợp thực thi độc lập các ô Python và cũng trả 5/5 PASS. Mã đầy đủ của TV2, TV3, TV4 và TV5 được đặt trong notebook; phần TV4 là mã xuất tệp để chạy qua Streamlit, không phải giao diện nhúng bên trong Colab.

## Việc bắt buộc trước hạn nộp

- [ ] TV1/TV4 mở thử `streamlit run app/main.py` và xác nhận UI trên trình duyệt.
- [ ] Chụp ảnh 3 mức SAFE/WARNING/DANGER và bảng PASS để đưa vào báo cáo Word.
- [ ] Điền tên giáo viên, rà nội dung Word cuối và xác minh thành viên đã đọc script vấn đáp.
- [ ] Chạy lại sau khi cập nhật code cuối, rồi nộp Word + link GitHub.

## Quyết định dọn repo

Giữ nguyên tài liệu Week 1 và README cá nhân để bảo toàn lịch sử, ảnh chứng minh và liên kết từ issue. Các thư mục `src/`, `app/`, `data/`, `docs/code/` và `images/` hiện có vai trò rõ ràng; **chưa xóa file nào** vì chưa xác định được file dư thừa chắc chắn. Không nên xóa các tài liệu tham chiếu chỉ để làm repo ngắn hơn.
