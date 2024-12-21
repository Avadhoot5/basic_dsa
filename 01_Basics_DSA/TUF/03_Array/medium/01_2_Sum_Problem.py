# Two sum problem 

# arr = [], target = k

# two types - 1. If sum exists return Yes/No. 2. Sum do exist return the indexes of the elements

inputArr = [2, 6, 5, 8, 11]

# TC. O(N*N). SC. O(1)

def twoSumProblemBF(arr, k):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                continue
            if ((arr[i] + arr[j]) == k):
                return i, j
    return 'No'

# print(twoSumProblemBF(inputArr, 13))

# TC. O(N*N). bit less than O(N2) 

def twoSumProblemBF2(arr, k):
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] == k):
                return i, j
    return -1

# print(twoSumProblemBF2(inputArr, 17))

def twoSumProblemB(arr, k):
    hashMap = {}
    currentSum = 0

    for i in range(0, len(arr)):
        currentSum += arr[i]
        hashMap[currentSum] = i
        diff = k - arr[i]
        if (hashMap.get(diff)):
            return hashMap[diff]

print(twoSumProblemB(inputArr, 17))

# optimal approach 

def twoSumProblemO(arr,k):
    pass

print(twoSumProblemO(inputArr, 17))
