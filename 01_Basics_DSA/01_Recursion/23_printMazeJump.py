# print the maze Paths.

def printMPJ(sr, sc, dr, dc, ans):

    if (sr == dr and sc == dc):
        print(ans)
        return
    
    for ms in range(1, (dr-sr)+1):
        printMPJ(sr+ms, sc, dr, dc, ans + 'h' + str(ms))

    for ms in range(1, (dc-sc)+1):
        printMPJ(sr, sc+ms, dr, dc, ans + 'v' + str(ms))

    for ms in range(1, (dr-sr)+1 and (dc-sc)+1):
        printMPJ(sr+ms, sc+ms, dr, dc, ans + 'd' + str(ms))

printMPJ(1, 1, 3, 3, '')

