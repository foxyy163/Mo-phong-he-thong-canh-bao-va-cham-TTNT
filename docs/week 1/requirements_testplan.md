# ĐẶC TẢ YÊU CẦU, PHÂN TÍCH TÁC TỬ PEAS VÀ KẾ HOẠCH KIỂM THỬ

**Issue:** `[W1-05]` Đặc tả yêu cầu và kế hoạch kiểm thử  
**Vai trò:** QA & Documentation  
**Dự án:** Mô phỏng hệ thống cảnh báo va chạm – Môn Trí Tuệ Nhân Tạo (TTNT)  
**File:** `docs/week1/requirements_testplan.md`

---

## 1. TỔNG QUAN YÊU CẦU HỆ THỐNG

### 1.1. Mục tiêu hệ thống
Hệ thống **Mô phỏng cảnh báo va chạm** được xây dựng nhằm mô phỏng cách một tác tử trí tuệ nhân tạo dựa trên luật (Rule-Based AI Agent) thu nhận dữ liệu chuyển động của phương tiện (vận tốc, khoảng cách đến vật cản phía trước), phân tích mức độ rủi ro và đưa ra quyết định cảnh báo theo 3 cấp độ: **An toàn (`SAFE`)**, **Cảnh báo (`WARNING`)** và **Nguy hiểm (`DANGER`)**.

### 1.2. Phạm vi hệ thống
* **Chức năng bắt buộc (In-Scope):**
  * Cung cấp dữ liệu đầu vào thông qua nhập liệu thủ công hoặc chọn từ danh sách kịch bản mô phỏng có sẵn.
  * Kiểm tra tính hợp lệ của dữ liệu đầu vào (Validation).
  * Đánh giá nguy cơ va chạm bằng hệ thống suy diễn luật `IF–THEN` (Rule-Based System).
  * Hiển thị trực quan trạng thái cảnh báo, màu sắc tương ứng, mã luật kích hoạt và lời giải thích trên giao diện Streamlit.
  * Hiển thị bảng so sánh kết quả giữa các kịch bản mô phỏng.
* **Chức năng mở rộng / Không bắt buộc (Out-of-Scope trong Week 1):**
  * Kết nối cảm biến phần cứng thực tế (Radar, LiDAR, Camera).
  * Huấn luyện mô hình học máy/học sâu (Machine Learning / Deep Learning).
  * Can thiệp cơ học vào hệ thống phanh hoặc vô lăng thực tế.

### 1.3. Đối tượng sử dụng
* **Giảng viên và Sinh viên:** Sử dụng hệ thống để trực quan hóa hoạt động của hệ chuyên gia / hệ dựa trên luật trong môn học Trí tuệ nhân tạo.
* **Nhóm phát triển dự án:** Sử dụng làm chuẩn tham chiếu để lập trình, tích hợp các module (`Simulation`, `AI Engine`, `Streamlit UI`) và nghiệm thu chất lượng sản phẩm.

### 1.4. Quy ước Đầu vào – Đầu ra tổng quát
* **Đầu vào (Inputs):**
  * `speed` ($v$): Tốc độ hiện tại của xe ($\text{km/h}$), kiểu số thực (`float`), giá trị hợp lệ $0 \le v \le 200$.
  * `distance` ($d$): Khoảng cách từ xe đến vật cản phía trước ($\text{m}$), kiểu số thực (`float`), giá trị hợp lệ $0 \le d \le 500$.
  * `scenario_id`: Mã kịch bản mô phỏng (nếu chọn chế độ chạy theo kịch bản).
* **Đầu ra (Outputs):**
  * `status`: Mức cảnh báo (`SAFE` | `WARNING` | `DANGER` | `INVALID_INPUT`).
  * `rule_id`: Mã luật AI được kích hoạt (ví dụ: `R01`, `R02`, ...).
  * `explanation`: Chuỗi văn bản giải thích nguyên nhân đưa ra mức cảnh báo.
  * `ui_color`: Mã màu hiển thị trên giao diện (Xanh lá `#28a745` / Vàng `#ffc107` / Đỏ `#dc3545`).

---

## 2. ĐẶC TẢ YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

