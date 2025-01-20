# Pascal Triangle.
# 1. find the element at that place R and C.
# 2. Print the Nth row of pascal triangle.
# 3. given N, print the entire triangle.

# given R and C print the element and the place 

def pascalElement(n, r):
    n, r = n-1, r-1
    res = 1
    for i in range(0, r):
        res = res * (n-i)
        res = res // (i+1)
    return res

# print(pascalElement(5, 3))

# brute force 

# 2. print nth row of pascal triangle.

def printNRowBF(n):
    res = []
    for i in range(1, n+1):
        response = pascalElement(n, i)
        res.append(response)
    return res

# print(printNRowBF(6))

def printNRowB(n):
    res = []
    ans = 1
    res.append(1)

    for i in range(1, n):
        ans = ans * (n-i)
        ans = ans // (i)
        res.append(ans)
    return res

print(printNRowB(6))

# optimal approach.

def pascalTriO(n):
    finalArr = []
    for i in range(1, n+1):
        response = printNRowB(i)
        finalArr.append(response)
    return finalArr

ans = pascalTriO(6)
print(ans)

