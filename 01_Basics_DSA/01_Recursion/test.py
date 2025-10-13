# print decreasing values of n

def printDecrease(n):
    if (n == 0):
        return
    print(n)
    printDecrease(n-1)

# printDecrease(5)

def printIncrease(n):
    if (n == 0):return
    printIncrease(n-1)
    print(n)

# printIncrease(5)

def printIncreaseDecrease(n):
    if (n == 0):
        return
    print(n)
    printIncreaseDecrease(n-1)
    print(n)

# printIncreaseDecrease(5)





