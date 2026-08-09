# 문제 1
names = ["민수", "지수", "철수"]

for index, name in enumerate(names, start=1):
    print(index, name)

#예상 결과:
# 1 민수
# 2 지수
# 3 철수


# 문제 2
print()
names = ["민수", "지수", "철수"]
scores = [80, 90, 70]

result = [
    f"{name}:{score}"
    for name, score in zip(names, scores)
    if score >= 80
]

print(result)

# 예상 결과:
# [{민수 : 80}, {지수 : 90}]
#수정 후
#[민수 : 80, 지수 : 90]

# 작동 순서:
# 1. for name, score in zip(names, scores)
# 2. if score >= 80
# 3. f"{name}:{score}"


# 문제 3
print()
def numbers():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")

gen = numbers()

print("시작")
print(next(gen))
print("중간")
print(next(gen))

# 예상 결과:
# 시작
# A
# 10
# 중간
# B
# 20
