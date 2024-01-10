def solution(n, info):
    answer = []
    max_difference = 0

    arrows_to_point = [i + 1 for i in info]

    def iteration(ryan, left):
        nonlocal answer, max_difference

        if len(ryan) == 10:
            ryan = ryan + [left]
            difference = calculate_point(ryan, info)
            if difference > max_difference or (difference == max_difference and has_priority(ryan, answer)):
                answer = ryan
                max_difference = difference
            return

        iteration(ryan + [0], left)
        next_arrows = arrows_to_point[len(ryan)]
        if left >= next_arrows:
            iteration(ryan + [next_arrows], left - next_arrows)

    iteration([], n)

    return answer if max_difference != 0 else [-1]


def calculate_point(ryan, apeach):
    ryan_point = apeach_point = 0

    for i, (r, a) in enumerate(zip(ryan, apeach)):
        point = 10 - i
        if a == r == 0:
            continue
        elif r > a:
            ryan_point += point
        else:
            apeach_point += point

    return ryan_point - apeach_point


def has_priority(cur, before):
    for c, b in zip(reversed(cur), reversed(before)):
        if c > b:
            return True
        elif b > c:
            return False
