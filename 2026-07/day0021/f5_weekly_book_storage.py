import json

FILE_NAME = "f5_weekly_books.json"

def load():
    # try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)
    # except FileNotFoundError:
    #     return None
    # except json.JSONDecodeError:
    #     return False

def save(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)