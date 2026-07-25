import json

FILE_NAME = "f6_rebuild_books.json"

def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            books = json.load(file)
            return books  #빼먹음

    except FileNotFoundError:
        print("파일이 존재하지 않으므로 []로 시작합니다.")
        return []

    except json.JSONDecodeError:
        print("파일의 내용이 잘못되었으므로 []로 시작합니다.")
        return []

def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file: #빼먹음, w모드 안 쓰고 r모드 씀
        # json.dump(books, FILE_NAME, ensure_ascii=False, indent=4)
        json.dump(books, file, ensure_ascii=False, indent=4)