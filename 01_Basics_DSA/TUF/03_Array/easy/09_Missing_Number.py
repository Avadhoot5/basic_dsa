# missing number in an array

missNum = [9,6,4,2,3,5,7,0,1]

# BF -> TC = O(n*n) SC = O(1)

def missingNumBF1(arr):
    n = len(arr)
    for i in range(0, n):
        flag = 0
        for j in range(0, n):
            if(arr[j] == i):
                flag = 1
                break
    if (flag == 0):
        return i

# print(missingNumBF1(missNum))

def missingNumBF2(arr):
    for i in range(0, len(arr)):
        if not(i in arr):
            return i

# print(missingNumBF2(missNum))

# Optimal approach. TC -> O(N+M). SC -> O(N)
# hash arr approach

def missingNumBetter(arr):
    n = len(arr)
    hashArr = [0] * (n+1)
    for i in range(0, n):
        hashArr[arr[i]] = 1
    for i in range(0, len(hashArr)):
        if (hashArr[i] == 0):
            return i

# print(missingNumBetter(missNum))

# optimal solution - 2 methods

# 1. using SUM. TC => O(N). SC => O(1)

def missingNumO1(arr):
    n = len(arr)
    nSum = (n*(n+1))//2
    arraySum = 0
    for i in arr:
        arraySum += i
    return nSum - arraySum

print(missingNumO1(missNum))

# 2. XOR

def missingNumO2(arr):
    xor1, xor2 = 0, 0
    n = len(arr)
    for i in range(0,n):
        xor2 = xor2 ^ arr[i]
        xor1 = xor1 ^ (i)
    xor1 = xor1 ^ n
    return xor1 ^ xor2

print(missingNumO2(missNum))
