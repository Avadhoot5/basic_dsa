
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

