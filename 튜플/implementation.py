def solution(s):
    sets = [set()] + sorted(map(lambda x: set(x.split(",")), s[2:-2].split("},{")), key=len)
    return [(a - b).pop() for a, b in zip(sets[1:], sets)]


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))