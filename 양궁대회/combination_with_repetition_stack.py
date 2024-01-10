def solution(n, info):
    answer = []
    max_difference = 0

    def iteration(ryan):
        nonlocal answer, max_difference

        if len(ryan) == n:
            ryan = convert(ryan)
            difference = calculate_point(ryan, info)
            if difference >= max_difference:
                answer = ryan
                max_difference = difference
            return

        last_point = ryan[-1] if ryan else 0
        for i in range(last_point, 11):
            stack.append(ryan + [i])

    stack = [[]]

    while stack:
        iteration(stack.pop())

    return answer if max_difference != 0 else [-1]


def convert(arr):
    return [arr.count(10 - i) for i in range(11)]


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
