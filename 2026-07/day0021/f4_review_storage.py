import json

FILE_NAME = "f4_review_data.json"

def load_records():
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)