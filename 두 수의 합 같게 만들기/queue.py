from collections import deque


def solution(queue1, queue2):
    target = sum(queue1 + queue2)
    if target % 2 != 0:
        return -1
    target //= 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    count = 0
    cur = sum(queue1)
    max_count = len(queue1) * 3 - 3
    while count <= max_count:
        if cur > target:
            moved = queue1.popleft()
            queue2.append(moved)
            cur -= moved
        elif cur < target:
            moved = queue2.popleft()
            queue1.append(moved)
            cur += moved
        else:
            return count
        count += 1
    return -1