| Mã YC | Tên chức năng | Đầu vào (Input) | Xử lý (Process) | Đầu ra (Output) | Cách kiểm tra (Verification) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-01** | Nhập thông số thủ công | Người dùng nhập `speed` ($\text{km/h}$) và `distance` ($\text{m}$) trên giao diện Streamlit. | Thu nhận giá trị từ các widget nhập liệu và chuyển thành cấu trúc dữ liệu chuẩn. | Dictionary chứa cặp giá trị `{"speed": v, "distance": d}`. | Kiểm tra giao diện nhận đúng số thực/số nguyên người dùng nhập vào. |
| **FR-02** | Chọn kịch bản mô phỏng | Người dùng chọn 1 kịch bản từ danh sách (`scenario_id`). | Truy xuất thông số `speed` và `distance` tương ứng từ module Simulation. | Thông số của kịch bản được nạp tự động vào hệ thống. | Chọn thử từng kịch bản (An toàn, Cảnh báo, Nguy hiểm) và đối chiếu thông số hiển thị. |
| **FR-03** | Kiểm tra dữ liệu đầu vào (Validation) | Cặp giá trị `(speed, distance)` từ FR-01 hoặc FR-02. | Kiểm tra kiểu dữ liệu số, kiểm tra không rỗng (`not None`) và điều kiện $0 \le v \le 200$, $0 \le d \le 500$. | Trả về `True` nếu hợp lệ; trả về `False` kèm thông báo lỗi nếu vi phạm. | Nhập số âm, chữ cái, giá trị rỗng hoặc vượt ngưỡng để xem hệ thống có chặn lại không. |
| **FR-04** | Suy diễn mức cảnh báo bằng luật AI | Dữ liệu `(speed, distance)` đã qua bước Validation. | Đối chiếu tuần tự theo độ ưu tiên với tập luật `IF–THEN` trong Knowledge Base (tính ngưỡng khoảng cách an toàn theo vận tốc). | Trạng thái cảnh báo chính xác: `SAFE`, `WARNING`, hoặc `DANGER` kèm `rule_id`. | Chạy bộ Unit Test phủ kín cả 3 vùng và các giá trị biên (Boundary cases). |
| **FR-05** | Giải thích kết quả suy diễn | Kết quả từ FR-04 (`status`, `rule_id`, `speed`, `distance`). | Sinh câu giải thích tường minh dựa trên mã luật được kích hoạt và ngưỡng an toàn tương ứng. | Chuỗi `explanation` mô tả rõ vì sao hệ thống đưa ra cảnh báo đó. | Kiểm tra mỗi mức cảnh báo đều xuất hiện văn bản giải thích khớp với điều kiện luật. |
| **FR-06** | Hiển thị kết quả và so sánh kịch bản | Kết quả đầu ra từ module AI (`status`, `explanation`, danh sách kịch bản). | Render thẻ trạng thái theo màu sắc quy ước (Xanh/Vàng/Đỏ) và lập bảng tổng hợp so sánh các kịch bản trên Streamlit. | Giao diện hiển thị trực quan trạng thái, thông số đầu vào và bảng đối chiếu. | Quan sát trực tiếp trên trình duyệt khi chạy ứng dụng Streamlit. |

---

## 3. ĐẶC TẢ YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS)

