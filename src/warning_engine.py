"""Rule-based collision warning engine."""


def assess_risk(speed_kmh: float, distance_m: float) -> dict[str, str]:
    """Return a basic warning level and explanation for the given inputs."""
    if speed_kmh < 0 or distance_m < 0:
        raise ValueError("Speed and distance must be non-negative.")
    if speed_kmh >= 80 and distance_m <= 10:
        return {"level": "Nguy hiểm", "reason": "Tốc độ cao và khoảng cách rất gần."}
    if speed_kmh >= 40 and distance_m <= 20:
        return {"level": "Cảnh báo", "reason": "Khoảng cách gần so với tốc độ."}
    return {"level": "An toàn", "reason": "Chưa phát hiện tình huống nguy cơ theo luật hiện tại."}
