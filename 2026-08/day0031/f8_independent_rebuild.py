scores = [
    {"name": "민수", "score": 55},
    {"name": "지수", "score": 80},
    {"name": "현우", "score": 67},
    {"name": "서연", "score": 92},
    {"name": "도윤", "score": 40},
]

#1. add_five(score) -> socre + 5 / add_ten(score) -> score + 10
def add_five(score):
    score_plus_five = score + 5
    if score_plus_five >= 100:
        return 100
    else:
        return score_plus_five

def add_ten(score):
    score_plus_ten = score + 10
    if score_plus_ten >= 100:
        return 100
    else:
        return score_plus_ten

#2. select_bonus(choice) -> add_five 함수 객체, add_ten 함수 객체, None
def select_bonus(choice):
    if choice == "1":
        return add_five

    elif choice == "2":
        return add_ten

    else:
        return None
    
#3. apply_bonus(student, bonus_function) -> 
def apply_bonus(student, bonus_function):
    return {
    "name": student["name"],
    "original_score": student["score"],
    "bonus_score": bonus_function(student["score"]),
}
#4. select_bonus("2")
filtered_scores = filter(lambda student: student["score"] >= 60, scores)

# mapped = map(lambda filtered_score: apply_bonus(filtered_score, select_bonus("2")), filtered_scores)
selected_bonus = select_bonus("2")

mapped = map(lambda filtered_score: apply_bonus(filtered_score, selected_bonus), filtered_scores)

results = list(mapped)

#5. 출력
# print(f"선택된 함수: {select_bonus("2").__name__}")
print("선택된 함수:", selected_bonus.__name__)
print("결과 자료형:", results.__class__)
# for index in range(len(results)):
#     print(f"{results[index]["name"]} {results[index]["original_score"]} → {results[index]["bonus_score"]}")
for result in results:
    print(result["name"],
          result["original_score"],
          "→",
          result["bonus_score"],
          )
print("원본 점수 목록:", scores)
print("map 재사용:", list(mapped))
# 개인 공부
print()
print("결과 리스트 재사용:", results)
