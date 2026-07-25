import json

FILE_NAME = "memos.json"

def load_memos():
    try:
        with open("memos.json", "r", encoding="utf-8") as file:
            return json.load(file) #빼먹음

    except FileNotFoundError:
        print("파일을 찾을 수 없어 []으로 시작합니다.")
        return []

    except json.JSONDecodeError:
        print("내용을 찾을 수 없어 []으로 시작합니다.")
        return []

def save_memos(memos):
    # with open(memos, "w", encoding="utf-8") as file:
    with open("memos.json", "w", encoding="utf-8") as file:
        json.dump(memos, file, ensure_ascii=False, indent=4)