import csv
import os
from datetime import datetime
from app.core.generator import generate_value, get_domain_context

GENERATED_DIR = "generated"


def write_csv_streaming(columns: list[dict], count: int) -> str:
    """
    Write generated data to a CSV file using streaming approach for large datasets.
    Optimized for memory efficiency with very large datasets.
    """
    
    if not columns:
        raise ValueError("No columns provided")

    # Extract column names and types
    column_names = [col["name"] for col in columns]
    column_types = {col["name"]: col["type"] for col in columns}

    # Ensure output directory exists
    os.makedirs(GENERATED_DIR, exist_ok=True)

    filename = f"dataset_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv"
    file_path = os.path.join(GENERATED_DIR, filename)

    # Get domain context once for efficiency
    domain = get_domain_context(column_names)

    with open(file_path, mode="w", newline="", encoding="utf-8", buffering=8192) as f:
        writer = csv.DictWriter(f, fieldnames=column_names)
        writer.writeheader()
        f.flush()  # Ensure header is written immediately
        
        # Optimize batch size based on total count
        if count <= 1000:
            batch_size = 100
        elif count <= 10000:
            batch_size = 500
        elif count <= 100000:
            batch_size = 1000
        else:
            batch_size = 2000  # For million+ records
        
        rows_written = 0
        for batch_start in range(0, count, batch_size):
            batch_end = min(batch_start + batch_size, count)
            
            # Generate and write batch
            for _ in range(batch_start, batch_end):
                row = {col["name"]: generate_value(col["type"], domain) for col in columns}
                writer.writerow(row)
                rows_written += 1
            
            # Flush more frequently for very large datasets
            if rows_written % 5000 == 0 or batch_end >= count:
                f.flush()

    # Convert backslashes to forward slashes for URL compatibility
    return file_path.replace("\\", "/")


def write_csv(data: list[dict]) -> str:
    """
    Write generated data to a CSV file and return file path.
    Legacy method for backward compatibility.
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

    # Convert backslashes to forward slashes for URL compatibility
    return file_path.replace("\\", "/")
