# Tổng hợp tài liệu của 5 thành viên

Các README gốc được giữ nguyên trong `docs/code/<github-username>/README.md` để bảo toàn phần đóng góp cá nhân, ảnh minh chứng và đường dẫn lịch sử.

| GitHub | Phụ trách | README | Code |
|---|---|---|---|
| TV1 – Kiến trúc và nghiệm thu | [README](captainduycan-hub/README.md) | [README chung](../../README.md) |
| TV2 – Bộ luật cảnh báo | [README](foxyy163/README.md) | [warning_engine.py](../../src/warning_engine.py) |
| TV3 – CSV và kịch bản | [README](hathihongdao/README.md) | [simulator.py](../../src/simulator.py) · [CSV](../../data/scenarios.csv) |
| TV4 – Giao diện Streamlit | [README](ledan823-spec/README.md) | [main.py](../../app/main.py) |
| TV5 – Đối chiếu kết quả | [README](nguyenvc2772-sys/README.md) | [comparison.py](../../src/comparison.py) |

## Luồng tích hợp

1. TV3 dùng `load_scenarios()` đọc các kịch bản CSV.
2. TV2 dùng `assess_risk(speed_kmh, distance_m)` tính mức cảnh báo.
3. TV5 dùng `compare_scenarios(scenarios)` đối chiếu `expected_action` và `actual_level`.
4. TV4 hiển thị input và bảng kết quả qua Streamlit.
5. TV1 rà soát kiến trúc, tích hợp và tổng hợp báo cáo.

## Cách chạy

```bash
pip install -r requirements.txt
python -m src.comparison
streamlit run app/main.py
```

- [Notebook tổng hợp logic và mã nguồn](../../notebooks/Collision_Warning_Demo.ipynb)
- [Tổng hợp tiến độ và kết quả](../TONG_HOP_BAN_GIAO.md)

**Kết quả kiểm tra Python ngày 20/11/2026:** 5/5 kịch bản CSV PASS. Giao diện Streamlit cần cả nhóm mở kiểm tra trực tiếp trên máy trước khi nộp.
