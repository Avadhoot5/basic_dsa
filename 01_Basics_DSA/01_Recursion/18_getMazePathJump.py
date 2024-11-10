# Get maze paths with jump value

def getMazePaths(sr, sc, dr, dc):

    if (sr == dr and sc == dc):
        return ['']

    paths = []

    for ms in range(1, (dr-sr)+1):
        hPath = getMazePaths(sr+ms, sc, dr,dc)
        for prevH in hPath:
            paths.append('h' + str(ms) + prevH)

    for ms in range(1, (dc-sc)+1):
        vPath = getMazePaths(sr, sc+ms, dr,dc)
        for prevV in vPath:
            paths.append('v' + str(ms) + prevV)

    for ms in range(1, (dc-sc)+1 and (dr-sr)+1):
        dPath = getMazePaths(sr+ms, sc+ms, dr,dc)
        for prevD in dPath:
            paths.append('d' + str(ms) + prevD)

    return paths

ans = getMazePaths(1, 1, 3, 3)
print(ans)
