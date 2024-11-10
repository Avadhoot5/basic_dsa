# Get maze paths with jump value

def getMazePaths(sr, sc, dr, dc):

    if (sr == dr and sc == dc):
        return ['']

    paths = []

    for ms in range(1, (dr-sr)+1, dr, dc):
        hPath = getMazePaths(sr+1, sc, dr,dc)
        for prevH in hPath:
            paths.append('h' + ms + prevH)

    for ms in range(1, (dc-sc)+1, dr, dc):
        vPath = getMazePaths(sr, sc+1, dr,dc)
        for prevV in vPath:
            paths.append('v' + ms + prevV)

    for ms in range(1, (dc-sc)+1 and (dr-sr)+1, dr, dc):
        dPath = getMazePaths(sr+1, sc+1, dr,dc)
        for prevD in dPath:
            paths.append('d' + ms + prevD)

    return paths

ans = getMazePaths(1, 1, 3, 3)
print(ans)
