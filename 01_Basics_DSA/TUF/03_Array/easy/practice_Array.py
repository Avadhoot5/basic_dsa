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

print(rotateArrByDBF(rotateArr, len(rotateArr), 3))


# optimal solution



rotateArrNew = [1,2,19,3,88,56,91,14,27,65]

# - without using STL






