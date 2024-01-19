def solution(record):
    logs = []
    names = {}

    for r in record:
        r = r.split()
        if r[0] == "Enter":
            logs.append((r[0], r[1]))
            names[r[1]] = r[2]
        elif r[0] == "Leave":
            logs.append((r[0], r[1]))
        else:
            names[r[1]] = r[2]

    result = []
    for tp, uid in logs:
        if tp == "Enter":
            result.append(f'{names[uid]}님이 들어왔습니다.')
        else:
            result.append(f'{names[uid]}님이 나갔습니다.')
    return result


print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))
