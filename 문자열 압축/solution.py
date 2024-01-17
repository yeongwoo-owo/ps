def solution(s):
    if len(s) == 1:
        return 1
    return min(map(lambda x: compress(s, x), range(1, len(s) // 2 + 1)))


def compress(s, n):
    before = ""
    dup = 1
    result = 0

    for i in range(0, len(s), n):
        cur = s[i:i + n]
        if cur == before:
            dup += 1
        else:
            result += len(before) + (len(str(dup)) if dup > 1 else 0)
            before = cur
            dup = 1

    return result + len(before) + (len(str(dup)) if dup > 1 else 0)


print(solution("aabbaccc"))
