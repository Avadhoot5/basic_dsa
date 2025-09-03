# Two sum problem 

# arr = [], target = k

# two types - 1. If sum exists return Yes/No. 2. Sum do exist return the indexes of the elements

twoArr = [2, 6, 5, 8, 11]

# TC. O(N*N). SC. O(1)

def twoSumProblemBF1(arr, k):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] == k):
                return [i, j]
    return 'NO'

# print(twoSumProblemBF1(twoArr, 16))

def twoSumProblemBetter(arr, k):
    n = len(arr)
    hashArr = {}

    for i in range(n):
        diff = k - arr[i]
        if (diff in hashArr):
            return 'YES'
        # [hashArr[diff], i]
        hashArr[arr[i]] = i
    return 'No'

# print(twoSumProblemBetter(twoArr, 16))

def twoSumProblemO(arr, k):
    arr.sort()
    n = len(arr)
    left = 0
    right = n-1

    while (left < right):
        currentSum = arr[left] + arr[right]
        if (currentSum == k):
            return 'YES'
        elif (currentSum < k):
            left += 1
        else:
            right -=1
    return 'NO'

# print(twoSumProblemO(twoArr, 16))

# Sort an array of 0's 1's & 2's - 

sortArr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]

def sortArrBF(arr):
    arr.sort()
    return arr

# print(sortArrBF(sortArr))

# Better approach

def sortArrBetter(arr):
    count0, count1, count2 = 0,0,0
    n = len(arr)

    for i in range(n):
        if (arr[i] == 0):
            count0 += 1
        elif (arr[i] == 1):
            count1 += 1
        else:
            count2 += 1
    
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, count0 + count1):
        arr[i] = 1
    for i in range(count0 + count1, n):
        arr[i] = 2
    return arr

# print(sortArrBetter(sortArr))

# DNF - dutch national flag algo 

def sortArrO(arr):
    n = len(arr)
    low, mid = 0, 0
    high = n-1

    while (mid <= high):
        if (arr[mid] == 0):
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif (arr[mid] == 1):
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

# print(sortArrO(sortArr))

# Majority Element I | Brute-Better-Optimal | Moore's Voting Algorithm 

majorityArr = [2, 2, 3, 3, 1, 2, 2]

def majorityElementBF(arr):
    n = len (arr)



print(majorityElementBF(majorityArr))




def majorityElementB(arr):
    pass









mergeArr = [3,4,1,6,2,5,7]

def mS(arr, low, mid, high):
    pass


