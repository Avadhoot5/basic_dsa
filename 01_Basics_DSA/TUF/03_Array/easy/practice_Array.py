# arrays in python

# arr = [0] * 6
# print(arr)

# 1. Largest Element in Array

oneArr = [3, 2, 1, 5, 2]

# brute force approach 

# we can sort the array and then return the last index. 
# sorting takes O(NlogN) time, S.C - O(1) - considering merge, quick sort

def largeElementBF(arr):
    arr.sort()
    return arr[-1]

# print(largeElementBF(oneArr))

# Optimal approach

# TC - O(N)

def largeElement(arr):
    max = 0
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]
    return max

# print(largeElement(oneArr))

# 2. Second largest element in an array

secondArr = [42,7,19,3,88,56,91,14,27,65]

def secondLargestO(arr):
    large, second = arr[0], -1

    for i in range(0, len(arr)):
        if (arr[i] > large):
            second = large
            large = arr[i]
        elif (arr[i] < large and arr[i] > second):
            second = arr[i]
    return second

# print(secondLargestO(secondArr))

def secondSmallest(arr):
    small = float('inf')
    secondSmall =  float('inf')

    for i in range(len(arr)):
        if (arr[i] < small):
            secondSmall = small
            small = arr[i]
        elif (arr[i] > small and arr[i] < secondSmall):
            secondSmall = arr[i]

    return -1 if secondSmall == float('inf') else secondSmall

# print(secondSmallest(secondArr))


# check if the array is sorted.

arr1 = [1, 2, 2, 3, 3, 4]
arr2 = [1,2,1,19,3,88,56,91,14,27,65]

def sortedArr(arr):
    n = len(arr)
    for i in range(1, n):
        if (arr[i] >= arr[i-1]):
            continue
        else:
            return False
    return True

# print(sortedArr(arr1))
# print(sortedArr(arr2))

# Remove duplicates from the sorted array.

dupArray = [1, 2, 3, 3, 4, 5, 5, 7, 8, 8]

# Bruteforce approach -

# 1. new array, copy unique elements.

def removeDuplicatesBF1(arr):
    temp = []
    for i in range(len(arr)):
        if not(arr[i] in temp):
            temp.append(arr[i])
    return len(temp)

# print(removeDuplicatesBF1(dupArray))

# 2. Similar implementation in set.

dupArray2 = [1,1,2,2,2,3,3]

def removeDuplicatesBF2(arr):
    temp = set(arr)
    return len(temp)

# print(removeDuplicatesBF2(dupArray2))

def removeDuplicateO(arr):
    i = 0
    n = len(arr)
    for j in range(1, n):
        if (arr[i] != arr[j]):
            arr[i+1] = arr[j]
            i += 1
    return i + 1

# print(removeDuplicateO(dupArray))
# print(removeDuplicateO(dupArray2))

# 1. Left Rotate array by 1.

rotateArr = [1,2,19,3,88,56,91,14,27,65]

def rotateArrByOne(arr):
    temp = arr[0]
    n = len(arr)

    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp

    return arr

# print(rotateArrByOne(rotateArr))

# 2. Left Rotate array by K places.

def rotateArrByDBF(arr, n, d):
    d = d % n
    temp = []

    for i in range(0, d):
        temp.append(arr[i])
    
    for i in range(d, n):
        arr[i-d] = arr[i]
    
    for i in range(n-d, n):
        arr[i] = temp[i-(n-d)]

    return arr

# print(rotateArrByDBF(rotateArr, len(rotateArr), 3))

# optimal solution

rotateArrO = [1,2,19,3,88,56,91,14,27,65]

def rotateArrByDO(arr, n, d):
    d = d % n
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])
    arr.reverse()
    return arr

# print(rotateArrByDO(rotateArrO, len(rotateArrO), 3))

# - without using STL

rotateArrO2 = [1,2,19,3,88,56,91,14,27,65]

# ans - [3, 88, 56, 91, 14, 27, 65, 1, 2, 19]

def rev(arr, start, end):
    while (start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def rotateArrByDO1(arr, n, d):
    d = d % n
    rev(arr, 0, d-1)
    rev(arr, d, n-1)
    return rev(arr, 0, n-1)

# print(rotateArrByDO1(rotateArrO2,  len(rotateArrO2), 3))

# Move Zeros to End 

# brute force - TC => O(N) + O(X) + O(N-X) => O(2N)
# SC => O(N) 

zeroArr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

def moveZeroBF(arr, n):
    temp = []

    for i in range(n):
        if not(arr[i] == 0):
            temp.append(arr[i])
    
    for i in range(0, len(temp)):
        arr[i] = temp[i]
        
    for i in range(len(temp), n):
        arr[i] = 0
    return arr

# print(moveZeroBF(zeroArr, len(zeroArr)))

def moveZeroO(arr, n):
    j = -1
    for i in range(n):
        if (arr[i] == 0):
            j = i
            break

    for i in range(j+1, n):
        if (arr[i] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

# print(moveZeroO(zeroArr, len(zeroArr)))

# Linear Search

linearArr = [42,7,19,3,88,56,91,14,27,65]

def findElement(arr, k):
    for i in range(len(arr)):
        if (arr[i] == k):
            return i
    return -1

# print(findElement(linearArr, 14))

# Union of two sorted arrays.

arrU1 = [1, 2, 2, 3, 4, 5, 6]
arrU2 = [2, 3, 4, 4, 7, 8]

# brute force approach 

def unionSortBF(arr1, arr2):
    unionSet = set()
    temp = []
    for i in arr1:
        unionSet.add(i)

    for i in arr2:
        unionSet.add(i)

    for i in unionSet:
        temp.append(i)
    return temp

# print(unionSortBF(arrU1, arrU2))

def unionSortO(a, b):
    temp = []
    i, j = 0, 0
    m = len(a)
    n = len(b)

    while (i < m and j < n):
        if (a[i] <= b[j]):
            if (len(temp) == 0 or temp[-1] != a[i]):
                temp.append(a[i])
            i += 1
        else:
            if (len(temp) == 0 or temp[-1] != b[j]):
                temp.append(b[j])
            j += 1
    while (i < m):
        if (len(temp) == 0 or temp[-1] != a[i]):
            temp.append(a[i])
        i += 1
    while (j < n):
        if (len(temp) == 0) or temp[-1] != b[j]:
            temp.append(b[j])
        j += 1
    return temp

# print(unionSortO(arrU1, arrU2))

# Intersection of Sorted Arrays 

arrI1 = [1, 2, 2, 3, 3, 4, 5, 6]
arrI2 = [2, 3, 3, 5, 6, 7, 8]

def intersectionBF1(a, b):
    visitedArr = [0] * len(b)
    temp = []

    for i in range(len(a)):
        for j in range(len(b)):
            if (a[i] == b[j] and visitedArr[j] == 0):
                temp.append(b[j])
                visitedArr[j] = 1
            if (b[j] > a[i]):
                break
    return temp

# print(intersectionBF1(arrI1, arrI2))

def intersectionO(a, b):
    i, j = 0, 0
    m = len(a)
    n = len(b)
    temp = []

    while (i < m and j < n):
        if (a[i] < b[j]):
            i += 1
        elif (b[j] < a[i]):
            j += 1
        else:
            temp.append(a[i])
            i += 1
            j += 1
    return temp

# print(intersectionO(arrI1, arrI2))

# missing number in an array


