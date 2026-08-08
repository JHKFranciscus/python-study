from pathlib import Path


def save_record(record):
    study_object = Path("study_records")
    study_object.mkdir(exist_ok=True)
    # wirte_text("record.txt", encoding="utf-8")
    #
    file_path = study_object/ "record.txt"

    content = (
        f"주제: {record.topic}\n"
        f"시간: {record.minutes}분\n"
        f"태그: {', '.join(record.tags)}\n"
    )

    file_path.write_text(content, encoding="utf-8")
