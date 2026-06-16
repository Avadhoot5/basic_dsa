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
    # upper part
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*', end='')
        print(' ' * (2* (n-i)),end='')
        for k in range(1, i+1):
            print('*', end='')
        print()
    # lower part
    for i in range(1, n):
        for j in range(n-i, 0, -1):
            print('*', end='')
        print(' ' * (2*i) , end='')
        for j in range(n-i, 0, -1):
            print('*', end='')
        print()

# pattern20(5)

def finalPattern(n):
    origN = n
    n = (2*n)-1
    for i in range(0, n):
        for j in range(0, n):
            top = i
            down = n - i - 1
            left = j
            right = n - j - 1
            val = min(top, left, down, right)
            print(origN - val, end='')

        print()
    
# finalPattern(4)

# link - https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa

def p_pattern_1(n):
    for i in range(0, n):
        print('*' * n)

# p_pattern_1(5)

def p_pattern_2(n):
    for i in range(1, n+1):
        print('*' * i)

# p_pattern_2(5)

def p_pattern_3(n):
    num = ''
    for i in range(1, n+1):
        num += str(i)
        print(num)

# p_pattern_3(5)

def p_pattern_4(n):

    for i in range(1,n+1):
        print(str(i) * i)

# p_pattern_4(5)

def p_pattern_5(n):
    for i in range(n):
        print('*' * (n-i))

# p_pattern_5(5)

def p_pattern_6(n):
    for i in range(n, 0, -1):
        ans = ''
        for num in range(1, i+1):
            ans += str(num)
        print(ans)

# p_pattern_6(5)
        
def p_pattern_7(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end = '')
        print('*' * ((2*i)-1))

# p_pattern_7(5)

def p_pattern_8(n):
    for i in range(n, 0, -1):
        print(' ' * (n-i), end = '')
        print('*' * ((2*i)-1))

# p_pattern_8(5)
        

def p_pattern_9(n):
    for i in range(1, (2*n)+1):
        if (i<=n):
            print(' ' * (n-i), end='')
            print('*' * ((2*i)-1))
        else:
            print(' ' * (i-n-1), end='')
            print('*' * (2*(2*n-i)+1))

# p_pattern_9(5)

def p_pattern_10(n):
    for i in range(1, (2*n)):
        if (i<=n):
            print('*' * i)
        else:
            print('*' * ((2*n)-i))

# p_pattern_10(5)
        

def p_pattern_11(n):
    start = 1

    for i in range(1, n+1):
        if (i % 2 == 0): start = 0
        else: start = 1
        for j in range(1, i+1):
            print(start, end='')
            start = 1-start
        print()

# p_pattern_11(5)

def p_pattern_12(n):

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        
        print(' ' * (2*(n-i)), end='')

        for k in range(i, 0, -1):
            print(k, end='')
        print()

# p_pattern_12(5)

def p_pattern_13(n):
    value = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(value, end =' ')
            value += 1
        print()

# p_pattern_13(5)
        
def p_pattern_14(n):
    
    for i in range(65, 65+n):
        for j in range(65, i+1):
            print(chr(j), end ='')
        print()

# p_pattern_14(5)

def p_pattern_15(n):
    
    for i in range(5, 0, -1):
        for j in range(65, i+65):
            print(chr(j), end='')
        print()

# p_pattern_15(5)
        
def p_pattern_16(n):
    
    for i in range(0, n):
        print(chr(i+65) * (i+1))

# p_pattern_16(5)
        
def p_pattern_17(n):

    for i in range(65, 65+n):
        print(' ' * ((65+n)-i), end='')
        for j in range(65, i):
            print(chr(j), end='')
        for k in range(i, 64, -1):
            print(chr(k), end='')
        print()

# p_pattern_17(5)s

def p_pattern_18(n):

    for i in range(65+n, 64, -1):
        for k in range(i, 65+n):
            print(chr(k), end='')
        print()

# p_pattern_18(5)
        
def p_pattern_19(n):
    
    for i in range(1, (2*n)+1):
        if (i <= n):
            print('*' * (n-i+1), end='')
            print(' ' * ((2*i)-2), end='')
            print('*' * (n-i+1), end='')
        else:
            print('*' * (i-n), end='')
            print(' ' * (2*((2*n)-i)), end='')
            print('*' * (i-n), end='')
        print()

# p_pattern_19(5)
        
def p_pattern_20(n):
    
    for i in range(1, (2*n)+1):
        if (i <= n):
            print('*' * i, end='')
            print(' ' * (2*(n-i)), end='')
            print('*' * i, end='')
        else:
            print('*' * ((2*n) - i), end='')
            print(' ' * (2*(i-n)), end='')
            print('*' * ((2*n) - i), end='')

        print()

# p_pattern_20(5)

def p_pattern_21(n):
    
    for i in range(1, n+1):
        if (i == 1 or i == n):
            print('*' * n)
        else:
            for j in range(1, n+1):
                if (j==1 or j == n): print('*', end='')
                else: print(' ', end='')
            print()

# p_pattern_21(5)
        
def p_pattern_22(n):
    original_N = n
    n = 2*n-1
    
    for i in range(0, n):
        for j in range(0, n):
            top = i
            left = j
            bottom = n-i-1
            right = n-j-1

            value = min(top, left, bottom, right)
            print(original_N-value, end='')

        print()

# p_pattern_22(4)

