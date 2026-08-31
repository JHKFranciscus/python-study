words = [
    "python",
    "flask",
    "python",
    "mongodb",
    "flask",
    "python",
    "ajax"
]

words_count = {}
max_word = None
max_count = 0


for word in words:
    if word in words_count:
        words_count[word] += 1

    else:
        words_count[word] = 1


print(words_count)


for word in words_count:
    if words_count[word] > max_count:
        max_word = word
        max_count = words_count[word]

print()
print(max_word)
print(max_count)

