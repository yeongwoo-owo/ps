def solution(n, k):
    nums = filter(lambda x: x, convert_base(n, k).split('0'))
    return len(list(filter(is_prime, map(int, nums))))


def convert_base(n, k):
    s = ''
    while n:
        s += str(n % k)
        n //= k
    return s[::-1]


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
