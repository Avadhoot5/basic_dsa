# print stair paths

def getStairs(n, path):

    if (n == 0):
        print(path)
        return
    if (n < 0):
        return
    
    getStairs(n-1, '1' + path)
    getStairs(n-2, '2' + path)
    getStairs(n-3, '3' + path)


getStairs(4, '')
