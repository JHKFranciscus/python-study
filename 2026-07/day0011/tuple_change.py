student_list = [101, "민수", 3]
print("변경 전:", student_list)

student_list[1] = "철수"
print("변경 후:", student_list)
#region
# 예상
# 변경 전: [101, '민수', 3]
# 변경 후: [101, '민수', 3]

# 예상:
# 튜플의 두 번째 요소가 "철수"로 변경될 것인가? 또는 오류가 발생할 것인가?
# 변경되지 않는다.
# 그렇게 예상한 이유: dictionary가 아닌 list이기 때문이다.

#[수정 후]
# 변경 전: [101, '민수', 3]
# 변경 후: [101, '철수', 3]
# list_var[index_num] = value는 기존의 index_num이 존재하면, 기존의 value를 변경하고, 기존의 index_num이 없으면, 오류가 난다.

# 리스트는 인덱스로 요소를 조회할 수 있을 뿐 아니라 해당 인덱스에 새로운 값을 대입하여 요소를 변경할 수도 있다.
# student_list[1]은 기존의 "민수"를 "철수"로 변경한다.
# list_var[index_num] = value는 해당 인덱스가 존재하면 그 위치의 기존 값을 새로운 값으로 변경한다. 존재하지 않는 인덱스를 사용하면 IndexError가 발생한다.
#endregion

student_tuple = (101, "민수", 3)
print("튜플 변경 전:", student_tuple)

student_tuple[1] = "철수"
print("튜플 변경 후:", student_tuple)
#region
# 튜플 예상:
# "튜플 변경 전"은 출력된다. student_tuple[1] = "철수"에서 오류가 발생한다. 따라서 "튜플 변경 후"는 출력되지 않는다.

# 그렇게 예상한 이유:
# 튜플은 인덱스로 요소를 조회할 수 있지만 만들어진 뒤 특정 요소를 새로운 값으로 변경할 수 없기 때문이다.
#endregion