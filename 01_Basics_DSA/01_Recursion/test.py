# print decreasing values of n

def printDecrease(n):
    if (n == 0):
        return
    print(n)
    printDecrease(n-1)

# printDecrease(5)

def printIncrease(n):
    if (n == 0):return
    printIncrease(n-1)
    print(n)

# printIncrease(5)

def printIncreaseDecrease(n):
    if (n == 0):
        return
    print(n)
    printIncreaseDecrease(n-1)
    print(n)

# printIncreaseDecrease(5)

# factorial of n 

def factorial(n):
    if (n == 1):
        return 1
    ans = factorial(n-1)
    res = ans * n
    return res

# print(factorial(5))

# power of n

def powX(x, n):
    if (n == 0): return 1
    return x * powX(x, n-1)

# print(powX(5, 3))

# power of n log time 

def powLog(x, n):
    if (n == 0): return 1
    half = powLog(x, n // 2)
    if (n % 2 == 0):
        return half * half
    else:
        return x * half * half

# print(powLog(5, 3))

# Print zig zag

def pred(n):
    if (n == 0): return
    print('Pre' + str(n))
    pred(n-1)
    print('In' + str(n))
    pred(n-1)
    print('Post' + str(n))

# pred(2)

# tower of hanoi

def toh(n, A, B, C):
    if (n == 0):
        return
    toh(n-1, A, C, B)
    print(n, A, B)
    toh(n-1, C, B, A)

# toh(3, 'A','B','C')

# display an array 

# display an array using recursion

dislpayArr = [42,7,19,3,88,56,14,27,65,91]

def showArray(arr, idx):
    if (idx == len(arr)): return
    print(arr[idx])
    showArray(arr, idx+1)

# showArray(dislpayArr, 0)

def showArrayRev(arr, idx):
    if (idx == len(arr)): return
    showArrayRev(arr, idx+1)
    print(arr[idx])

# showArrayRev(dislpayArr, 0)

# print the maxium element of an array.

maxArr = [42,7,19,3,88,56,91,14,27,65]

def maxVal(arr, i):
    if (i == len(arr)-1): return arr[i]
    mesa = maxVal(arr, i+1)
    if (arr[i] > mesa):
        return arr[i]
    else:
        return mesa

# print(maxVal(maxArr, 0))

# First index ques.

firstArr = [2,5,7,8,2,6,8,1]

def firstOccr(arr, i, element):
    if (i == len(arr)): return -1
    if (arr[i] == element):
        return i
    else:
        return firstOccr(arr,i+1, element)

print(firstOccr(firstArr, 0, 8))


# Last index ques.
lastArr = [2,5,7,8,2,6,8,1]

def lastOccr(arr, i, element):
    if (i == len(arr)): return -1
    value = lastOccr(arr, i+1,element)
    if (value == -1):
        if (element == arr[i]):
            return i
        else:
            return -1
    return value

# print(lastOccr(lastArr, 0, 8))

# return all indices of an element in an array.

allArr = [2,5,7,8,2,6,9,2,8,1]








