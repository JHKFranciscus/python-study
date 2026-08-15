#문제 1
numbers = [-13, -5, -21, -2, -8]

largest = numbers[0]

for number in numbers:
    if largest < number:
        largest = number

print(largest)

#문제 2
print()
numbers2 = [-7, 3, 18, 5, 12]

largest = numbers2[0]
largest_index = 1

for index, number2 in enumerate(numbers2[1:], start=2):
    if largest < number2:
        largest = number2
        largest_index = index

print(largest)
print(largest_index)