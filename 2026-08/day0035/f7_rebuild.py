shipments = [
    {"name": "A창고", "weights": [2, 3, 1]},
    {"name": "B창고", "weights": [4, 2]},
    {"name": "C창고", "weights": [1, 5, 2]}
]


#1. total_weights
# 함수로 만든다.
# 딕셔너리를 받아 숫자로 반환
def total_weights(shipment):
    total = 0
    weights = shipment["weights"]
    for weight in weights:
        total += weight
    return total

#2. to_str_kg / to_str_g
# 함수로 만든다
# 숫자를 받아 문자열로 반환
def to_str_kg(total_num):
    return f"{total_num}kg"

def to_str_g(total_num):
    return f"{total_num * 1000}g"

#3. select_unit
# 함수로 만든다
# 문자열을 받아 함수를 반환
def select_unit(mode):
    mode_dict = {"kg" : to_str_kg, "g" : to_str_g}
    return mode_dict[mode]

#5. 문자열 하나를 인수로 받는 decorator를 만든다.
# 함수로 만든다
# 바깥: 문자열을 받아 함수를 반환
# 가운데: 함수를 받아 함수를 반환
# 안쪽: 딕셔너리와 함수를 받아 문자열을 반환
def decorate(churi_status):
    def wrapper(func):
        def A(shipment, func2):
            result = func(shipment, func2)

            return f"[{churi_status}] {result}"

        return A
    
    return wrapper

#4. 선택된 함수를 다른 함수에 전달
# 함수로 만든다
# 딕셔너리와 함수를 받아서 문자열로 반환
@decorate("처리완료")
def status_shipment(shipment, func):
    total_weight = total_weights(shipment)
    weight_unit = func(total_weight)

    return f"{shipment["name"]}: {weight_unit}"

#6. 리스트에 모으고 출력하기
# 코드 블록
sumsum = []

mode = "g"
change_unit = select_unit(mode)

for shipment in shipments:
    a = status_shipment(shipment, change_unit)
    sumsum.append(a)

print(sumsum)





# 1 -> 4
# 2 -> 3
# 3 -> 4
# 4 -> 5
# 5 -> 6