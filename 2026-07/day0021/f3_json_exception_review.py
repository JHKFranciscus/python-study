import  json

FILE_NAME = "review_records.json"

def load_records():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            # return json.dump(file)
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

def convert_minutes(minutes_text):
    clean_minutes = minutes_text.strip()

    try:
        new_minutes = int(clean_minutes)
        return new_minutes
    
    except ValueError:
        return None

def add_record(records, topic, minutes):
    clean_topic = topic.strip()

    if clean_topic == "":
        return False

    if minutes is None:
        return False

    # for record in records:
    #     if record["topic"] == clean_topic:
    #         record["minutes"] = minutes

            # new_record = {f"topic: {clean_topic}, minutes: {minutes}"}
    new_record = {"topic": clean_topic, "minutes": minutes}

    records.append(new_record)
    return True

def save_records(records):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=4)

records = load_records()

while True:
    print()
    print("1. 기록 불러오기")
    print("2. 기록 추가")
    print("3. 종료")


    menu = input("메뉴를 입력하세요: ")

    if menu == "1":
        # load = load_records()
        records = load_records()

        if len(records) == 0:
            print("저장된 기록이 없습니다.")
        else:
            for record_nubmer, record in enumerate(records, start=1):
                print(f"{record_nubmer}. {record['topic']} - {record['minutes']}분")

    elif menu == "2":
        topic = input("새 주제: ")
        minutes_text = input("새 시간: ")

        minutes = convert_minutes(minutes_text)
        added = add_record(records, topic, minutes)

        # if minutes != None:
            # add_record(records, topic, minutes)
            # records = load_records()

            # if add_record == True:
        if added:
            save_records(records)
            print("기록을 저장했습니다.")
        else:
            print("올바른 주제와 시간을 입력해주세요.")

    elif menu == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴를 입력해주세요.")
