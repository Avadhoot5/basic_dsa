
# Pattern problems. before starting DSA.

# 1. square problem

def square(n):
    for i in range(1, n+1):
        print(n * '*')

# square(5)

def triangle(n):
    for i in range(1, n+1):
        print(i * '*')

# triangle(5)

def triNum(n):
    val = ''
    for i in range(1, n+1):
        val += str(i)
        print(val)

# triNum(5)

def triNum2(n):
    for i in range(1, n+1):
        val = ''
        val += str(i) * i
        print(val)
    
# triNum2(5)

def opTri(n):
    for i in range(n, 0, -1):
        print('*' * i)

# opTri(5)

def numTri(n):
    for i in range(n, 0, -1):
        val = ''
        for j in range(1, i+1):
            val += str(j)
        print(val)

# numTri(5)

def centerTri(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end = '')
        print('*' * ((2*i)-1))

# centerTri(5)

def centerTriDown(n):
    for i in range(1, n+1):
        print('*' * ((2*(n-i))+1))
        print(' ' * (i), end = '')

centerTriDown(5)





