def add_memo(memos, text):
    text = text.strip()

    if text == "":
        print("빈 문자열은 입력할 수 없습니다.")
        return False

    new_text = {"text": text}

    memos.append(new_text)
    # return memos
    return True

def search_memos(memos, keyword):
    keyword = keyword.strip()

    if keyword == "":
        return None

    found = []

    for memo in memos:
        cleaned_text = memo["text"].strip().lower() #빼먹음
        
        # if keyword in memo:
        if keyword in cleaned_text:
            found.append(memo)

    return found


    