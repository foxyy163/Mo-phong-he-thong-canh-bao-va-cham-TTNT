import csv
import math
from pathlib import Path

DEFAULT_CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "scenarios.csv"
REQUIRED_COLUMNS = {"scenario_id", "name", "speed_kmh", "distance_m", "expected_action"}


def load_scenarios(csv_path: str | Path = DEFAULT_CSV_PATH) -> list[dict]:
    """Đọc danh sách kịch bản mô phỏng từ file CSV chuẩn 5 cột."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy file kịch bản: {path}")

    scenarios: list[dict] = []
    with path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(set(reader.fieldnames)):
            missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
            raise ValueError(f"File CSV thiếu cột bắt buộc: {sorted(missing)}")

        for row_num, row in enumerate(reader, start=2):
            try:
                speed = float(row["speed_kmh"])
                distance = float(row["distance_m"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Dòng {row_num}: speed_kmh hoặc distance_m không phải số hợp lệ.") from exc

            if not (math.isfinite(speed) and math.isfinite(distance)) or speed < 0 or distance < 0:
                raise ValueError(f"Dòng {row_num}: speed_kmh và distance_m phải là số hữu hạn không âm.")

            scenarios.append({
                "scenario_id": (row["scenario_id"] or "").strip(),
                "name": (row["name"] or "").strip(),
                "speed_kmh": speed,
                "distance_m": distance,
                "expected_action": (row["expected_action"] or "").strip(),
            })

    return scenarios


if __name__ == "__main__":
    for item in load_scenarios():
        print(item)