scores = []


while True:
    print()
    print("1. 점수 추가")
    print("2. 전체 점수 보기")
    print("3. 통계")
    print("4. 합격자 수")
    print("5. 마지막 점수 삭제")

    choice = input("메뉴를 골라주세요. 종료시 0: ") #뒤에 else로 처리할 거니까 int를 안 해줘도 된다.

    if choice == 0:
        print("프로그램을 종료합니다.")
        break

    elif choice == 1:
        new_score = int(input("점수를 입력하세요: "))
        if 0 <= new_score <=100:
            scores.append(new_score)
            print(f"현재 점수: {scores}")
        else:
            print("잘못된 점수입니다.")
    
    elif choice == 2:
        print(f"전체 점수: {scores}")
        # if len(scores) == 0:
        #     print("입력된 점수가 없습니다.")
        # else:
        #     print("전체 점수", scores)
        #점수 없을 때를 생각해주기

    elif choice == 3:
        #if len(scores) == 0:
        #     print("저장된 점수가 없어 통계를 계산할 수 없습니다.")
        # else:
        #를 해서 아무것도 없을 때도 생각을 해줘야한다. 안해도 오류는 안 드는데 그냥 종료된다.
        total = 0
        largest = scores[0]
        smallest = scores[0]

        for saved_score in scores:
            total += saved_score

            if saved_score > largest:
                largest = saved_score

            if saved_score < smallest:
                smallest = saved_score
        
        print(total/len(scores))
        #점수 계수, 평균, 합계, 최댓값, 최솟값도 프린트 해주기 
    
    elif choice == 4:
        # if len(scores) == 0:
        #     print("저장된 점수가 없습니다.")
        # else:
        #여기도 마찬가지
        pass_count = 0
        for saved_score in scores:
            if saved_score >= 60:
                pass_count += 1
        
        print(f"합격자 수는 {saved_score}입니다.")

    elif choice == 5:
        removed_score = scores.pop()
        print(f"{removed_score}가 삭제되었습니다.")
    # elif choice == "5":
    #     if len(scores) != 0:
    #         removed_score = scores.pop()
    #         print(f"{removed_score}점이 삭제되었습니다.")
    #         print("현재 점수: ", scores)
    #     else:
    #         print("삭제할 점수가 없습니다.")
    #여기도 마찬가지

    # else:
    #     print("잘못된 메뉴선택")
