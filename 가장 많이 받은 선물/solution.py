def solution(friends, gifts):
    fmap = {x: {y: 0 for y in friends if x != y} for x in friends}
    gmap = {x: 0 for x in friends}
    tmap = {x: 0 for x in friends}

    for gift in gifts:
        g, t = gift.split()
        fmap[g][t] += 1
        gmap[g] += 1
        tmap[t] += 1

    ngifts = {x: 0 for x in friends}
    for g in friends:
        for t in friends:
            if g == t:
                continue

            if fmap[g][t] > fmap[t][g] or (fmap[g][t] == fmap[t][g] and (gmap[g] - tmap[g]) > (gmap[t] - tmap[t])):
                ngifts[g] += 1

    return max(ngifts.values())
