# Get maze paths 

def getMazePath(sr, sc, dr, dc):

    if (sr == dr and sc == dc):
        return ['']

    hPath = []
    vPath = []

    if (sc < dc):
        hPath = getMazePath(sr, sc+1, dr, dc)
    if (sr < dr):
        vPath = getMazePath(sr+1, sc, dr, dc)
    
    paths = []
    for i in hPath:
        paths.append('h' + i)
    for i in vPath:
        paths.append('v' + i)

    return paths

ans = getMazePath(1,1,3,3)
print(ans)
