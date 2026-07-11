scores = []


while True:
    print()
    print("=== 점수 관리 프로그램 ===")
    print("1. 점수 추가")
    print("2. 전체 점수 보기")
    print("3. 점수 통계")
    print("4. 합격자 수 보기")
    print("0. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":
        new_score = int(input("추가할 점수를 입력하세요: "))

        if 0 <= new_score <= 100:
            scores.append(new_score)
            print(f"{new_score}점이 추가되었습니다.")
            print("현재 점수: ",scores)
        else:
            print("점수는 0점 이상 100점 이하로 입력하세요")
    
    elif choice == "2":
        if len(scores) == 0:
            print("저장된 점수가 없습니다.")
        else:
            print("전체 점수: ", scores)

    elif choice == "3":
        if len(scores) == 0:
            print("저장된 점수가 없어 통계를 계산할 수 없습니다.")
        else:
            total = 0
            largest = scores[0]
            smallest = scores[0]

            for score in scores:
                total += score
                if score > largest:
                    largest = score
                
                if score < smallest:
                    smallest = score

            average = total / len(scores)

            print("점수 개수:", len(scores))
            print("합계:", total)
            print("평균:", average)
            print("최댓값:", largest)
            print("최솟값:", smallest)
    
    elif choice == "4":
        if len(scores) == 0:
            print("저장된 점수가 없습니다.")
        else:
            pass_count = 0
            for saved_score in scores:
                if saved_score >= 60:
                    pass_count += 1
            
            print("합격자 수: ", pass_count)
    
    else:
        print("올바른 메뉴 번호를 입력하세요.")
