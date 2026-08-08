def normalize_name(name):
    return name.strip().lower()

def contains_keyword(text, keyword):
    if keyword in text:
        return True

    else:
        return False

if __name__ == "__main__":
    print("text_utils 직접 실행")