def solution(places):
    return [validate(place) for place in places]


def validate(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and not valid(place, i, j):
                return 0

    return 1


def valid(place, y, x):
    if is_person(place, y + 1, x):
        return False
    if is_person(place, y, x + 1):
        return False

    if is_person(place, y + 2, x) and not is_partition(place, y + 1, x):
        return False
    if is_person(place, y, x + 2) and not is_partition(place, y, x + 1):
        return False

    if is_person(place, y + 1, x + 1) and not (is_partition(place, y, x + 1) and is_partition(place, y + 1, x)):
        return False
    if is_person(place, y + 1, x - 1) and not (is_partition(place, y, x - 1) and is_partition(place, y + 1, x)):
        return False

    return True


def is_person(place, y, x):
    return in_boundary(y, x) and place[y][x] == 'P'


def is_partition(place, y, x):
    return place[y][x] == 'X'


def in_boundary(y, x):
    return 0 <= y < 5 and 0 <= x < 5


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
