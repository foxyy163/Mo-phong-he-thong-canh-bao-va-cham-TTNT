import sys
from pathlib import Path
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.warning_engine import assess_risk
from src.simulator import load_scenarios
from src.comparison import compare_scenarios

def _format_num(val):
    if val is None:
        return "N/A"
    if isinstance(val, float):
        return f"{val:.2f}"
    return str(val)

def _render_assessment_card(speed_val, distance_val):
    try:
        res = assess_risk(speed_val, distance_val)
    except ValueError as exc:
        st.error(f"Lỗi dữ liệu đầu vào: {exc}")
        return
    except Exception as exc:
        st.error(f"Lỗi khi đánh giá rủi ro: {exc}")
        return

    level = str(res.get("level", "")).upper()
    rule_id = res.get("rule_id", "N/A")
    reason = res.get("reason", "")
    d_stop = res.get("stopping_distance_m")
    d_warn = res.get("warning_distance_m")

    m1, m2, m3 = st.columns(3)
    m1.metric("Tốc độ hiện tại", f"{float(speed_val):.1f} km/h")
    m2.metric("Khoảng cách thực tế", f"{float(distance_val):.1f} m")
    m3.metric("D_stop / D_warning", f"{_format_num(d_stop)}m / {_format_num(d_warn)}m")

    if level == "SAFE":
        st.success(f"### XANH — SAFE\n{reason}")
    elif level == "WARNING":
        st.warning(f"### VÀNG — WARNING\n{reason}")
    elif level == "DANGER":
        st.error(f"### ĐỎ — DANGER\n{reason}")
    else:
        st.info(f"### {level}\n{reason}")

    with st.container(border=True):
        st.markdown("#### Giải thích kết quả & Luật được kích hoạt")
        st.markdown(f"- **Mức cảnh báo:** `{level}`")
        st.markdown(f"- **Mã luật:** `{rule_id}`")
        st.markdown(f"- **Ngưỡng dừng (`stopping_distance_m`):** `{_format_num(d_stop)} m`")
        st.markdown(f"- **Ngưỡng cảnh báo (`warning_distance_m`):** `{_format_num(d_warn)} m`")
        st.markdown(f"- **Giải thích chi tiết:** {reason}")

st.set_page_config(page_title="Mô phỏng Hệ thống Cảnh báo Va chạm", page_icon="🚗", layout="wide")

st.title("🚗 Mô Phỏng Hệ Thống Cảnh Báo Va Chạm (FCW)")
st.caption("TV4 — Giao diện Streamlit (Issue #11)")

with st.expander("Hướng dẫn sử dụng & Quy ước mức cảnh báo", expanded=False):
    st.markdown("""
- **Bước 1:** Nhập trực tiếp **Tốc độ (km/h)** và **Khoảng cách (m)** hoặc chọn kịch bản từ danh sách CSV của TV3.
- **Bước 2:** Nhấn **Đánh giá** (hoặc **Chạy kịch bản đã chọn**) để gọi bộ luật từ `src.warning_engine`.
- **Bước 3:** Xem mức cảnh báo (**SAFE / Xanh**, **WARNING / Vàng**, **DANGER / Đỏ**), mã luật, ngưỡng khoảng cách và bảng đối chiếu từ TV5.
    """)

try:
    csv_scenarios = load_scenarios()
except Exception as exc:
    st.error(f"Không thể tải danh sách kịch bản: {exc}")
    csv_scenarios = []

col_input, col_output = st.columns([1, 1.6], gap="large")

with col_input:
    st.subheader("1. Khu vực nhập dữ liệu")
    with st.form("manual_form"):
        speed = st.number_input("Tốc độ (km/h)", value=30.0, step=1.0, format="%.2f")
        distance = st.number_input("Khoảng cách (m)", value=30.0, step=1.0, format="%.2f")
        submitted = st.form_submit_button("Đánh giá", type="primary", use_container_width=True)

    st.divider()
    st.subheader("Kịch bản từ TV3")
    selected_scenario = None
    run_scenario_btn = False
    if csv_scenarios:
        labels = [
            f"{sc.get('scenario_id', '')} - {sc.get('name', '')} ({sc.get('speed_kmh')} km/h, {sc.get('distance_m')} m)"
            for sc in csv_scenarios
        ]
        sel_idx = st.selectbox("Chọn kịch bản:", options=list(range(len(csv_scenarios))), format_func=lambda i: labels[i])
        selected_scenario = csv_scenarios[sel_idx]
        run_scenario_btn = st.button("Chạy kịch bản đã chọn", use_container_width=True)
    else:
        st.info("Chưa có kịch bản nào từ CSV.")

with col_output:
    st.subheader("2. Kết quả đánh giá & Giải thích luật")
    if submitted:
        _render_assessment_card(speed, distance)
    elif run_scenario_btn and selected_scenario is not None:
        _render_assessment_card(selected_scenario.get("speed_kmh"), selected_scenario.get("distance_m"))
    else:
        st.info("Nhập thông số bên trái và bấm **Đánh giá**, hoặc chọn một kịch bản để xem kết quả.")

st.divider()
st.subheader("3. Bảng đối chiếu kịch bản (TV5)")

if csv_scenarios:
    try:
        rows = compare_scenarios(csv_scenarios)
        st.dataframe(rows, use_container_width=True)
        passed = sum(1 for r in rows if r.get("status") == "PASS")
        st.write(f"**Tổng kết đối chiếu:** `{passed}/{len(rows)}` kịch bản đạt `PASS`.")
        for r in rows:
            st_val = r.get("status")
            sid = r.get("scenario_id", "")
            if st_val == "PASS":
                st.success(f"{sid}: {r.get('actual_level')} ({r.get('rule_id')}) — PASS")
            elif st_val == "FAIL":
                st.warning(f"{sid}: kỳ vọng {r.get('expected_action')}, thực tế {r.get('actual_level')} ({r.get('rule_id')}) — FAIL")
            else:
                st.error(f"{sid}: ERROR — {r.get('error')}")
    except Exception as exc:
        st.error(f"Lỗi khi gọi compare_scenarios: {exc}")
else:
    st.info("Không có kịch bản để đối chiếu.")
