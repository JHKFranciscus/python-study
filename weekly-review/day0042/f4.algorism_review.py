scores = [72, 91, 83, 96, 88, 94]

largest_score = scores[0]
student_number = 1

for number, score in enumerate(scores[1:], start=2):
    if largest_score <= score:
        largest_score = score
        student_number = number

print(f"최고 점수: {largest_score}")
print(f"학생 번호: {student_number}")