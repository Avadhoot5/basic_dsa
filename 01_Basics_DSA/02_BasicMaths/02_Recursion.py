# Lec 5. Recursion 

# Sum of first n terms. eg n = 5. 13 + 23 + 33 + 43 + 53 = 225

# very high run time for recursive code 
def cubeNum(n):
    if (n == 0):
        return 0
    return n**3 + cubeNum(n-1)

# print(cubeNum(5))

# Basic recursion problems

# print name 5 times

def printName(n):
    if (n == 0):
        return
    print('name')
    printName(n-1)

# printName(5)

# recursion - print from 1 to n

def recPrint(n):
    if (n == 0):
        return
    recPrint(n-1)
    print(n)

# recPrint(8)

# print from n to 1 

def recPrint1ToN(n):
    if (n == 0):
        return
    print(n)
    recPrint1ToN(n-1)

# recPrint1ToN(5)

# backtrack 1 to n

def print1ToNBT(i, n):
    if (i == 0):
        return
    print1ToNBT(i-1, n)
    print(i)

# print1ToNBT(3,3)

# backtrack n to 1

def printNto1BT(i, n):
    if (i > n):
        return
    printNto1BT(i+1, n)
    print(i)

# printNto1BT(1, 3)

# sum of first N numbers. - 2 methods - parameterised way, functional way

def sumOfNnumParameter(i, sum):
    if (i < 1):
        print(sum)
        return
    sumOfNnumParameter(i-1, sum+i)

# sumOfNnumParameter(10, 0)

def sumOfNnum(n):
    if (n == 0):
        return 0
    return n + sumOfNnum(n-1)

# print(sumOfNnum(10))

def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

print(fact(4))

