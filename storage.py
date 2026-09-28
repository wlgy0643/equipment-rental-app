"""CSV 저장소: 한 앱 프로세스의 여러 사용자 요청을 순서대로 처리합니다."""
import csv
import os
from datetime import datetime
from pathlib import Path
from threading import RLock
from uuid import uuid4

DATA_FILE = Path(__file__).resolve().parent / "data" / "rentals.csv"
FIELDS = ["등록번호", "직원명", "부서", "대여 비품", "대여일", "반납예정일", "등록일시"]
_LOCK = RLock()


def load_rentals():
    with _LOCK:
        if not DATA_FILE.exists():
            return []
        with DATA_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != FIELDS:
                raise ValueError("CSV 열 제목이 올바르지 않습니다.")
            rows = list(reader)
            if any(set(row) != set(FIELDS) or any(value is None for value in row.values()) for row in rows):
                raise ValueError("CSV 데이터 형식이 올바르지 않습니다.")
            return rows


def save_rental(employee, department, item, rental_date, due_date):
    if not employee.strip() or not department or not item:
        raise ValueError("직원명, 부서, 비품은 필수입니다.")
    if due_date < rental_date:
        raise ValueError("반납예정일은 대여일보다 빠를 수 없습니다.")
    row = dict(zip(FIELDS, [
        uuid4().hex, employee.strip(), department, item,
        rental_date.isoformat(), due_date.isoformat(),
        datetime.now().isoformat(timespec="seconds"),
    ]))
    with _LOCK:
        rows = load_rentals()
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        temporary = DATA_FILE.with_suffix(".tmp")
        try:
            with temporary.open("w", encoding="utf-8-sig", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(rows)
                writer.writerow(row)
                file.flush()
                os.fsync(file.fileno())
            os.replace(temporary, DATA_FILE)
        finally:
            temporary.unlink(missing_ok=True)
