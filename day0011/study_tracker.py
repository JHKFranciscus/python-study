# 변경하지 않을 학생 기본 정보
student_info = (101, "민수")

# 학습할 과목을 순서대로 저장
study_order = []

# 과목 이름과 점수를 연결
subject_scores = {}

# 완료한 과목을 중복 없이 저장
completed_subjects = set()


while True:
    print()
    # print("=== 학습 현황 관리 ===")
    # print("학생 번호:", student_info[0])
    # print("학생 이름:", student_info[1])
    # print("1. 학습 과목 추가")
    # print("2. 과목 점수 등록 또는 수정")
    # print("3. 완료 과목 등록")
    # print("4. 전체 학습 현황 조회")
    # print("5. 종료")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        new_subject = input("추가할 과목을 입력하세요: ")

        if new_subject in study_order:
            print("이미 등록된 과목입니다.")
        else:
            study_order.append(new_subject)
            print(new_subject, "과목을 추가했습니다.")

        print("현재 학습 과목:", study_order)
#region
# 1. new_subject in study_order는 무엇을 검사하는가?
# new_subject에 저장된 값과 같은 요소가 study_order 리스트에 존재하는지 검사한다.
# 2. 이미 Python이 있는데 다시 Python을 입력하면 append가 실행되지 않는 이유는 무엇인가?
# if문에서 new_subject가 study_order안에 존재하면 추가를 하지 않기 때문이다.
# 3. study_order에 세트가 아니라 리스트를 사용한 이유는 무엇인가?
# index로 접근하기 위해서
# 보완:
# 학습 과목을 입력한 순서대로 보관하고,
# 새로운 과목을 append로 추가할 수 있기 때문이다.
# 중복 여부는 in으로 직접 검사하여 막는다.
#endregion
    elif menu == "2":
        score_subject = input("점수를 등록할 과목을 입력하세요: ")

        if score_subject not in study_order:
            print("먼저 학습 과목을 등록하세요.")
        else:
            score = int(input("점수를 입력하세요: "))

            if score_subject in subject_scores:
                print("기존 점수를 수정합니다.")
            else:
                print("새 점수를 등록합니다.")
            
            subject_scores[score_subject] = score
            print("현재 과목별 점수:", subject_scores)
#region
# 1. score_subject not in study_order는 무엇을 검사하는가?
# score_subject에 저장된 값과 같은 요소가 study_order 리스트에 존재하지 않는지 검사한다
# 2. Python을 학습 과목으로 먼저 등록하지 않으면 점수를 입력받는 코드까지 실행되지 않는 이유는 무엇인가?
# if문에서 score_subject가 study_order 안에 존재하지 않으면, 먼저 학습과목을 등록하라는 문장만 출력하고 else를 출력하지 않기 때문이다.
# 3. 처음 Python 점수 80을 등록할 때 subject_scores["Python"] = 80은 추가인가, 수정인가?
# 추가
# 4. 이후 Python 점수 90을 등록할 때 subject_scores["Python"] = 90은 추가인가, 수정인가?
# 수정
# 5. 점수 입력에 int()를 사용한 이유는 무엇인가?
# int()를 사용하지 않고, input을 사용하면 문자열이 되기 때문이다.
# 보완
# 점수를 문자열이 아니라 정수로 저장하여 이후 합계나 평균 등의 숫자 계산에 사용할 수 있게 하기 때문이다.
#endregion
    elif menu == "3":
        completed_subject = input("완료한 과목을 입력하세요: ")

        if completed_subject not in study_order:
            print("먼저 학습 과목을 등록하세요.")
        elif completed_subject in completed_subjects:
            print("이미 완료된 과목입니다.")
        else:
            completed_subjects.add(completed_subject)
            print(completed_subject, "과목을 완료 처리했습니다.")

        print("현재 완료 과목:", completed_subjects)