| Mã YC | Nhóm yêu cầu | Mô tả chi tiết | Tiêu chí đo lường / Nghiệm thu |
| :--- | :--- | :--- | :--- |
| **NFR-01** | Tính dễ sử dụng (Usability) | Giao diện thiết kế trên một trang (Single-page), có ghi rõ đơn vị đo ($\text{km/h}$, $\text{m}$), phân biệt 3 mức cảnh báo bằng màu sắc trực quan và chữ in hoa rõ ràng. | Người dùng mới có thể thao tác chạy mô phỏng trong vòng $< 30\text{ giây}$ mà không cần đọc tài liệu phức tạp. |
| **NFR-02** | Độ ổn định & Xử lý lỗi (Reliability) | Hệ thống hoạt động ổn định, không bị dừng đột ngột (Crash / Traceback error trên màn hình) khi nhận dữ liệu sai định dạng, số âm hoặc chia cho $0$. | $100\%$ các ca kiểm thử dữ liệu bất thường đều được bắt lỗi êm (Graceful error handling) và hiển thị cảnh báo thân thiện. |
| **NFR-03** | Hiệu năng phản hồi (Performance) | Quá trình suy diễn luật AI và cập nhật giao diện phải diễn ra tức thời. | Thời gian xử lý từ lúc nhấn nút đến khi hiển thị kết quả $< 200\text{ ms}$. |
| **NFR-04** | Tính mô-đun hóa & Dễ bảo trì (Maintainability) | Mã nguồn được tách biệt rõ ràng thành các module độc lập: `simulation` (dữ liệu), `ai_rules` (bộ suy diễn), và `ui` (giao diện). | Có thể thay đổi ngưỡng trong module `ai_rules` mà không phải sửa code của `ui`. |
| **NFR-05** | Khả năng kiểm thử (Testability) | Module AI nhận đầu vào và trả đầu ra qua hàm Python thuần túy (Dictionary/JSON), tách rời khỏi giao diện Streamlit. | QA có thể chạy kịch bản kiểm thử tự động (Unit Test) độc lập cho hàm suy diễn AI. |

---

## 4. PHÂN TÍCH TÁC TỬ THÔNG MINH THEO MÔ HÌNH PEAS

### 4.1. Bản chất tác tử trong hệ thống
Hệ thống cảnh báo va chạm đóng vai trò là một **Tác tử phản xạ dựa trên luật (Rule-Based Reflex Agent)**. Tác tử liên tục nhận thông tin trạng thái từ môi trường mô phỏng, đối chiếu với cơ sở tri thức (Knowledge Base) chứa các luật `IF–THEN` và phát ra hành động cảnh báo tương ứng nhằm đảm bảo an toàn.

### 4.2. Bảng phân tích PEAS

| Thành phần PEAS | Mô tả trong bài toán Cảnh báo va chạm | Hiện thực hóa trong phần mềm mô phỏng |
| :--- | :--- | :--- |
| **P – Performance Measure**<br>*(Độ đo hiệu quả)* | - Phân loại chính xác $100\%$ mức độ nguy hiểm (`SAFE`, `WARNING`, `DANGER`).<br>- Không bỏ sót bất kỳ tình huống nguy hiểm nào (Zero False Negatives).<br>- Hạn chế tối đa cảnh báo giả gây nhiễu (False Positives).<br>- Đưa ra lời giải thích rõ ràng, phản hồi tức thời. | Đối chiếu kết quả của hàm suy diễn AI với bảng Test Case chuẩn; đo thời gian phản hồi và tính hợp lý của thông điệp giải thích. |
| **E – Environment**<br>*(Môi trường)* | Không gian giao thông gồm: xe chính (Ego Vehicle) đang di chuyển trên làn đường, xe/vật cản phía trước (Obstacle) và khoảng cách vật lý giữa hai thực thể. | Môi trường giả lập thông qua các kịch bản dữ liệu tĩnh/theo bước thời gian và không gian tương tác trên ứng dụng Streamlit. |
| **A – Actuators**<br>*(Bộ chấp hành)* | Màn hình hiển thị HUD trên taplo xe, đèn báo hiệu màu sắc, còi cảnh báo âm thanh nhắc nhở tài xế giảm tốc/phanh. | Các thành phần hiển thị trên giao diện Streamlit: Hộp trạng thái đổi màu (Xanh/Vàng/Đỏ), văn bản cảnh báo, mã luật và bảng so sánh. |
| **S – Sensors**<br>*(Cảm biến)* | Cảm biến đo vận tốc xe (Speedometer) và cảm biến đo khoảng cách phía trước (Radar / LiDAR / Camera). | Được mô phỏng bằng dữ liệu số `(speed, distance)` lấy từ thanh trượt/ô nhập liệu của người dùng hoặc đọc từ file kịch bản (`JSON`/`CSV`). |

