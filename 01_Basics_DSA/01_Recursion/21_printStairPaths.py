# print stair paths

def getStairs(n, path):

    if (n == 0):
        print(path)
        return
    if (n < 0):
        return
    
    getStairs(n-1, path + '1')
    getStairs(n-2, path + '2')
    getStairs(n-3, path + '3')


getStairs(4, '')
