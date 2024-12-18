
# Longest subarray with given sum K(positives)

longArr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]

# TC. -> O(N*N*N). SC -> O(1)

def longestSubarrBF1(arr, k):
    length = 0
    n = len(arr)

    for i in range(0, n):
        for j in range(i, n):
            currentSum = 0
            for s in range(i, j+1):
                currentSum += arr[s]
            if (currentSum == k):
                length = max(length, j-i+1)
    return length

# print(longestSubarrBF1(longArr, 3))

# TC -> O(N*N). SC -> O(1)

def longestSubarrBF2(arr, k):
    length = 0
    n = len(arr)
    
    for i in range(0, n):
        currentSum = 0
        for j in range(i, n):
            currentSum += arr[j]
            if (currentSum == k):
                length = max(length, j-i+1)
    return length

# print(longestSubarrBF2(longArr, 6))

# better approach 

longArrB =[1, 2, 3, 0, 0, 1, 1, 1, 4, 2, 3]

def longestSubarrB(arr, k):
    n = len(arr)
    length = 0
    prefixSum = {}
    currentSum = 0

    for i in range(0, n):
        currentSum += arr[i]    
        if (currentSum == k):
            length = max(length, i+1)
        rem = currentSum - k
        if (prefixSum.get(rem)):
            currentLen = i - prefixSum[rem]
            length = max(currentLen, length)
        prefixSum[currentSum] = i

    return length

print(longestSubarrB(longArrB, 3))

