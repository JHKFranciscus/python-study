numbers = [4, 15, 8, 21, 10, 32]

total = 0
count = 0

for number in numbers:
    if number > 10:
        total += number
        count += 1

print(f"합: {total}")
print(f"개수: {count}")