### 4.3. Các yêu cầu hệ thống rút ra từ phân tích PEAS
1. **Từ Sensors:** Vì dữ liệu cảm biến được mô phỏng qua nhập liệu hoặc file, hệ thống bắt buộc phải có **bộ lọc kiểm tra dữ liệu đầu vào (FR-03)** để loại bỏ các giá trị phi vật lý (như tốc độ âm, khoảng cách âm) trước khi đưa vào bộ suy diễn.
2. **Từ Performance Measure:** Để không bỏ sót nguy cơ va chạm, **bộ luật suy diễn (FR-04)** phải ưu tiên kiểm tra mức độ nghiêm trọng cao nhất trước (`DANGER` $\rightarrow$ `WARNING` $\rightarrow$ `SAFE`) và xử lý triệt để các điểm biên (ví dụ: $v = 0$ hoặc $d = 0$).
3. **Từ Actuators:** Đầu ra của tác tử không chỉ có nhãn trạng thái mà phải kèm theo **giải thích nguyên nhân (FR-05)** và **hiển thị trực quan (FR-06)** để người điều khiển hiểu và tin tưởng quyết định của AI.

---

## 5. KẾ HOẠCH KIỂM THỬ (TEST PLAN)

### 5.1. Mục tiêu và Phạm vi kiểm thử
* Đảm bảo từng module (`Simulation`, `AI Engine`, `UI`) hoạt động đúng thiết kế trước khi ghép nối trong Week 2.
* Kiểm chứng tính nhất quán và đầy đủ của bộ luật `IF–THEN` (bao phủ cả 3 mức `SAFE`, `WARNING`, `DANGER`).
* Đảm bảo hệ thống xử lý an toàn mọi trường hợp biên (Boundary cases) và dữ liệu lỗi (Invalid inputs).

### 5.2. Các cấp độ kiểm thử
1. **Kiểm thử đơn vị (Unit Testing):**
   * **Đối tượng:** Hàm kiểm tra dữ liệu `validate_input(speed, distance)` và hàm suy diễn AI `evaluate_collision_risk(speed, distance)` (kết hợp với W1-02), hàm tải kịch bản `load_scenarios()` (kết hợp với W1-03).
   * **Phương pháp:** Gọi trực tiếp hàm Python với các bộ tham số đầu vào trong bảng Test Case và kiểm tra giá trị trả về.
2. **Kiểm thử tích hợp (Integration Testing):**
   * **Đối tượng:** Luồng truyền dữ liệu từ Giao diện (`UI` - W1-04) $\leftrightarrow$ Kịch bản (`Simulation` - W1-03) $\leftrightarrow$ Bộ luật (`AI` - W1-02).
   * **Phương pháp:** Chọn kịch bản hoặc nhập số trên giao diện Streamlit, nhấn nút chạy và kiểm tra kết quả hiển thị cuối cùng trên màn hình.

### 5.3. Quy ước ngưỡng tham chiếu để thiết kế Test Case (Phối hợp với W1-02)
Để đảm bảo tính nhất quán khi kiểm thử, kế hoạch kiểm thử sử dụng mô hình ngưỡng khoảng cách phụ thuộc vận tốc (hoặc Thời gian tới va chạm $TTC$ / Khoảng cách an toàn theo quy tắc 3 giây):
* Gọi vận tốc đổi sang $\text{m/s}$ là $v_{ms} = \frac{\text{speed}}{3.6}$.
* **Khoảng cách nguy hiểm ($d_{danger}$):** Khoảng cách xe đi được trong $1.5\text{ giây}$ ($d_{danger} = 1.5 \times v_{ms}$, tối thiểu $5\text{ m}$ khi xe đang chạy). Nếu $d \le d_{danger} \rightarrow$ **`DANGER`**.
* **Khoảng cách cảnh báo ($d_{warning}$):** Khoảng cách xe đi được trong $3.0\text{ giây}$ ($d_{warning} = 3.0 \times v_{ms}$, tối thiểu $15\text{ m}$ khi xe đang chạy). Nếu $d_{danger} < d \le d_{warning} \rightarrow$ **`WARNING`**.
* **Khoảng cách an toàn:** Nếu $d > d_{warning}$ (hoặc $v = 0$ và $d > 0$) $\rightarrow$ **`SAFE`**.

