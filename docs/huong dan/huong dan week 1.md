
# HƯỚNG DẪN THỰC HIỆN ISSUES – WEEK 1

**Dự án:** Mô phỏng hệ thống cảnh báo va chạm  
**Môn học:** Trí tuệ nhân tạo (TTNT)  
**Thời gian:** 04/11/2026 – 10/11/2026  
**Hình thức:** Tự nghiên cứu, phân tích và hoàn thiện tài liệu Markdown.

---

## 1. GIỚI THIỆU

Tài liệu này cung cấp các câu hỏi định hướng giúp thành viên tự nghiên cứu và hoàn thành công việc được giao trong Week 1.

Mỗi thành viên tự chọn một GitHub Issue và thực hiện phần việc tương ứng.

**Yêu cầu chung:**

- Chủ động tìm hiểu kiến thức liên quan.
- Ưu tiên tài liệu môn học và yêu cầu đề tài.
- Trả lời các câu hỏi bằng cách hiểu của bản thân.
- Có giải thích, bảng biểu, sơ đồ hoặc ví dụ khi cần.
- Không chỉ liệt kê câu trả lời ngắn mà cần phân tích phù hợp.
- Trao đổi với thành viên khác khi nội dung liên quan.
- Không cần viết code hoàn chỉnh trong Week 1.

**Lưu ý:** Các câu hỏi dưới đây là gợi ý nghiên cứu, không phải mẫu đáp án. Thành viên có thể bổ sung nội dung nếu cần thiết.

---

# ISSUE W1-01: THIẾT KẾ KIẾN TRÚC HỆ THỐNG

**Vai trò:** System Architecture & Integration  
**Mức độ:** Trung bình  
**File nộp:** `docs/week1/architecture.md`

## A. Tìm hiểu tổng quan

1. Hệ thống cảnh báo va chạm được xây dựng nhằm giải quyết vấn đề gì?
2. Để mô phỏng hoạt động của hệ thống, chương trình cần những thành phần nào?
3. Các thành phần đó có nhiệm vụ gì?
4. Vì sao cần chia chương trình thành nhiều module thay vì viết toàn bộ trong một file?
5. Với phạm vi đề tài hiện tại, kiến trúc nào sẽ phù hợp và dễ phát triển nhất?

## B. Phân tích kiến trúc

6. Giao diện người dùng sẽ tương tác với những module nào?
7. Module mô phỏng dữ liệu có nhiệm vụ gì?
8. Module xử lý AI có vai trò gì trong việc đánh giá nguy cơ?
9. Dữ liệu được truyền giữa các module theo trình tự nào?
10. Khi một module xảy ra lỗi, hệ thống nên xử lý như thế nào?

## C. Thiết kế dữ liệu

11. Hệ thống cần nhận những dữ liệu đầu vào nào?
12. Đơn vị đo và kiểu dữ liệu của từng đầu vào là gì?
13. Kết quả đầu ra cần bao gồm những thông tin nào?
14. Nên biểu diễn kết quả dưới dạng dữ liệu nào để dễ sử dụng giữa các module?
15. Làm thế nào để các thành viên lập trình riêng nhưng vẫn kết nối được code?

## D. Thiết kế sơ đồ

16. Có thể biểu diễn kiến trúc chương trình bằng sơ đồ nào?
17. Trong sơ đồ, những thành phần nào cần kết nối trực tiếp?
18. Luồng dữ liệu đi từ người dùng đến kết quả cuối cùng như thế nào?

## E. Yêu cầu sản phẩm

Sau khi nghiên cứu và trả lời các câu hỏi, hãy tổng hợp thành tài liệu gồm:

- Giới thiệu kiến trúc.
- Danh sách module và chức năng.
- Sơ đồ kiến trúc hệ thống.
- Luồng xử lý dữ liệu.
- Bảng quy ước đầu vào và đầu ra.
- Phương án tích hợp module trong Week 2.

### Checklist hoàn thành

- [ ] Đã phân tích các thành phần hệ thống.
- [ ] Đã xây dựng sơ đồ kiến trúc.
- [ ] Đã mô tả chức năng từng module.
- [ ] Đã thống nhất quy ước dữ liệu với các thành viên liên quan.
- [ ] Đã hoàn thiện `architecture.md`.

---

# ISSUE W1-02: THIẾT KẾ BỘ LUẬT CẢNH BÁO AI

**Vai trò:** AI Developer  
**Mức độ:** Trung bình  
**File nộp:** `docs/week1/warning_rules.md`

## A. Tìm hiểu lý thuyết AI

