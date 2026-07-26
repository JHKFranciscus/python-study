import f4_review_service
import json


try:
    minutes = f4_review_service.calculate_total_minutes()
    print(f"전체 공부 시간: {minutes}분")

except FileNotFoundError:
    print("기록 파일이 없습니다.")

except json.JSONDecodeError:
    print("기록 파일의 JSON 형식이 잘못됐습니다.")