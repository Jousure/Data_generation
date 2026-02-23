import csv
import os
from datetime import datetime

GENERATED_DIR = "generated"


def write_csv(data: list[dict]) -> str:
    """
    Write generated data to a CSV file and return file path.
    """

    if not data:
        raise ValueError("No data to write")

    # Ensure output directory exists
    os.makedirs(GENERATED_DIR, exist_ok=True)

    filename = f"dataset_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    file_path = os.path.join(GENERATED_DIR, filename)

    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return file_path
