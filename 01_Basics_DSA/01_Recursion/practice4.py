# Print Decreasing using recursion

def printDec(n):
    if (n == 0): return
    print(n)
    printDec(n-1)

# printDec(5)

# Print Increasing using Recursion

def printInc(n):
    if (n == 0): return 
    printInc(n-1)
    print(n)

# printInc(5)

#  Print Decreasing Increasing Numbers using Recursion

def printIncDec(n):
    if (n == 0): return
    print(n)
    printIncDec(n-1)
    print(n)

# printIncDec(5)

# Factorial - Question | Recursion 

def fact(n):
    if (n == 0): return 1
    return n * fact(n-1)

# print(fact(5))

# Power (Linear) - Question

def powL(x, n):
    if (n == 0): return 1
    return x * powL(x, n-1)

print(powL(2, 5))
# print(powL(2, 8))

# Power (Linear) -  (Logarithmic) 

def powO(x, n):
    if (n == 0): return 1
    value = powO(x, n//2)
    if (n % 2 == 0):
        return value * value
    else:
        return x * value * value

print(powO(2, 5))
# print(powO(2, 8))

# Tower of Hanoi - Question

def toh(n, A, B, C):
    pass

# toh(3, 'A', 'B', 'C')






