# W1-03 — Dữ liệu và kịch bản mô phỏng (MVP hiện hành)

> **Cập nhật 17/11/2026 — dùng cho giai đoạn code trước hạn 24/11.** [README chính](https://github.com/foxyy163/Mo-phong-he-thong-canh-bao-va-cham-TTNT/blob/main/README.md) và [kế hoạch MVP](https://github.com/foxyy163/Mo-phong-he-thong-canh-bao-va-cham-TTNT/blob/main/docs/KE_HOACH_MVP_24-11.md) là chuẩn triển khai hiện hành. Phần thiết kế Week 1 gốc nằm ở cuối file, chỉ để tham khảo quá trình làm bài. Nếu có khác biệt, **ưu tiên quy ước MVP phía trên**. Không cần REST API, Docker, SQL, mô phỏng 3D, branch/PR hay unit test tự động.

## Công việc TV3

1. Hoàn thiện `data/scenarios.csv` theo chuẩn 5 cột thống nhất.
2. Viết hàm `load_scenarios()` trong `src/simulator.py` dùng `csv.DictReader`; kết quả `list[dict]` với `speed_kmh` và `distance_m` là `float`.
3. Không giữ danh sách `SCENARIOS` hard-code khác với CSV.
4. Chạy thử đọc đủ ít nhất ba tình huống, rồi bàn giao dict cho TV5; không tự viết so sánh PASS/FAIL (TV5 phụ trách).
5. Tạo `docs/code/hathihongdao/README.md` giải thích cấu trúc CSV, cách nạp và ví dụ đọc dữ liệu.

## CSV chung để tránh lệch kết quả

```csv
scenario_id,name,speed_kmh,distance_m,expected_action
SC01,An toàn,30,30,SAFE
SC02,Cảnh báo,30,20,WARNING
SC03,Nguy hiểm,30,10,DANGER
```

| Kịch bản | Kỳ vọng | Lý do |
|---|---|---|
| SC01 | SAFE | 30 m lớn hơn ngưỡng cảnh báo với 30 km/h |
| SC02 | WARNING | 20 m nằm giữa ngưỡng dừng và ngưỡng cảnh báo |
| SC03 | DANGER | 10 m nhỏ hơn khoảng cách dừng |

**Không dùng** ví dụ cũ `60 km/h, 25 m → WARNING`: theo luật W1-02 hiện hành, tình huống này phải là **DANGER**. CSV cần đồng bộ với AI trước khi TV5 làm phần so sánh.

---

<details>
<summary>📚 Xem bản thiết kế Week 1 gốc (lưu để đối chiếu quá trình làm)</summary>

THIẾT KẾ DỮ LIỆU VÀ KỊCH BẢN MÔ PHỎNG (SIMULATION_SCENARIOS)

• Đề tài: Mô phỏng hệ thống cảnh báo va chạm (Forward Collision Warning System)

• Issue: W1-03 – Thiết kế dữ liệu và kịch bản mô phỏng

• Vai trò: simulation_scenarios

• Tài liệu bàn giao: docs/week1/simulation_scenarios.md

1.Mô tả dữ liệu và Giả định môi trường

• Mô tả dữ liệu: Việc sử dụng dữ liệu mô phỏng nhằm trừu tượng hóa bài toán, cung cấp một môi trường lý tưởng (đã biết, tất định, không nhiễu) để kiểm tra độ chính xác của logic AI mà không đòi hỏi thiết bị phần cứng đắt tiền hay nguy hiểm.
• Giả định môi trường:
    • Xe di chuyển trên đường thẳng, bề mặt phẳng. Vận tốc tại thời diểm mô phỏng được xem là hằng số.
   • Vật cản phía trước là vật thể tĩnh nằm trên cùng làn đường.
   • Hệ thống áp dụng “bước thời gian đơn” để đánh giá mức độ nguy hiểm tức thời đị một khoảng khắc.

2. Cấu trúc dữ liệu dự kiến
   
• Dữ liệu mô phỏng được định dang CSV nhắm tối ưu hóa quá trình đọc và nạp tài liệu tự động vào mã nguồn Python.
• Cấu trúc file gồm 4 cột dữ liệu cốt lõi:
1.	Scenario_id (string): Mã kịch bản mô phỏng
2.	Speed_kmh (Float): tốc độ hiện tại của xe (ràng buộc: >= 0 km/h)
3.	Distance_m (Float): khoảng cách đến vật cản(ràng buộc: > 0 m)
4.	Expected_action (String): trạng thái cảnh báo kì vọng (SAFE, WARNING, DANGER)

3.Bảng tốc độ và khoảng cách (kịch bản cụ thể)

Scenario_id	Tốc độ (km/h)	Khoảng cách (m)	Kết quả kì vọng

SC_01_SAFE	40.0	50.0	SAFE

SC_02_WARN	60.0	25.0	WARNING

SC_03_DANG	80.0	15.0	DANGER

SC_04_TEST_DIST	80.0	80.0	SAFE

4.Giải thích mục đích từng kịch bản

• SC_01_SAFE: Kiểm tra khả năng giữ im lặng của hệ thống khi ở điều kiện an toàn, tránh tình trạng báo động giả.
• SC_02_WARN: kiểm tra độ nhạy tại ngưỡng biên cảnh báo. Xe đi nhanh và khoảng cách thu hẹp, cần phát tín hiệu chú ý.
• SC_03_DANG: kiểm tra phản xạ khẩn cấp. Vận tốc kèm bán đuôi sát, quỹ thời gian rất ngắn nên hệ thống phải báo động đỏ.
• SC_04_TEST_DIST: phân tích biến thiên, chứng minh khoảng cách xa giúp an toàn dù tốc độ cao.

5.Phương án sử dụng dữ liệu và So Sánh kết quả

• Cách sử dụng dữ liệu (tuần 2): Module Python sẽ đọc file Scenarios.csv, tiến hành kiểm tra tính hợp lệ, ép kiểu dữ liệu sang Float và truyền tham số trực tiếp vào hàm đánh giá suy diễn của module AI.
• Phương án so sánh: 
     • Xây dựng bảng Console Log đối chiếu 1:1 giữa cột Expected_action (kết quả mong đợi đã được thiết kế sẵn trong file CSV) và actual_action (kết quả thực tế do thuật toán AI tính toán).
   • In ra màn hình trạng thái “PASS” nếu kết quả trùng khớp hoàn toàn và “FAIL” nếu thuật toán AI trả về sự sai lệch logic.
• Công tác phối hợp với AI Developer: cần thống nhất chặt chẽ với thành viên phụ trách AI về công thức đánh giá rủi ro (dùng thời gian va chạm – TTC hay phanh khoảng cách) và các mốc ngưỡng chuyển đổi cụ thể để đảm bảo thông số trong kịch bản khớp tuyệt đối với code AI.



</details>
