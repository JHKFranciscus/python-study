def print_menu():
    print("1. 점수 입력")
    print("2. 점수 계산")
    print("3. 종료")

def add_score(scores):
    add_score = int(input("점수를 입력하세요: "))
    if 0 <= add_score <= 100:
        scores.append(add_score)
        print(f"{add_score}점을 입력했습다.")
    else:
        print("잘못된 점수입니다.")

def calculate_total(scores):
    total = 0
    for i in scores:
        total += i    
    return total

def find_largest(scores):
    largest = scores[0]
    for score in scores:
        if largest < score:
             largest = score
    return largest    

def find_smallest(scores):
    smallest = scores[0]
    for score in scores:
        if smallest > score:
             smallest = score
    return smallest
  
def calculate_average(scores):
    total = calculate_total(scores)
    average = total/len(scores)
    return average

def print_result(scores):
    if len(scores) == 0:
        print("점수가 존재하지 않습니다.")
    else:
        total = calculate_total(scores)
        largest = find_largest(scores)
        smallest = find_smallest(scores)
        average = calculate_average(scores)
        print(f"점수 목록: {scores}")
        print(f"합계: {total}")
        print(f"최댓값: {largest}")
        print(f"최솟값: {smallest}")
        print(f"평균: {average}")

scores = []

while True:
    print()
    print_menu()

    choice = int(input("번호를 선택하세요: "))

    if choice == 1:
        add_score(scores)

    elif choice == 2:
        print_result(scores)

    elif choice == 3:
        print("종료합니다.")
        break

    else:
        print("잘못된 번호입니다.")



# 함수 코드가 어떤 순서로 실행되는지 직접 추적:
# print_menu()로 호출
# def print_menu()를 실행

# choice 1 선택 시
# add_score(scores)로 호출
# def add_score(scores)를 실행

# choice 2 선택 시
# print_result(scores)로 호출
# def print_result(scores)를 실행
# if len(scores) == 0: 불충족시
# calculate_total(scores)로 호출
# def calculate_total(scores)를 실행해서
# total을 return
# find_largest(scores)로 호출
# def find_largest(scores)를 실행해서
# largest를 return
# find_smallest(scores)로 호출
# def find_smallest(scores)를 실행해서
# smallest를 return
# calculate_average(scores)로 호출
# def calculate_average(scores)를 실행해서
# average를 return