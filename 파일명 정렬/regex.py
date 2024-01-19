import re


def solution(files):
    exp = re.compile(r'^(\D+)(\d{1,5})')
    return sorted(files, key=lambda x: (exp.match(x)[1].lower(), int(exp.match(x)[2])))


print(solution(["F -5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))