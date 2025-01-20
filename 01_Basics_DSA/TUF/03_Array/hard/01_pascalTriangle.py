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

# better than above.

# TC - O(N)
# SC - O(1)

def pascalNtriBetter(n):
    ans = 1
    print(ans, end = ' ')
    for i in range(1, n):
        ans = ans * (n-i)
        ans = ans // i
        print(ans, end = ' ')

# pascalNtriBetter(6)

# 3rd Type 

def pascalRow(n):
    resultArray = []
    ans = 1
    resultArray.append(1)
    for i in range(1, n):
        ans = ans * (n-i)
        ans = ans // i
        resultArray.append(ans)
    return resultArray 

def pascalNtri(n):
    finalArr = []
    finalArr.append([1])
    for i in range(2, n+1):
        result = pascalRow(i)
        finalArr.append(result)
    return finalArr

ans = pascalNtri(6)
print(ans)



