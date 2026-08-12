numbers = [4, 15, 7, 21, 10, 13]

count = 0

for number in numbers:
    if number > 10:
        count += 1

print(count)
#region
# number = 4
# 4 > 10 → False
# count = 0

# number = 15
# 15 > 10 → True
# count = 1

# number = 7
# 7 > 10 → False
# count = 1

# number = 21
# 21 > 10 → True
# count = 2

# number = 10
# 10 > 10 → False
# count = 2

# number = 13
# 13 > 10 → True
# count = 3
#endregion
scores = [
    {"name": "A", "score": 72},
    {"name": "B", "score": 48},
    {"name": "C", "score": 91},
    {"name": "D", "score": 65},
    {"name": "E", "score": 39}
]

total = 0

for score in scores:
    if score["score"] >= 60:
        total += score["score"]

print(total)

