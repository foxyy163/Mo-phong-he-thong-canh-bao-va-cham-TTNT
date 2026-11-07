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

