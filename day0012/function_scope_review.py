def calculate_total(scores):
    total = 0

    for score in scores:
        total += score

    return total

def calculate_average(scores):
    total = calculate_total(scores)
    average = total / len(scores)

    return average

def determine_result(average):
    if average >= 70:
        return "합격"
    else:
        return "불합격"


scores = [80, 65, 90, 75]

total = calculate_total(scores)
average = calculate_average(scores)
result = determine_result(average)

print("총점:", total)
print("평균:", average)
print("결과:", result)