1. Hệ thống dựa trên luật (Rule-Based System) là gì?
2. Luật IF–THEN hoạt động như thế nào?
3. Cơ sở tri thức (Knowledge Base) có vai trò gì?
4. Suy diễn trong AI là gì?
5. Vì sao có thể áp dụng hệ thống luật vào bài toán cảnh báo va chạm?
6. Hệ thống này có cần huấn luyện dữ liệu như Machine Learning không? Vì sao?

## B. Phân tích bài toán

7. Những yếu tố nào ảnh hưởng đến nguy cơ va chạm?
8. Trong phạm vi đề tài, cần sử dụng những yếu tố nào?
9. Tốc độ xe ảnh hưởng đến khoảng cách an toàn như thế nào?
10. Nếu hai tình huống có cùng khoảng cách nhưng tốc độ khác nhau, mức cảnh báo có thể khác nhau không?
11. Cần đưa ra những giả định nào để đơn giản hóa bài toán?

## C. Thiết kế bộ luật

12. Làm thế nào để xác định mức An toàn (SAFE)?
13. Khi nào hệ thống nên đưa ra mức Cảnh báo (WARNING)?
14. Khi nào hệ thống nên đưa ra mức Nguy hiểm (DANGER)?
15. Các ngưỡng cảnh báo sẽ được xác định dựa trên cơ sở nào?
16. Nên sử dụng ngưỡng cố định hay ngưỡng thay đổi theo tốc độ?
17. Nếu nhiều điều kiện cùng đúng, hệ thống cần ưu tiên kết quả nào?
18. Làm thế nào để tránh các luật mâu thuẫn hoặc bỏ sót trường hợp?

## D. Giải thích kết quả

19. Làm thế nào để người dùng hiểu vì sao hệ thống đưa ra cảnh báo?
20. Có nên gán mã riêng cho từng luật không? Vì sao?
21. Nếu đầu vào không hợp lệ, hệ thống cần phản hồi như thế nào?

## E. Kiểm chứng bộ luật

22. Làm thế nào để kiểm tra đủ cả ba mức cảnh báo?
23. Những trường hợp biên nào cần được kiểm tra?
24. Có tình huống nào hai luật cùng được kích hoạt không?
25. Làm thế nào để chứng minh các luật hoạt động nhất quán?

## F. Yêu cầu sản phẩm

Tổng hợp kết quả nghiên cứu thành:

- Giới thiệu Rule-Based System.
- Xác định các biến đầu vào.
- Giải thích phương pháp xây dựng ngưỡng.
- Bảng luật IF–THEN.
- Quy tắc ưu tiên khi suy diễn.
- Sơ đồ hoặc mô tả quy trình suy diễn.
- Tối thiểu 6 ví dụ minh họa.

**Lưu ý:** Các ngưỡng cảnh báo chỉ phục vụ mô phỏng học tập, không được coi là tiêu chuẩn an toàn để điều khiển xe thực tế.

### Checklist hoàn thành

- [ ] Đã nghiên cứu cơ sở lý thuyết.
- [ ] Đã xác định đầu vào và giả định.
- [ ] Đã xây dựng các luật cảnh báo.
- [ ] Đã giải thích cách suy diễn.
- [ ] Đã có ví dụ kiểm chứng.
- [ ] Đã hoàn thiện `warning_rules.md`.

---

# ISSUE W1-03: THIẾT KẾ DỮ LIỆU VÀ KỊCH BẢN MÔ PHỎNG

**Vai trò:** Simulation Developer  
**Mức độ:** Dễ  
**File nộp:** `docs/week1/simulation_scenarios.md`

## A. Tìm hiểu bài toán mô phỏng

1. Mô phỏng dữ liệu cảm biến có ý nghĩa gì trong dự án?
2. Tại sao không cần sử dụng cảm biến thật?
3. Những dữ liệu nào cần được mô phỏng?
4. Đơn vị đo của từng dữ liệu là gì?
5. Giá trị hợp lệ của tốc độ và khoảng cách cần được quy định như thế nào?

## B. Xây dựng kịch bản

6. Một tình huống mô phỏng cần có những thông tin nào?
7. Làm thế nào để xây dựng tình huống an toàn?
8. Làm thế nào để xây dựng tình huống cần cảnh báo?
9. Làm thế nào để xây dựng tình huống nguy hiểm?
10. Ba tình huống nên khác nhau ở những yếu tố nào?
11. Nếu cùng tốc độ nhưng khoảng cách khác nhau, kết quả dự kiến thay đổi ra sao?
12. Nếu cùng khoảng cách nhưng tốc độ khác nhau, kết quả dự kiến thay đổi ra sao?

## C. Thiết kế dữ liệu

