# TV4 — Giao diện Streamlit

> **Thành viên GitHub:** [@ledan823-spec](https://github.com/ledan823-spec)  
> **Issue được giao:** [#11](https://github.com/foxyy163/Mo-phong-he-thong-canh-bao-va-cham-TTNT/issues/11)  
> **Hạn bàn giao code/giải thích:** trước 21/11/2026  
> **Trạng thái:** Đã hoàn thiện code giao diện và tài liệu giải thích trên 'main'

Đọc [README chung](../../../README.md) trước khi code. **Code chính đặt đúng file trong repo**, không sao chép bản code riêng vào thư mục này. Thư mục cá nhân này dành cho giải thích, kết quả chạy và ảnh minh họa nếu có.

## 1. Công việc của mình

- **Phần phụ trách:** Giao diện Streamlit.
- **File code thuộc trách nhiệm:** `app/main.py`.
- **Mình đã hoàn thành những gì?** Xây dựng giao diện Streamlit một trang gồm tiêu đề dự án, hai ô `number_input` cho tốc độ (`km/h`) và khoảng cách (`m`), nút đánh giá, hiển thị trạng thái `SAFE` / `WARNING` / `DANGER` kèm mã luật và lý do, bắt lỗi `ValueError` bằng `st.error`, tích hợp danh sách kịch bản từ TV3 và bảng đối chiếu từ TV5 khi sẵn sàng.

## 2. Giải thích cách code hoạt động

- **Hàm hoặc thành phần chính mình viết là gì?** `_extract_risk_fields(result)`, `_render_risk_output(speed_kmh, distance_m)`, `_format_scenario(item)` cùng các thành phần giao diện Streamlit (`st.title`, `st.form`, `st.number_input`, `st.selectbox`, `st.dataframe`, `st.success`, `st.warning`, `st.error`) trong `app/main.py`.
- **Dữ liệu đầu vào:** `speed_kmh` (`float`, đơn vị `km/h`) và `distance_m` (`float`, đơn vị `m`) nhập từ giao diện hoặc trích xuất từ kịch bản được chọn.
- **Dữ liệu đầu ra:** Thông báo trạng thái (`SAFE`, `WARNING`, `DANGER`) hiển thị qua `st.success` / `st.warning` / `st.error`, kèm mã luật, lý do cảnh báo, thông báo lỗi thân thiện khi gặp `ValueError`, và bảng đối chiếu các kịch bản.
- **Các bước xử lý chính:**
 1. Thêm thư mục gốc repository vào `sys.path` để lệnh `streamlit run app/main.py` import module `src.*` ổn định từ thư mục gốc.
 2. Nhận giá trị `speed_kmh` và `distance_m` từ form nhập tay hoặc từ kịch bản do TV3 cung cấp.
 3. Gọi `assess_risk(speed_kmh, distance_m)` từ `src.warning_engine` và bắt `ValueError` để hiển thị `st.error` rõ ràng.
 4. Ánh xạ kết quả trả về sang `st.success` (`SAFE`), `st.warning` (`WARNING`), hoặc `st.error` (`DANGER`) cùng mã luật và lý do.
 5. Gọi `compare_scenarios(scenarios)` từ `src.comparison` khi khả dụng để hiển thị bảng đối chiếu kịch bản.
- **Chương trình của mình gọi module của ai?** Gọi `assess_risk(speed_kmh, distance_m)` từ `src.warning_engine` (TV2), `load_scenarios()` từ module kịch bản của TV3, và `compare_scenarios(scenarios)` từ `src.comparison` (TV5).

## 3. Cách chạy và kết quả thực tế

**Lệnh hoặc thao tác chạy:**

```bash
streamlit run app/main.py
```

| Ví dụ | Input | Kết quả thực tế | Đã kiểm tra? |
|---|---|---|---|
| 1 | _[Điền]_ | _[Điền]_ | ☐ |
| 2 | _[Điền]_ | _[Điền]_ | ☐ |

**Ảnh minh họa (nếu có):** lưu cùng thư mục này và chèn đường dẫn tương đối, ví dụ `![Kết quả](ket-qua.png)`.

## 4. Câu hỏi tự chuẩn bị vấn đáp

1. Vì sao dùng Streamlit?
   - **Trả lời:** _[Tự trình bày ngắn gọn theo code mình viết.]_

2. Giao diện gọi hàm AI và Simulator thế nào?
   - **Trả lời:** _[Tự trình bày ngắn gọn theo code mình viết.]_

3. SAFE/WARNING/DANGER được hiển thị bằng màu nào?
   - **Trả lời:** _[Tự trình bày ngắn gọn theo code mình viết.]_

4. Có thể chạy demo nhập tay và kịch bản ra sao?
   - **Trả lời:** _[Tự trình bày ngắn gọn theo code mình viết.]_

## 5. Bàn giao

- [ ] Code đã đưa lên `main`, đúng file được phân công.
- [ ] Chạy thử được, không còn lỗi cú pháp.
- [ ] README này đã thay các mục `TODO` / `_[Điền]_` bằng nội dung thật.
- [ ] Đã ghi đường dẫn commit trong [issue #11](https://github.com/foxyy163/Mo-phong-he-thong-canh-bao-va-cham-TTNT/issues/11).
- [ ] Đã thông báo thành viên phụ thuộc để họ tiếp tục công việc.

**Commit code:** _[Dán link commit tại đây sau khi hoàn thành.]_
