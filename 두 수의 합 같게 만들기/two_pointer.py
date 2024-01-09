def solution(queue1, queue2):
    target = sum(queue1 + queue2)
    if target % 2 != 0:
        return -1
    target //= 2

    queue = queue1 + queue2 + queue1

    start = 0
    end = len(queue1)

    count = 0
    cur = sum(queue1)
    while start < end < len(queue):
        if cur < target:
            cur += queue[end]
            end += 1
        elif cur > target:
            cur -= queue[start]
            start += 1
        else:
            return count
        count += 1

    return -1