13. Nên lưu dữ liệu mô phỏng dưới dạng CSV, JSON hay danh sách Python?
14. Mỗi dòng dữ liệu nên chứa những cột nào?
15. Làm thế nào để đặt tên kịch bản rõ ràng?
16. Có cần lưu mã kịch bản để phân biệt không?
17. Làm thế nào để bảo đảm dữ liệu mô phỏng có thể sử dụng trực tiếp cho module AI?

## D. Thiết kế quá trình mô phỏng

18. Mỗi kịch bản chỉ cần một bộ dữ liệu hay nên có nhiều bước thời gian?
19. Nếu mô phỏng nhiều bước, tốc độ và khoảng cách sẽ thay đổi theo quy tắc nào?
20. Hệ thống nên kiểm tra dữ liệu đầu vào trước khi đánh giá như thế nào?
21. Nếu có dữ liệu âm hoặc bị thiếu thì xử lý ra sao?

## E. Đánh giá kết quả

22. Làm thế nào để so sánh kết quả giữa ba kịch bản?
23. Những thông tin nào cần đưa vào bảng so sánh?
24. Kết quả dự kiến có phù hợp với bộ luật AI không?
25. Cần trao đổi với thành viên phụ trách AI những nội dung gì trước khi chốt dữ liệu?

## F. Yêu cầu sản phẩm

Tổng hợp kết quả thành tài liệu gồm:

- Mô tả dữ liệu mô phỏng.
- Giả định môi trường.
- Cấu trúc dữ liệu dự kiến.
- Ít nhất 3 kịch bản cụ thể.
- Bảng tốc độ và khoảng cách.
- Giải thích mục đích từng kịch bản.
- Cách sử dụng dữ liệu cho Week 2.
- Phương án so sánh kết quả.

### Checklist hoàn thành

- [ ] Đã xác định cấu trúc dữ liệu.
- [ ] Đã xây dựng tối thiểu 3 kịch bản.
- [ ] Đã mô tả giả định mô phỏng.
- [ ] Đã thống nhất với người phụ trách AI.
- [ ] Đã chuẩn bị phương án so sánh kết quả.
- [ ] Đã hoàn thiện `simulation_scenarios.md`.

---

# ISSUE W1-04: THIẾT KẾ GIAO DIỆN STREAMLIT

**Vai trò:** UI Developer  
**Mức độ:** Dễ  
**File nộp:** `docs/week1/ui_design.md`

## A. Tìm hiểu giao diện

1. Streamlit là gì?
2. Vì sao Streamlit phù hợp với dự án mô phỏng bằng Python?
3. Người dùng cần thực hiện những thao tác nào với hệ thống?
4. Giao diện một trang có đủ đáp ứng yêu cầu không?
5. Những thông tin nào cần xuất hiện trên màn hình chính?

## B. Thiết kế khu vực nhập dữ liệu

6. Người dùng nhập tốc độ và khoảng cách bằng cách nào?
7. Có nên sử dụng ô nhập số hay thanh trượt?
8. Cần hiển thị đơn vị đo ở vị trí nào?
9. Người dùng sẽ chọn kịch bản có sẵn bằng thành phần giao diện nào?
10. Khi nào nút chạy mô phỏng được phép hoạt động?

## C. Thiết kế hiển thị kết quả

11. Làm thế nào để hiển thị rõ ba mức cảnh báo?
12. Màu sắc nên được sử dụng như thế nào?
13. Có cần hiển thị tên trạng thái bằng chữ không?
14. Phần giải thích kết quả nên đặt ở đâu?
15. Có nên hiển thị tốc độ và khoảng cách cùng với kết quả không?
16. Có cần biểu đồ hoặc bảng so sánh các kịch bản không?

## D. Thiết kế trải nghiệm người dùng

17. Nếu người dùng nhập tốc độ âm, giao diện phản hồi như thế nào?
18. Nếu khoảng cách không hợp lệ, hệ thống hiển thị thông báo gì?
19. Người dùng có cần hướng dẫn sử dụng ngay trên màn hình không?
20. Làm thế nào để giao diện đơn giản và dễ thuyết trình?

## E. Phác thảo giao diện

21. Giao diện cần được chia thành những khu vực nào?
22. Vị trí của biểu mẫu nhập liệu và kết quả nên được bố trí ra sao?
23. Có thể thiết kế bản phác thảo bằng công cụ nào?
24. Bản phác thảo có thể hiện đầy đủ luồng thao tác của người dùng không?

## F. Yêu cầu sản phẩm

Tài liệu cần có:

- Mục tiêu thiết kế.
- Danh sách thành phần giao diện.
- Bản phác thảo (wireframe).
- Luồng thao tác của người dùng.
- Mô tả các trạng thái cảnh báo.
- Phương án xử lý nhập liệu không hợp lệ.
- Danh sách thành phần Streamlit dự kiến sử dụng.

