# Get Stairs Path - Question | Recursion

def getStairs(n):

    if (n == 0):
        return ['']
    if (n < 0):
        return []

    path1 = getStairs(n-1)
    path2 = getStairs(n-2)
    path3 = getStairs(n-3)

    paths = []
    
    for i in path1:
        paths.append('1' + i)
    for i in path2:
        paths.append('2' + i)
    for i in path3:
        paths.append('3' + i)
    
    return paths

ans = getStairs(4)
print(ans)
