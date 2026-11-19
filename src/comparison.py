"""Đối chiếu kết quả kỳ vọng (expected_action) với kết quả thực tế của AI (actual_level).

TV5 — issue #10. Module này KHÔNG tự viết lại luật IF–THEN: nó gọi
`assess_risk` của TV2 và chỉ làm nhiệm vụ so sánh.

Luồng dữ liệu:  CSV (TV3: load_scenarios)  ->  compare_scenarios (TV5)  ->  giao diện (TV4)
                                                    |
                                          gọi assess_risk (TV2)

Mỗi dòng kết quả có các key:
    scenario_id, name, speed_kmh, distance_m, expected_action   (lấy từ CSV)
    actual_level          SAFE/WARNING/DANGER do AI tính; None nếu ERROR
    status                PASS / FAIL / ERROR
    reason, rule_id       giải thích và mã luật từ AI ("" nếu ERROR)
    stopping_distance_m, warning_distance_m   ngưỡng AI dùng (None nếu ERROR)
    error                 nội dung lỗi ("" nếu không lỗi)

Chạy thử (từ thư mục gốc repo):  python -m src.comparison
"""

try:  # chạy từ thư mục gốc: streamlit / python -m src.comparison
    from src.warning_engine import assess_risk
except ModuleNotFoundError:  # chạy trực tiếp: python src/comparison.py
    from warning_engine import assess_risk

VALID_LEVELS = ("SAFE", "WARNING", "DANGER")


def _normalize_expected(value) -> str:
    """Chuẩn hóa expected_action do người nhập trong CSV: bỏ khoảng trắng, viết hoa."""
    return str(value).strip().upper() if value is not None else ""


def _compare_one(scenario: dict) -> dict:
    """So sánh một kịch bản. Mọi lỗi của riêng kịch bản này được ghi thành ERROR."""
    row = {
        "scenario_id": scenario.get("scenario_id"),
        "name": scenario.get("name"),
        "speed_kmh": scenario.get("speed_kmh"),
        "distance_m": scenario.get("distance_m"),
        "expected_action": scenario.get("expected_action"),
        "actual_level": None,
        "status": "ERROR",
        "reason": "",
        "rule_id": "",
        "stopping_distance_m": None,
        "warning_distance_m": None,
        "error": "",
    }

    expected = _normalize_expected(row["expected_action"])
    if expected not in VALID_LEVELS:
        row["error"] = f"expected_action không hợp lệ: {row['expected_action']!r}"
        return row

    try:
        result = assess_risk(row["speed_kmh"], row["distance_m"])
    except Exception as exc:  # ValueError từ TV2 hoặc dữ liệu sai kiểu
        row["error"] = f"{type(exc).__name__}: {exc}"
        return row

    # actual_level phải ĐÚNG mã chuẩn (không tự sửa chữ hoa/thường) để lộ lỗi hợp đồng của AI.
    actual = result.get("level") if isinstance(result, dict) else None
    if actual not in VALID_LEVELS:
        row["error"] = f"assess_risk trả level ngoài SAFE/WARNING/DANGER: {result!r}"
        return row

    row["actual_level"] = actual
    row["reason"] = result.get("reason", "")
    row["rule_id"] = result.get("rule_id", "")
    row["stopping_distance_m"] = result.get("stopping_distance_m")
    row["warning_distance_m"] = result.get("warning_distance_m")
    row["status"] = "PASS" if actual == expected else "FAIL"
    return row


def compare_scenarios(scenarios: list[dict]) -> list[dict]:
    """Chạy AI cho từng kịch bản và trả bảng đối chiếu.

    Mỗi dòng có tối thiểu: scenario_id, name, speed_kmh, distance_m,
    expected_action, actual_level, status (PASS / FAIL / ERROR).
    Có thêm reason, rule_id, stopping_distance_m, warning_distance_m, error
    để giao diện hiển thị lời giải thích.
    Một kịch bản lỗi không làm dừng các kịch bản còn lại.
    """
    results = []
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            scenario = {}
        results.append(_compare_one(scenario))
    return results


if __name__ == "__main__":
    try:
        from src.simulator import load_scenarios
    except ModuleNotFoundError:
        from simulator import load_scenarios

    try:
        rows = compare_scenarios(load_scenarios())
    except (FileNotFoundError, ValueError) as exc:  # CSV thiếu hoặc sai định dạng (lỗi của TV3)
        raise SystemExit(f"Không đọc được kịch bản từ CSV: {exc}")

    print(f"{'ID':<6}{'speed':>7}{'dist':>7}  {'expected':<9}{'actual':<9}{'status':<6} rule")
    for r in rows:
        print(
            f"{str(r['scenario_id']):<6}{str(r['speed_kmh']):>7}{str(r['distance_m']):>7}  "
            f"{str(r['expected_action']):<9}{str(r['actual_level']):<9}{r['status']:<6} {r['rule_id']}"
            + (f"  <- {r['error']}" if r["error"] else "")
        )
    counts = {s: sum(r["status"] == s for r in rows) for s in ("PASS", "FAIL", "ERROR")}
    print("Tổng:", counts)
