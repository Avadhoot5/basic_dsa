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

# factorial of n 

def factorial(n):
    if (n == 1):
        return 1
    ans = factorial(n-1)
    res = ans * n
    return res

# print(factorial(5))

# power of n

def powX(x, n):
    if (n == 0): return 1
    return x * powX(x, n-1)

# print(powX(5, 3))

# power of n log time 

def powLog(x, n):
    if (n == 0): return 1
    half = powLog(x, n // 2)
    if (n % 2 == 0):
        return half * half
    else:
        return x * half * half

# print(powLog(5, 3))

# Print zig zag

def pred(n):
    if (n == 0): return
    print('Pre' + str(n))
    pred(n-1)
    print('In' + str(n))
    pred(n-1)
    print('Post' + str(n))

# pred(2)

# tower of hanoi

def toh(n, A, B, C):
    if (n == 0):
        return
    toh(n-1, A, C, B)
    print(n, A, B)
    toh(n-1, C, B, A)

# toh(3, 'A','B','C')







