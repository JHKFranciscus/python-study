scores = [
    ("python", 80),
    ("flask", 70),
    ("python", 90),
    ("mongodb", 60),
    ("flask", 85),
    ("python", 70),
    ("mongodb", 90)
]

stats = {}

for score in scores:
    if score[0] in stats:
        stats[score[0]]["total"] += score[1]
        stats[score[0]]["count"] += 1
    else:
        stats[score[0]] = {
            "total": score[1],
            "count": 1
        }

print(stats)
print()

max_stat = None
max_average = 0

for stat in stats:
    average = stats[stat]["total"] / stats[stat]["count"]
    print(stat, average)

    if average > max_average:
        max_stat = stat
        max_average = average

print()
print(f"과목: {max_stat}")
print(f"평균: {max_average}")
