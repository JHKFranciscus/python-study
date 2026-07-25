scores = []

while True:
    print()
    print("1. 점수 입력")
    print("2. 점수 계산")
    print("3. 종료")

    choice = int(input("번호를 선택하세요: "))

    if choice == 1:
        new_score = int(input("점수를 입력하세요: "))
        if 0 <= new_score <=100:
            scores.append(new_score)
            print(f"{new_score}점을 입력했습니다.")
        else:
            print("잘못된 점수입니다.")

    elif choice == 2:
        if len(scores) == 0:
            print("점수가 존재하지 않습니다.")
        else:
            total = 0
            largest = scores[0]
            smallest = scores[0]

            for score in scores:
                if largest < score:
                    largest = score
                
                if smallest > score:
                    smallest = score

                total += score
            
            average = total/len(scores)

            print("점수 목록", scores)
            print(f"합계: {total}")
            print(f"최댓값: {largest}")
            print(f"최솟값: {smallest}")
            print(f"평균: {average}")


    elif choice == 3:
        print("종료합니다.")
        break

    else:
        print("잘못된 번호입니다.")