# 1주차 점수 관리 프로그램 독립 재현

# 구현 순서
# 1. 빈 리스트 생성
# 2. while반복문 작성
# 3. 메뉴 적어두기
# 4. 사용자의 메뉴 선택을 입력받고 if, elif로 기능을 구분
# 5. 종료 메뉴먼저 제작
# 6. 각 조건에 맞는 코드 제작
# 7. 빈 리스트일 때 통계와 삭제가 오류 나지 않도록 처리하고 실행 테스트

# 점수 리스트를 어느 위치에서 만들 것인가:
# 반복문 바깥에서
# 메뉴를 어떻게 반복해서 보여줄 것인가:
# while 반복문을 통하여
# 사용자가 종료를 선택하면 어떻게 반복을 끝낼 것인가:
# break를 통하여

scores = []

while True:
    print("1. 점수 추가")
    print("2. 전체 점수 보기")
    print("3. 점수 통계")
    print("4. 합격자 수")
    print("5. 마지막 점수 삭제")
    print("6. 종료")

    choice = int(input("메뉴를 입력하세요: "))



    if choice == 1:
        new_score = int(input("점수를 입력하세요: "))
        scores.append(new_score)
        # append 안에는 리스트 자체가 아니라 새로 입력받은 점수를 넣어야 한다.
        print(f"{new_score}가 추가 되었습니다.")

    elif choice == 2:
        if len(scores) == 0:
            print("저장된 점수가 없습니다.")
        else:
            print("현재 점수: ", scores)

    elif choice == 3:
        if len(scores) == 0:
            print("저장된 점수가 없습니다.")
        else:
            total = 0
            highest_score = scores[0]
            smallest_score = scores[0]

            for score in scores:
                total += score

                if score > highest_score:
                    highest_score = score
                elif score < smallest_score:
                    smallest_score = score

            average = total/len(scores)
                             
            print("점수 개수: ", len(scores))
            print("총합:", total)
            print("평균:", average)
            print("최고점:", highest_score)
            print("최저점:", smallest_score)

    elif choice == 4:
        pass_count = 0

        for pass_score in scores:
            if pass_score >= 60:
                pass_count += 1
        
        print("합격자 수:",pass_count)


    elif choice == 5:
        if len(scores) == 0:
            print("삭제할 점수가 없습니다.")
        else:
            removed_score = scores.pop()
            print(f"{removed_score}가 삭제 되었습니다.")

    elif choice == 6:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴 번호입니다.")