*(Lưu ý: Khi thành viên phụ trách W1-02 chốt bảng hằng số ngưỡng cuối cùng, các giá trị biên trong bảng Test Case dưới đây sẽ được căn chỉnh khớp chính xác với `warning_rules.md`).*

---

## 6. BẢNG THIẾT KẾ TEST CASE CHI TIẾT

Bảng dưới đây bao gồm **12 Test Cases** bao phủ đầy đủ: các ca chuẩn (Normal), các ca biên (Boundary) và các ca dữ liệu lỗi (Abnormal/Invalid).

| Mã TC | Mục đích kiểm thử | Phân loại | Đầu vào (`speed`, `distance`) | Kết quả mong đợi (Expected Output) | Module kiểm thử | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Kiểm thử trạng thái **An toàn (`SAFE`)** ở tốc độ trung bình, khoảng cách xa | Normal | `speed = 60` ($\text{km/h}$)<br>`distance = 80` ($\text{m}$) | - `status`: **`SAFE`**<br>- Hiển thị màu Xanh lá, giải thích khoảng cách hiện tại ($80\text{ m}$) lớn hơn ngưỡng an toàn ($50\text{ m}$). | AI Engine & UI | Pending |
| **TC-02** | Kiểm thử trạng thái **Cảnh báo (`WARNING`)** khi khoảng cách thu hẹp | Normal | `speed = 60` ($\text{km/h}$)<br>`distance = 35` ($\text{m}$) | - `status`: **`WARNING`**<br>- Hiển thị màu Vàng, nhắc nhở người lái giảm tốc độ và giữ khoảng cách. | AI Engine & UI | Pending |
| **TC-03** | Kiểm thử trạng thái **Nguy hiểm (`DANGER`)** khi bám đuôi quá gần ở tốc độ cao | Normal | `speed = 80` ($\text{km/h}$)<br>`distance = 15` ($\text{m}$) | - `status`: **`DANGER`**<br>- Hiển thị màu Đỏ, cảnh báo nguy cơ va chạm tức thời và yêu cầu phanh khẩn cấp. | AI Engine & UI | Pending |
| **TC-04** | Kiểm thử cùng khoảng cách ($30\text{ m}$) nhưng tốc độ thấp $\rightarrow$ An toàn | Normal | `speed = 20` ($\text{km/h}$)<br>`distance = 30` ($\text{m}$) | - `status`: **`SAFE`**<br>- Chứng minh bộ luật có xét đến yếu tố tốc độ thấp ($d_{warning} \approx 16.7\text{ m} < 30\text{ m}$). | AI Engine | Pending |
| **TC-05** | Kiểm thử trường hợp biên: **Xe đang đứng yên ($v = 0\text{ km/h}$)** và cách vật cản $5\text{ m}$ | Boundary | `speed = 0` ($\text{km/h}$)<br>`distance = 5` ($\text{m}$) | - `status`: **`SAFE`**<br>- Không phát sinh lỗi chia cho $0$ (`ZeroDivisionError`), giải thích xe đang đứng yên. | AI Engine | Pending |
| **TC-06** | Kiểm thử trường hợp biên: **Khoảng cách bằng $0\text{ m}$ ($d = 0\text{ m}$)** (Đã chạm vật cản) | Boundary | `speed = 10` ($\text{km/h}$)<br>`distance = 0` ($\text{m}$) | - `status`: **`DANGER`**<br>- Cảnh báo va chạm ngay lập tức vì khoảng cách bằng $0$. | AI Engine | Pending |
| **TC-07** | Kiểm thử giá trị ngay tại biên giữa `WARNING` và `DANGER` (với $v = 72\text{ km/h} = 20\text{ m/s}$, ngưỡng $1.5\text{s}$ là $30\text{ m}$) | Boundary | `speed = 72` ($\text{km/h}$)<br>`distance = 30` ($\text{m}$) | - `status`: **`DANGER`** (ưu tiên mức an toàn cao hơn tại điểm biên $d \le 30\text{ m}$). | AI Engine | Pending |
| **TC-08** | Kiểm thử giá trị ngay tại biên giữa `SAFE` và `WARNING` (với $v = 72\text{ km/h} = 20\text{ m/s}$, ngưỡng $3.0\text{s}$ là $60\text{ m}$) | Boundary | `speed = 72` ($\text{km/h}$)<br>`distance = 60` ($\text{m}$) | - `status`: **`WARNING`** (tại điểm biên $d \le 60\text{ m}$ hệ thống kích hoạt cảnh báo sớm). | AI Engine | Pending |
| **TC-09** | Kiểm thử nhập **tốc độ âm** | Invalid / Error | `speed = -20` ($\text{km/h}$)<br>`distance = 40` ($\text{m}$) | - `status`: **`INVALID_INPUT`**<br>- Chặn suy diễn, hiển thị thông báo lỗi: *"Tốc độ không được nhỏ hơn 0"*. | Validation & UI | Pending |
| **TC-10** | Kiểm thử nhập **khoảng cách âm** | Invalid / Error | `speed = 50` ($\text{km/h}$)<br>`distance = -10` ($\text{m}$) | - `status`: **`INVALID_INPUT`**<br>- Chặn suy diễn, hiển thị thông báo lỗi: *"Khoảng cách không được nhỏ hơn 0"*. | Validation & UI | Pending |
| **TC-11** | Kiểm thử dữ liệu **bị bỏ trống (`None`) hoặc sai kiểu dữ liệu (chữ cái)** | Invalid / Error | `speed = "abc"`<br>`distance = None` | - `status`: **`INVALID_INPUT`**<br>- Không bị văng lỗi hệ thống (Crash), hiển thị yêu cầu nhập số hợp lệ. | Validation & UI | Pending |
| **TC-12** | Kiểm thử tích hợp tải và so sánh 3 kịch bản mẫu từ module Simulation | Integration | Chọn lần lượt `SC01` (Safe), `SC02` (Warning), `SC03` (Danger) | - Dữ liệu nạp đúng lên UI, kết quả khớp 3 mức cảnh báo và hiển thị đầy đủ trên bảng so sánh. | Simulation + AI + UI | Pending |

