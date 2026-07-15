student_scores = {
    "민수": 80,
    "지수": 92,
    "철수": 76,
    "영희": 88
}

highest_name = "민수"
highest_score = student_scores[highest_name]

for name, score in student_scores.items():
    if score > highest_score:
        highest_score = score
        highest_name = name
    
print(f"최고 점수 학생은 {highest_name}이고, 점수는 {highest_score}점입니다.")

# 예상 출력
# 최고 점수 학생은 지수이고, 점수는 92점입니다.