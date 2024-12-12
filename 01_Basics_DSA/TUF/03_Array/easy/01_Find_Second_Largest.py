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
    for i in range(0, len(arr)):
        if (arr[i] > max):
            max = arr[i]
    return max

# print(largeElement(oneArr))

# using recursion

def recMaxElement(arr, i):
    if (i == len(arr)-1):
        return arr[i]
    max = recMaxElement(arr, i+1)
    if (max > arr[i]):
        return max
    else:
        return arr[i]

# print(recMaxElement(oneArr, 0))

# 2. Second largest element in an array

secondArr = [42,7,19,3,88,56,91,14,27,65]

# brute force approach - 

# 1.
def secondLBF(arr):
    arrSet = set(arr)
    finalArr = sorted(arrSet)
    return finalArr[-2]

# print(secondLBF(secondArr))

# 2. TC - O(NlogN + N).

def secondLEBF(arr):
    arr.sort()
    large, second = arr[-1], 0
    for i in range(len(arr)-2, -1, -1):
        if (arr[i] != large):
            second = arr[i]
            break
    return second

# print(secondLEBF(secondArr))

# Better approach - T.C => O(N + N) = O(2N)

# first iterate and take the largest element, then again iterate and take the 2nd smallest element, less than the largest element. 

def secondLEB(arr):
    large = arr[0]
    for i in range(0, len(arr)):
        if (arr[i] > large):
            large = arr[i]
    secondL = -1
    for j in range(0, len(arr)):
        if (arr[j] > secondL and arr[j] < large):
            secondL = arr[j]
    return secondL

# print(secondLEB(secondArr))

# Optimal approach. TC - O(N)

def secondLO(arr):
    large, second = arr[0], -1
    for i in range(0, len(arr)):
        if (arr[i] > large):
            second = large
            large = arr[i]
        elif (arr[i] < large and arr[i] > second):
            second = arr[i]
    return second

# print(secondLO(secondArr))

def secondSO(arr):
    smallest = arr[0]
    secondSmallest = 0
    for i in range(0, len(arr)):
        if (arr[i] < smallest):
            secondSmallest = smallest
            smallest = arr[i]
        elif (arr[i] != smallest and arr[i] < secondSmallest):
            secondSmallest = arr[i]
    return secondSmallest

# print(secondSO(secondArr))

