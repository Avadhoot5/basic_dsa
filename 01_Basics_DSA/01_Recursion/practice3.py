# Print Decreasing using recursion

def recDec(n):
    if (n == 0): return
    print(n)
    recDec(n-1)

# recDec(8)

# Print Increasing using Recursion

def recInc(n):
    if (n == 0): return
    recInc(n-1)
    print(n)

# recInc(8)

#  Print Decreasing Increasing Numbers using Recursion

def recDecInc(n):
    if (n == 0): return
    print(n)
    recDecInc(n-1)
    print(n)

# recDecInc(8)

# Factorial - Question | Recursion 

def fact(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact(n-1)

# print(fact(5))

# n power x

def pow(x,n):
    if (n == 0):
        return 1
    return x * (pow(x, n-1))

# print(pow(2, 5))

# n power x using log time

def powL(x, n):
    if (n == 0): return 1
    if (n % 2 == 0):
        return powL(x, n//2) * powL(x, n//2)
    else:
        return x * powL(x, n//2) * powL(x, n//2)

# print(powL(2, 5))

# predict the output

def pred(n):
    if (n == 0):
        return 
    print('Pre' + str(n))
    pred(n-1)
    print('In' + str(n))
    pred(n-1)
    print('Post' + str(n))

# pred(2)

# tower of hanoi
def towerOfHanoi(n, A, B, C):
    pass

# towerOfHanoi(2, 'A', 'B', 'C')