#region
# 1. completed_subject not in study_order는 무엇을 검사하는가?
# completed_subject에 저장된 값이 study_order의 요소에 없는지 확인
# 2. completed_subject in completed_subjects는 무엇을 검사하는가?
# completed_subject에 저장된 값이 completed_subjects의 요소에 있는지 확인
# 3. 이미 완료된 Python을 다시 입력했을 때 add()가 실행되지 않는 이유는 무엇인가?
# elif문에서 completed_subject에 저장된 값이 completed_subjects의 요소에 있다면 else로 넘어가지 않고 이미 완료된 과목입니다.라는 문장을 띄우기 때문이다.
# 4. completed_subjects에 리스트가 아니라 세트를 사용한 이유는 무엇인가?
# 중복되는 요소를 저장하지 않기 위하여
# 5. 세트가 중복을 저장하지 않더라도 add() 전에 중복 검사를 별도로 하는 이유는 무엇인가?
# 원래 없던 것인지, 원래 있던 것인지, 새로 추가하는 것인지를 알려주기 위하여
# 세트는 중복 요소를 자동으로 저장하지 않으므로 중복 검사를 하지 않고 add()를 실행해도 결과는 같다.
# 하지만 미리 검사하면 새로 완료 처리된 것인지, 이미 완료된 과목인지 구분하여 안내할 수 있다.
#endregion
    elif menu == "4":
        print()
        print("=== 전체 학습 현황 ===")
        print("학생 번호:", student_info[0])
        print("학생 이름:", student_info[1])

        if len(study_order) == 0:
            print("등록된 학습 과목이 없습니다.")
        else:
            for subject in study_order:
                if subject in subject_scores:
                    score = subject_scores[subject]
                else:
                    score = "미등록"

                if subject in completed_subjects:
                    status = "완료"
                else:
                    status = "진행 중"

                print(f"{subject}/ 점수: {score}/ 상태: {status}")
#region
# 1. 전체 현황을 출력할 때 completed_subjects가 아니라 study_order를 for문으로 순회한 이유는 무엇인가?
# study_order에 subject_scores나 completed_subjects에 저장되지 않은 값이 있기 때문
# 보완:
# study_order에는 등록된 전체 학습 과목이 입력 순서대로 저장되어 있다.
# subject_scores에는 점수를 등록한 과목만 있고, completed_subjects에는 완료한 과목만 있으므로 전체 과목을 출력하려면 study_order를 순회해야 한다.
# 2. subject in subject_scores는 무엇을 검사하는가?
# subject에 저장된 값이 subject_scores의 요소에 존재하는지 비교해본다
# # 수정:
# subject에 저장된 값과 같은 key가 subject_scores 딕셔너리에 존재하는지 검사한다..
# 3. Git의 점수가 "미등록"으로 출력되는 이유는 무엇인가?
# Git에는 점수를 저장하지 않았기 때문
# 4. subject in completed_subjects가 참이면 status에는 무엇이 저장되는가?
# 완료
# 5. Python과 Git이 입력한 순서대로 출력되는 이유는 무엇인가?
# for문에서 iterable을 []형태인 study_order를 사용했기 때문이다.
#endregion
    elif menu == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 메뉴를 선택하세요.")

#region
# 1. student_info에 튜플을 사용한 이유는 무엇인가?
# 이 프로그램에서 학생 번호와 이름을 변경하지 않을 기본 정보로 정했기 때문이다.
# 2. study_order에 리스트를 사용한 이유는 무엇인가?
# 학습할 과목의 순서를 유지하고, 새로운 과목을 추가할 수 있기 때문이다.
# 3. subject_scores에 딕셔너리를 사용한 이유는 무엇인가?
# 과목과 점수를 연결하고, 과목으로 점수를 찾기 위함이다.
# 4. completed_subjects에 세트를 사용한 이유는 무엇인가?
# 중복으로 적은 과목은 제외하기 위함이다.
# 5. completed_subjects = {}라고 작성하면 어떤 자료형이 만들어지는가?
# 빈 dictionart로 만들어진다. set는 {element}이고, dictionary는 {key : value}로 구분된다.
#endregion

