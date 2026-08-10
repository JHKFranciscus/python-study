stations = [
    {
        "name": "A",
        "measurements": [18, 21, 25]
    },
    {
        "name": "B",
        "measurements": [13, 15]
    },
    {
        "name": "C",
        "measurements": [27, 30, 24]
    }
]

def highest(values):
    current = values[0]

    for value in values:
        if value > current:
            current = value

    return current


for station in stations:
    result = highest(station["measurements"])
    print(station["name"], result)

# # 문제 A
# 각 항목에 정확히 무엇이 들어 있는지 적어라.

# 1. stations
# - collection 전체
# - [{"name": "A", "measurements": [18, 21, 25]}, {"name": "B", "measurements": [13, 15]}, {"name": "C", "measurements": [27, 30, 24]}]

# 2. 첫 번째 반복의 station
# - 요소 하나
# - {"name": "A", "measurements": [18, 21, 25]}

# 3. 첫 번째 반복의 station["measurements"]
# - collection 전체
# - [18, 21, 25]

# 4. highest(station["measurements"])가 호출될 때 values
# - collection 전체
# - [18, 21, 25], [13, 15], [27, 30, 24]

# 5. for value in values:의 첫 번째 반복에서 value
# - 단일 값
# - 18

# 6. 첫 번째 highest() 호출이 끝난 직후 result
# - 단일 값
# - 25


# # 문제 B
# 다음 네 문장이 맞는지 틀리는지 판단하고 이유를 한 줄씩 적어라.
# ① station에는 stations 전체가 들어온다.
# stations의 요소 중 하나가 들어오는 것이기 때문에 틀리다.

# ② highest()의 values에는 station 하나가 들어온다.
# satation의 "measurements"라는 키를 가진 요소의 값이 들어 가는 것이기 때문에 아니다. 그런데 그 값이 단일 값이 아니라 collection이다.

# ③ value에는 측정값 하나가 들어온다.
# list collection의 요소 중 하나인 측정값 하나가 들어간다.

# ④ result에는 highest 함수 자체가 들어온다.
# result = highest(station["measurements"])이므로 highest함수의 결과값이 들어간다.


# 문제 C — 가장 중요

# 아래 흐름을 실제 값으로 채워라.

# 첫 번째 반복만 추적하면 된다.

# stations
#    ↓ for
# station = {"name": "A", "measurements": [18, 21, 25]}

# station["measurements"] = [18, 21, 25]

#    ↓ highest(station["measurements"])

# values = [18, 21, 25]

#    ↓ for
# value = 18

#    ↓ 계산 완료
# return 18

#    ↓ 호출부로 복귀
# result = 18



# stations는 list 객체
# station는 dict 객체
# values는 measurements값을 인자로 받는데 이는 list 객체이고
# values는 list 객체
# value는 iterator이자 values(list 객체) 내부의 요소인데 이를 뭐라고 하지?