---

## 7. TIÊU CHÍ ĐÁNH GIÁ PASS / FAIL VÀ NGHIỆM THU

### 7.1. Tiêu chí đánh giá từng Test Case
* **Đạt (`PASS`):**
  * Đầu ra thực tế (`Actual Output`) khớp chính xác với kết quả mong đợi (`Expected Output`) về cả nhãn trạng thái (`SAFE` / `WARNING` / `DANGER` / `INVALID_INPUT`), màu sắc hiển thị và nội dung giải thích.
  * Chương trình thực thi mượt mà, không xuất hiện lỗi ngoại lệ (Exception/Traceback) trên giao diện hoặc terminal.
* **Không đạt (`FAIL`):**
  * Trả về sai mức độ cảnh báo so với bộ luật quy định (đặc biệt là lỗi đánh giá nhầm `DANGER` thành `SAFE` hoặc `WARNING`).
  * Không chặn được dữ liệu âm, dữ liệu rỗng hoặc để xảy ra lỗi chia cho $0$ khi $v = 0$.
  * Giao diện hiển thị sai màu sắc quy ước hoặc thiếu thông điệp giải thích.

### 7.2. Điều kiện nghiệm thu toàn hệ thống (Sign-off Criteria cho Week 2)
* $100\%$ các Test Case thuộc nhóm **Normal** và **Boundary** (`TC-01` đến `TC-08`) phải đạt trạng thái **PASS**.
* $100\%$ các Test Case thuộc nhóm **Invalid / Error** (`TC-09` đến `TC-11`) được xử lý an toàn, đạt trạng thái **PASS**.
* Kiểm thử tích hợp luồng kịch bản (`TC-12`) hoạt động thông suốt giữa 3 module `Simulation` – `AI` – `UI`.

---

## 8. CHECKLIST HOÀN THÀNH

- [x] Đã xác định phạm vi yêu cầu.
- [x] Đã lập bảng yêu cầu chức năng.
- [x] Đã lập bảng yêu cầu phi chức năng.
- [x] Đã phân tích PEAS.
- [x] Đã xây dựng kế hoạch kiểm thử.
- [x] Đã viết tối thiểu 8 test case (đã thiết kế 12 test case).
- [x] Đã hoàn thiện `requirements_testplan.md`.
