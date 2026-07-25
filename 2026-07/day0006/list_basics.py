scores = [80, 95, 70]

print(scores)

print(scores[0])
print(scores[1])
print(scores[2])
#region 예상:
#[80,95,70]
#[80]
#[95]
#[70]
# 예상이 틀림. 인덱스로 꺼낸 값에는 대괄호가 없다.
#endregion
scores[0] = 85

print(scores)
print(scores[0])
#region 예상:
#[80, 95, 70]
#80
#95
#70
#[85, 95, 70]
#85
#endregion
scores.append(100)

print(scores)
print(len(scores))
#region 예상:
#[80, 95, 70]
#80
#95
#70
#[85, 95, 70]
#85
#[85, 95, 70, 100]
#4
#endregion

removed_score = scores.pop()

print(removed_score)
print(scores)
print(len(scores))
#region pop 실행 후 예상:
#removed_score:
#[100]
#scores:
#[85, 95, 70]
#len(scores):
#3
#예상이 틀림:
#removed_score:
#100이어야한다. []가 없다
#endregion

print(95 in scores)
print(100 in scores)
#region 예상:
#95
#존재하지 않는 값입니다.
#실제:
#True
#False
#틀린 이유:
#A in B는 B안에 A가 들어 있는지 확인,
#in은 True or False로 boolean으로 반환된다.
#in은 문장을 직접 출력하지 않는다.
#endregion

for score in scores:
    print(score)
#region 반복문 출력 예상:
#85
#95
#70
#endregion
