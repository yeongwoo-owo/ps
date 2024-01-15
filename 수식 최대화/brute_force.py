from collections import deque
from itertools import permutations


def solution(expression):
    tokens = parse_token(expression)
    return max(map(lambda x: abs(calculate(deque(tokens), x)), permutations(['+', '-', '*'])))


def parse_token(exp):
    ops = ['+', '-', '*']
    tokens = []
    tmp = ''
    for ch in exp:
        if ch in ops:
            tokens.append(tmp)
            tokens.append(ch)
            tmp = ''
        else:
            tmp += ch

    tokens.append(tmp)
    return tokens


def calculate(exp, ops):
    for op in ops:
        tmp = deque()
        while exp:
            token = exp.popleft()
            if token == op:
                token = eval(f'{tmp.pop()}{op}{exp.popleft()}')
            tmp.append(token)
        exp = tmp
    return exp[0]
