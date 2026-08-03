names = ["서준", "유나", "도윤"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 예상 결과:
# 서준: 85점
# 유나: 92점
# 도윤: 78점
# 실제 결과:
# 서준: 85점
# 유나: 92점
# 도윤: 78점

print("--- zip 결과 확인 ---")

paired_data = list(zip(names, scores))
print(paired_data)

# paired_data의 자료형: list 자료형
# 이름과 점수를 묶은 내부 자료형: tuple 자료형

print("--- 길이가 다른 경우 ---")

cities = ["서울", "부산", "대전", "광주"]
temperatures = [31, 29, 30]

for city, temperature in zip(cities, temperatures):
    print(f"{city}: {temperature}도")

# 예상 결과:
# 서울: 31도
# 부산: 29도
# 대전: 30도
# 광주:
# 실제 결과:
# 서울: 31도
# 부산: 29도
# 대전: 30도
# 광주는 짝이 되는 온도가 없으므로 출력되지 않는다.

print("--- 직접 작성 ---")

menus = ["김밥", "라면", "떡볶이"]
prices = [3500, 4500, 5000]
stocks = [8, 0, 3]

for menu, price, stock in zip(menus, prices, stocks):
    print(f"{menu} / {price}원 / 재고 {stock}개")

# 1. zip()은 여러 리스트의 어떤 값들을 서로 묶는가?
# 답: iterable의 같은 index자리에 위치하는 요소들끼리 묶는다.
# 2. zip()에 넣은 리스트들의 길이가 다르면 어디까지 반복하는가?
# 답: 가장 짧은 리스트의 길이까지 반복한다.