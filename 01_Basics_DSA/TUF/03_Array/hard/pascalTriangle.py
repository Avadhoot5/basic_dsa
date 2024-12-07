# Pascal Triangle

# 3 types of questions - 
# 1. find the element at that place R and C.
# 2. Print the Nth row of pascal triangle.
# 3. given N, print the entire triangle.

# 1st type.

def elementnCr(n, r):
    res = 1
    for i in range(0, r):
        res = res * (n-i)
        res = res // (i+1)
    return res

# nCr = 5C3
# print(elementnCr(4, 2))

# TC. => O(r)
# SC. => O(1)

# 2nd type

# Brutre Force approach 
def pascalNtriBF(n):
    for i in range(1, n+1):
        value = elementnCr(n-1, i-1)
        print(value, end = '')

# pascalNtriBF(6)

