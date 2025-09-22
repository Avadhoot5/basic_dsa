# pascal triangle

def elementnCr(n, r):
    n, r = n-1, r-1
    res = 1

    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    
    return res

# nCr = 5C3
# print(elementnCr(5, 3))

def pascalNtriBF(n):
    for i in range(1, n+1):
        ans = elementnCr(n, i)
        print(ans, end = ' ')

pascalNtriBF(6) 
