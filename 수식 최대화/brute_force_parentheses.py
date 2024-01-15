from itertools import permutations


def solution(expression):
    operators = list(permutations(['+', '-', '*']))
    return max(map(lambda x: abs(eval(add_parentheses(expression, list(x)))), operators))


def add_parentheses(exp: str, ops: list):
    if not ops:
        return exp

    op = ops[-1]
    return op.join([f'({add_parentheses(token, ops[:-1])})' for token in exp.split(op)])
