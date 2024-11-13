# print the maze Paths.

def mazePath(sr, sc, dr, dc, ans):
    
    if (sr == dr and sc == dc):
        print(ans)
        return

    if (sc < dc):
        mazePath(sr, sc + 1, dr, dc, ans + 'h')

    if (sr < dr):
        mazePath(sr + 1, sc, dr, dc, ans + 'v')


mazePath(1, 1, 3, 3, '')

