#문제1

numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total += i       
    #i += numbers라는 실수를 했었다.
    #실제로는 10 + [10, 20, 30, 40, 50] 이런계산을 시도한 것으로
    #이 오류의 종류는 정수와 리스트를 더하는 오류였다.

print(total)
#region
# 시작: total = 0
# 10을 처리한 후: 10
# 20을 처리한 후: 30
# 30을 처리한 후: 60
# 40을 처리한 후: 100
# 50을 처리한 후: 150
#endregion

#문제2

numbers = [3, 8, 12, 7, 10, 5]

even_count = 0
odd_count = 0

for number in numbers:    #number가 아니라 i를 써도 되지만 업계 관행으로는 이게 맞다
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("짝수 개수: {}".format(even_count))
print("홀수 개수: {}".format(odd_count))
#region
# 3 처리 후: even_count = 0, odd_count = 1
# 8 처리 후: even_count = 1, odd_count = 1
# 12 처리 후: even_count = 2, odd_count = 1
# 7 처리 후: even_count = 2, odd_count = 2
# 10 처리 후: even_count = 3, odd_count = 2
# 5 처리 후: even_count = 3, odd_count = 3
#endregion

#문제3

scores = [75, 90, 55, 60, 100]
pass_count = 0

for score in scores:
    if score >= 60:
        print("합격 점수:", score)
        pass_count += 1
    else:
        continue

print(f"합격자 수: {pass_count}")
#region
# 75 처리 후: 합격 여부 = 합격, pass_count = 1
# 90 처리 후: 합격 여부 = 합격, pass_count = 2
# 55 처리 후: 합격 여부 = 불합격, pass_count = 2
# 60 처리 후: 합격 여부 = 합격, pass_count = 3
# 100 처리 후: 합격 여부 = 합격, pass_count = 4
#endregion
#region
#else아래에 실행할 코드가 없기 때문에 생략해도 결과는 같다
#else: continue를 생략했을 때
# 1. for score in scores: 루프가 돌면서 score에 55가 담깁니다.
# 2. if score >= 60: 조건을 검사하고, 거짓(False)이 됩니다.
# 3. if 조건이 거짓이므로 if 블록 안의 코드(print와 pass_count += 1)는 실행되지 않고 건너뜁니다.
# 4. if 블록을 건너뛰고 보니 그 아래에 더 이상 실행할 코드가 없습니다.
# 5. 할 일이 끝났으므로 자연스럽게 다음 점수인 60으로 넘어갑니다.
#endregion

#문제4

numbers = [4, 7, 4, 2, 4, 9]
four_count = 0

for number in numbers:
    if  number == 4:  #여기도 변수명을 four_count로 했었다. 변수명 생각잘하자
        four_count += 1

print("4의 개수: ", four_count)
#region
# 시작: four_count = 0
# 첫 번째 4 처리 후: four_count = 1
# 7 처리 후: four_count = 1
# 두 번째 4 처리 후: four_count = 2
# 2 처리 후: four_count = 2
# 세 번째 4 처리 후: four_count = 3
# 9 처리 후: four_count = 3
#endregion

#문제5

scores = [80, 35, 95, 105, -10, 70]
valid_scores = []

for score in scores:
    if 0 <= score <= 100:
        valid_scores.append(score)

print(f"정상 점수: {valid_scores}")
#region
# 시작: valid_scores = []
# 80 처리 후: valid_scores = [80]
# 35 처리 후: valid_scores = [80, 35]
# 95 처리 후: valid_scores = [80, 35, 95]
# 105 처리 후: valid_scores = [80, 35, 95]
# -10 처리 후: valid_scores = [80, 35, 95]
# 70 처리 후: valid_scores = [80, 35, 95, 70]
#endregion
#region
#append()는 원본 scores를 바꾸는 것이 아니라,
#조건을 통과한 score를 valid_scores 끝에 추가한다.
#endregion

#문제6

numbers = [5, 2, 9, 1, 7]
largest = numbers[0]

for number in numbers:
    if largest < number:
        largest = number

print("최댓값: {}".format(largest))
#region
# 시작: largest = 5
# 5 비교 후: largest = 5 < 5인가? False
# 2 비교 후: largest = 5 < 2인가? False
# 9 비교 후: largest = 5 < 9인가? True
# 1 비교 후: 현재 largest < 1인가? False
# 7 비교 후: 현재 largest < 7인가? False
#endregion
