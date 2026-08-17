numbers = [8, 13, 10, 17, 16]

max_increase_number = numbers[1] - numbers[0]

for i in range(1, len(numbers) -1):
    increase_number = numbers[i + 1] - numbers[i]

# for i in range(2, len(numbers)):
#     increase_number = numbers[i] - numbers[i - 1]

    if max_increase_number < increase_number:
        max_increase_number = increase_number

print(max_increase_number)
