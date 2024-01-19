from itertools import combinations, chain
from collections import deque


def solution(relation):
    row, col = len(relation), len(relation[0])
    columns = deque(chain(*[combinations(range(col), x) for x in range(1, col + 1)]))

    result = 0
    while columns:
        indices = columns.popleft()
        cond = set([tuple([r[i] for i in indices]) for r in relation])

        if len(cond) == row:
            result += 1
            columns = deque(filter(lambda column: not set(column) > set(indices), columns))

    return result


print(solution([["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))
