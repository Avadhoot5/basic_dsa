# Kadane's Algorithm | Maximum Subarray Sum | Finding and Printing

inputArr = [-2, -3, 4, -1, -2, 1, 5, -3]

# brute force approach. TC. O(N*N*N). SC. O(1)

# better approach TC. O(N*N). SC. O(1) 

def maxSubarraySumB(arr):
    maxSum = 0
    n = len(arr)

    for i in range(0, n):
        currentSum = 0
        for j in range(i, n):
            currentSum += arr[j]
            if (currentSum > maxSum):
                maxSum = currentSum
    return maxSum

# print(maxSubarraySumB(inputArr))

# optimal Kadane's algo

import sys
min_int = -sys.maxsize - 1

inputArrN = [-2, -1]

def maxSubarraySumO(arr):
    maxSum = min_int
    n = len(arr)
    currentSum = 0

    for i in range(0, n):
        currentSum += arr[i]

        if (currentSum > maxSum):
            maxSum = currentSum

        if (currentSum < 0):
            currentSum = 0

    return maxSum

print(maxSubarraySumO(inputArrN))

# follow up que - print the subarray 


def maxSubarraySumO2(arr):
    maxSum = 0
    n = len(arr)
    currentSum = 0
    arrStart, arrEnd = -1, -1

    for i in range(0, n):
        if (currentSum == 0):
            start = i
        currentSum += arr[i]
        if (currentSum > maxSum):
            maxSum = currentSum
            arrStart = start
            arrEnd = i

        if (currentSum < 0):
            currentSum = 0

    return maxSum, arrStart, arrEnd

print(maxSubarraySumO2(inputArrN))