Có thể sử dụng Canva, Figma hoặc draw.io để thiết kế hình minh họa.

Lưu ảnh vào `docs/week1/assets/` và chèn đường dẫn vào Markdown.

### Checklist hoàn thành

- [ ] Đã xác định chức năng giao diện.
- [ ] Đã thiết kế wireframe.
- [ ] Đã mô tả các thành phần.
- [ ] Đã thiết kế ba trạng thái cảnh báo.
- [ ] Đã mô tả xử lý dữ liệu sai.
- [ ] Đã hoàn thiện `ui_design.md`.

---

# ISSUE W1-05: ĐẶC TẢ YÊU CẦU VÀ KẾ HOẠCH KIỂM THỬ

**Vai trò:** QA & Documentation  
**Mức độ:** Dễ – Trung bình  
**File nộp:** `docs/week1/requirements_testplan.md`

## A. Phân tích yêu cầu

1. Mục tiêu chính của hệ thống cảnh báo va chạm là gì?
2. Theo đề tài, hệ thống bắt buộc phải thực hiện những chức năng nào?
3. Những chức năng nào chỉ là mở rộng, không bắt buộc?
4. Đầu vào và đầu ra của hệ thống là gì?
5. Đối tượng sử dụng hệ thống là ai?
6. Những trường hợp nào chương trình cần xử lý?

## B. Đặc tả yêu cầu chức năng

7. Yêu cầu chức năng (Functional Requirement) là gì?
8. Hệ thống cần những yêu cầu chức năng nào?
9. Nên đánh mã yêu cầu như thế nào để dễ theo dõi?
10. Mỗi chức năng cần có mô tả đầu vào, xử lý và đầu ra ra sao?
11. Làm thế nào để kiểm tra một chức năng đã được thực hiện đúng?

## C. Đặc tả yêu cầu phi chức năng

12. Yêu cầu phi chức năng (Non-Functional Requirement) là gì?
13. Chương trình cần đáp ứng những yêu cầu nào về tính dễ sử dụng?
14. Hệ thống cần hoạt động ổn định trong những điều kiện nào?
15. Tính dễ bảo trì và khả năng kiểm thử thể hiện ở đâu?

## D. Phân tích tác tử thông minh

16. Tác tử thông minh (Intelligent Agent) là gì?
17. Hệ thống cảnh báo va chạm có thể được mô tả như một tác tử không? Vì sao?
18. PEAS là gì?
19. Performance Measure trong hệ thống này là gì?
20. Environment bao gồm những thành phần nào?
21. Actuators của hệ thống là gì?
22. Sensors được mô phỏng bằng dữ liệu nào?
23. Từ bảng PEAS, có thể rút ra những yêu cầu nào cho chương trình?

## E. Xây dựng kế hoạch kiểm thử

24. Vì sao cần kiểm thử trước khi tích hợp chương trình?
25. Những module nào cần được kiểm thử?
26. Unit Test và Integration Test khác nhau như thế nào?
27. Một test case cần có những trường thông tin nào?
28. Làm thế nào để xác định kết quả mong đợi của một test case?
29. Điều kiện nào để đánh giá một test case là Pass hoặc Fail?

## F. Thiết kế test case

30. Làm thế nào để kiểm thử ba mức SAFE, WARNING và DANGER?
31. Cần kiểm tra trường hợp tốc độ bằng 0 không?
32. Nếu người dùng nhập số âm thì hệ thống nên phản hồi ra sao?
33. Cần kiểm thử các giá trị tại ngưỡng cảnh báo như thế nào?
34. Nếu dữ liệu bị thiếu hoặc sai định dạng thì xử lý thế nào?
35. Làm thế nào để đảm bảo test case phù hợp với bộ luật của W1-02?

## G. Yêu cầu sản phẩm

Tài liệu cần có:

- Tổng quan yêu cầu hệ thống.
- Bảng yêu cầu chức năng.
- Bảng yêu cầu phi chức năng.
- Phân tích PEAS.
- Kế hoạch kiểm thử.
- Bảng tối thiểu 8 test case.
- Tiêu chí đánh giá Pass / Fail.

### Checklist hoàn thành

- [ ] Đã xác định phạm vi yêu cầu.
- [ ] Đã lập bảng yêu cầu chức năng.
- [ ] Đã lập bảng yêu cầu phi chức năng.
- [ ] Đã phân tích PEAS.
- [ ] Đã xây dựng kế hoạch kiểm thử.
- [ ] Đã viết tối thiểu 8 test case.
- [ ] Đã hoàn thiện `requirements_testplan.md`.

---
