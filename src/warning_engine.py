"""Bộ suy diễn cảnh báo va chạm bằng luật IF–THEN (mô phỏng học tập)."""

import math

REACTION_TIME_S = 1.0
DECELERATION_M_S2 = 5.0
WARNING_FACTOR = 1.5


def assess_risk(speed_kmh: float, distance_m: float) -> dict[str, str | float]:
    """Trả mức cảnh báo, mã luật, lời giải thích và ngưỡng khoảng cách.

    Input: tốc độ km/h, khoảng cách m (số hữu hạn, không âm).
    Output: level, reason, rule_id, stopping_distance_m, warning_distance_m.
    Lưu ý: đây chỉ là mô phỏng, không dùng cho phương tiện thật.
    """
    for name, value in (("speed_kmh", speed_kmh), ("distance_m", distance_m)):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} phải là số thực hoặc số nguyên.")
        if not math.isfinite(value) or value < 0:
            raise ValueError(f"{name} phải là số hữu hạn không âm.")

    speed_ms = speed_kmh / 3.6
    stopping_distance = (
        speed_ms * REACTION_TIME_S
        + speed_ms ** 2 / (2 * DECELERATION_M_S2)
    )
    warning_distance = WARNING_FACTOR * stopping_distance

    # Ưu tiên theo mức độ nguy hiểm: R01 > R02 > R03.
    if distance_m == 0 or distance_m <= stopping_distance:
        level = "DANGER"
        rule_id = "R01"
        reason = "Khoảng cách hiện tại không vượt quá khoảng cách dừng dự kiến."
    elif distance_m <= warning_distance:
        level = "WARNING"
        rule_id = "R02"
        reason = "Khoảng cách hiện tại nằm trong vùng cần cảnh báo."
    else:
        level = "SAFE"
        rule_id = "R03"
        reason = "Khoảng cách hiện tại vượt ngưỡng cảnh báo của mô hình."

    return {
        "level": level,
        "reason": reason,
        "rule_id": rule_id,
        "stopping_distance_m": stopping_distance,
        "warning_distance_m": warning_distance,
    }
