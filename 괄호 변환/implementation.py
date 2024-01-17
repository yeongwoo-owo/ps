def solution(p):
    if not p:
        return ""

    u, v = separate(p)
    if is_correct(u):
        return u + solution(v)

    return f'({solution(v)}){flip(u[1:-1])}'


def separate(p):
    u = p[0]
    bias = bias_of(p[0])

    for ch in p[1:]:
        u += ch
        bias += bias_of(ch)
        if not bias:
            break

    return u, p[len(u):]


def is_correct(p):
    return p[0] == "("


def bias_of(ch):
    return 1 if ch == "(" else -1


def flip(p):
    return ''.join(["(" if x == ")" else ")" for x in p])


print(solution('(()())()'))
