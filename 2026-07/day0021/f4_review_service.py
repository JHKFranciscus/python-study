import f4_review_storage

def calculate_total_minutes():
    records = f4_review_storage.load_records()

    total = 0

    for record in records:
        minutes = int(record["minutes"])
        total += minutes

    return total