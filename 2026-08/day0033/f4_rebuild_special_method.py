class NumberSequence:
    def __init__(self, start, final, step):
        self.start = start
        self.final = final
        self.step = step

    def __str__(self):
        return f"{self.start}부터 {self.final}까지 {self.step}씩 증가"

    # def __iter__(self):
    #     for i in list(range(self.start, self.final + 1, self.step)):
    #         if i % 2 != 0:
    #             continue
    #         else:
    #             yield i

    # def __iter__(self):
    #     generator = (
    #         number
    #         # for number in list(range(self.start, self.final + 1, self.step))
    #         for number in range(self.start, self.final +1, self.step)
    #         # if number % 2 == 0
    #         )
    #     return generator

    def __iter__(self):
        return iter(range(self.start, self.final +1, self.step))

    def __len__(self):
        # return len(list(self.__iter__()))
        # return (self.final - self.start) // self.step + 1
        return len(range(self.start, self.final + 1, self.step))

    def __eq__(self, other):
        return self.start == other.start and self.final == other.final and self.step == other.step

numbers = NumberSequence(2, 10, 2)
# 요구사항 1 — 객체 출력
print()
print(numbers)

# 요구사항 2 — 길이
print()
print(f"개수: {len(numbers)}")

# 요구사항 3 — 객체 자체 반복
print()
for number in numbers:
    print(number)

# 요구사항 4 — 같은 구간인지 비교
print()
numbers2 = NumberSequence(2, 10, 2)
numbers3 = NumberSequence(2, 10, 3)
print(numbers == numbers2)
print(numbers == numbers3)

# 요구사항 5 — 두 번 반복해도 다시 처음부터
print()
print("---")

for number in numbers:
    print(number)

















