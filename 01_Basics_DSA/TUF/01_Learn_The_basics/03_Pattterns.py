
# Pattern problems. before starting DSA.

# 1. square problem

def square(n):
    for i in range(1, n+1):
        print(n * '*')

# square(5)

def squareAlt(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print('*', end = '')
        print()

# squareAlt(5)

def triangle(n):
    for i in range(1, n+1):
        print(i * '*')

# triangle(5)

def triangleALt(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*', end = '')
        print()

# triangleALt(5)

def triNum(n):
    val = ''
    for i in range(1, n+1):
        val += str(i)
        print(val)

# triNum(5)

def triNumAlt(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end = '')
        print()

# triNumAlt(5)

def triNum2(n):
    for i in range(1, n+1):
        val = ''
        val += str(i) * i
        print(val)
    
# triNum2(5)

def triNum2Alt(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end='')
        print()

# triNum2Alt(5)

def opTri(n):
    for i in range(n, 0, -1):
        print('*' * i)

# opTri(5)

def opTriAlt(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+2):
            print('*', end = '')
        print()

# opTriAlt(5)

def numTri(n):
    for i in range(n, 0, -1):
        val = ''
        for j in range(1, i+1):
            val += str(j)
        print(val)

# numTri(5)

def numTriAlt(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+2):
            print(j, end = '')
        print()

# numTriAlt(5)

def centerTri(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end = '')
        print('*' * ((2*i)-1))

# centerTri(5)

def centerTriAlt(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(' ', end = '')
        for k in range(1, ((2*i)-1)+1):
            print('*', end = '')
        print()

# centerTriAlt(5)

def centerTriDown(n):
    for i in range(1, n+1):
        print('*' * ((2*(n-i))+1))
        print(' ' * (i), end = '')

# centerTriDown(5)

def centerTriDownAlt(n):
    for i in range(1, n+1):
        for j in range(1, i):
            print(' ', end = '')
        for k in range(1, (2*(n-i))):
            print('*', end = '')
        print()

# centerTriDownAlt(5)

def diamond(n):
    for i in range(1, (2*n)+1):
        if (i <= n):
            print(' ' * (n-i), end = '')
            print('*' * ((2*i)-1))
        else:
            print('*' * ((2*((2*n)-i))+1))
            print(' ' * (i-n), end = '')

# diamond(5)

def diamondAlt(n):
    for i in range(1, (2*n)):
        if (i <= n):
            for j in range(1, (n-i)+1):
                print(' ', end='')
            for k in range(1, (2*i)):
                print('*', end = '')
        else:
            for k in range(1, (i-n)+1):
                print(' ', end='') 
            for j in range(1, ((2*((2*n)-i)))):
                print('*', end = '')
        print()
        pass

# diamondAlt(5)

def triFull(n):
    for i in range(1, 2*n):
        if (i < n):
            print('*' * i)
        else:
            print('*' * ((2*n)-i))

# triFull(5)

# 11. Pattern ques -> 

def numTree(n):
    for i in range(1, n+1):
        val = '01'
        if (i % 2 == 0):
            print(val * (i//2), end ='')
        else:
            print('1' + (val * ((i-1)//2)), end ='')
        print()

numTree(5)
