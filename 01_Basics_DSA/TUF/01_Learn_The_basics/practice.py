# Pattern problems. before starting DSA.

# 1. square problem

def squarePattern(n):
    for i in range(0, n):
        print('*' * n)

# squarePattern(5)

def triPattern(n):
    for i in range(0, n):
        print('*' * (i+1))

# triPattern(5)

def numPattern(n):
    for i in range(1, n+1):
        ans = ''
        for j in range(1, i+1):
            ans = ans + str(j) + ' '
        print(ans)

# numPattern(5)

def numPattern2(n):
    for i in range(1, n+1):
        ans = ''
        for j in range(1, i+1):
            ans += str(i)
        print(ans)

# numPattern2(5)

def downTri(n):
    for i in range(n, 0, -1):
        ans = ''
        for j in range(0, i):
            ans += '*'
        print(ans)

# downTri(5)

def downNumPattern(n):
    for i in range(n, 0, -1):
        ans = ''
        for j in range(1, i+1):
            ans += str(j)
        print(ans)

# downNumPattern(5)

def triPattern(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end = '')
        print('*' * ((2*i)-1), end = '')
        print(' ' * (n-i))

# triPattern(5)

def downTriPattern(n):
    for i in range(1, n+1):
        print(' ' * (i-1), end = '')
        print('*' * ((2 * (n-i)) + 1))

# downTriPattern(5)

def diamondPattern(n):
    for i in range(1, (2*n)+1):
        if (i <= n):
            print(' ' * (n-i),end ='')
            print('*' * ((2*i)-1))
        else:
            print(' ' * (i-n-1), end = '')
            print('*' * (2*(2*n-i)+1))

# diamondPattern(5)

def diamondTri(n):
    for i in range(1, 2*n):
        if (i <= n):
            print('*' * i)
        else:
            print('*' * ((2*n)-i))

# diamondTri(5)

def zeroOnePattern(n):
    start = 1
    for i in range(0, n):
        if (i % 2 == 0): start = 1
        else: start = 0
        for j in range(0, i+1):
            print(start, end = '')
            start = 1 - start
        print()

# zeroOnePattern(5)

def numVPattern(n):
    for i in range(1, n+1):
        ans = ''
        for j in range(1, i+1):
            ans += str(j)
        for sp in range(1, 2*(n-i)+1):
            ans += ' '
        for k in range(i, 0, -1):
            ans += str(k)

        print(ans)
        
# numVPattern(5)

def numFullPattern(n):
    ctr = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(f'{ctr} ', end = '')
            ctr += 1
        print()

# numFullPattern(4)

def pattern14(n):
    for i in range(65, 65 + n):
        for j in range(65, i+1):
            print(chr(j), end='')
        print()

# pattern14(5)

def pattern15(n):
    for i in range(65+n, 65, -1):
        for j in range(65, i):
            print(chr(j), end = '')
        print()

# pattern15(5)

def pattern16(n):
    for i in range(65, 65+n):
        for j in range(65, i+1):
            print(chr(i), end ='')
        print()

# pattern16(5)

def pattern17(n):
    for i in range(65, 65 + n):
        for sp in range(65+n, i, -1):
            print(' ', end='')
        for j in range(65, i+1):
            print(chr(j), end='')
        for k in range(i-1, 64, -1):
            print(chr(k), end='')
            pass
        print()

# pattern17(5)

def pattern18(n):
    for i in range(65+n-1, 64, -1):
        for j in range(i, 65+n):
            print(chr(j), end='')
        print()

# pattern18(5)

def pattern19(n):
    for i in range(1, (2*n)+1):
        if (i <= n):
            for sLeft in range(n-i+1, 0, -1):
                print('*', end='')
            for spTop in range(1, i):
                print(' ' * 2, end='')
            for sRight in range(n-i+1, 0, -1):
                print('*', end='')
        else:
            for dStar in range(1, i-n+1):
                print('*', end='')
            for spDown in range(2*((2*n)-i), 0, -1):
                print(' ', end ='')
            for dStar in range(1, i-n+1):
                print('*', end='')
            
        print()

# pattern19(4)

def pattern20(n):
    pass

pattern20(5)















