# print from n to 1 and 1 to n

def printDecInc(n):
    if (n == 0):
        return
    print(n)
    printDecInc(n-1)
    print(n)
    
printDecInc(5)
