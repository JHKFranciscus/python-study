import json

FILE_NAME = "rebuild_books.json"

def load_books():
    try: 
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            books = json.load(file)
            return books
    except FileNotFoundError: 
        return [] 

    except json.JSONDecodeError:
        print("저장 파일의 JSON 형식이 올바르지 않아 빈 목록으로 시작합니다.")
        return []

def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

    return
