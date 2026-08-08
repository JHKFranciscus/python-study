def get_average(scores):
    return sum(scores) / len(scores)


def get_max_score(scores):
    return max(scores)


if __name__ == "__main__":
    print("score_utils 직접 실행됨")
    print(get_average([70, 80, 90]))
