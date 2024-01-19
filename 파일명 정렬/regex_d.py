import re


def solution(files):
    exp = re.compile(r'([\D]+)([\d]{1,6})')
    return sorted(files, key=lambda x: (exp.match(x)[1].lower(), int(exp.match(x)[2])))