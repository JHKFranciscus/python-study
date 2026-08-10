students = [
    {"name": "민수", "scores": [80, 90]},
    {"name": "지수", "scores": [70, 85, 95]},
    {"name": "현우", "scores": [100, 90]}
]


def total_scores(scores):
    total = 0

    for score in scores:
        total += score

    return total


def make_result(name, total):
    return name + ": " + str(total)

student = students[1]

score_total = total_scores(student["scores"])

result = make_result(student["name"], score_total)

print(result)


# # A. collection과 요소 구분

# students =
# - collection 전체
# - [{"name": "민수", "scores": [80, 90]}, {"name": "지수", "scores": [70, 85, 95]}, {"name": "현우", "scores": [100, 90]}]


# student =
# - 요소 하나
# - {"name": "지수", "scores": [70, 85, 95]}

# student["scores"] =
# - collection 전체
# - [70, 85, 95]

# total_scores() 내부의 score =
# - 요소 하나

# # B. 첫 번째 함수 호출 역추적

# score_total = total_scores(student["scores"])

# 호출부의 student = {"name": "지수", "scores": [70, 85, 95]}
# 호출부의 student["scores"] = [70, 85, 95]

# ↓

# total_scores의 scores = [70, 85, 95]

# ↓

# 첫 번째 반복에서 score = 70
# 두 번째 반복에서 score = 85
# 세 번째 반복에서 score = 95

# ↓

# total_scores가 반환하는 값 = 250

# ↓

# score_total = 250


# # C. 두 번째 함수 호출 역추적

# result = make_result(student["name"], score_total)

# 첫 번째 인수 student["name"]의 현재 값 = "지수"
# 두 번째 인수 score_total의 현재 값 = 250

# ↓

# make_result의 name = "지수"
# make_result의 total = 250

# ↓

# make_result가 반환하는 값 = 지수:250

# ↓

# result = 지수:250


# # D. 판단 문제

# 1. make_result()의 total에 [70, 85, 95]가 들어가는가?
# 들어가지 않는다.
# 2. score_total에 현재 무엇이 들어 있는지 모른다면 어느 줄부터 역추적해야 하는가?
# total_scores(student["scores"])
# #[수정]
# #score_total = total_scores(student["scores"])
# 3. total_scores()의 scores와 내부 반복문의 score는 무엇이 다른가?
# 전자는 collection 전체라면 후자는 element 하나이다.
# 4. make_result(student["name"], score_total)의 두 번째 인수 score_total의 값은 최초에 어디에서 만들어졌는가?
# total_scores(student["scores"])