# Longest Consecutive Sequence 

nums = [0,3,7,2,5,8,4,6,0,1]
nums2 = [102,4,100,1,101,1,3,2]

# brute force approach.

def longestSqBF(arr):
    arr = list(set(arr))
    arr.sort()
    
    value, ctr = arr[0], 0
    maxCtr = 0

    for i in range(0, len(arr)):
        if (arr[i] != value):
            value = arr[i]
            ctr = 0
        ctr += 1
        value += 1
        maxCtr = max(ctr, maxCtr)

    return maxCtr

# print(longestSqBF(nums))
# print(longestSqBF(nums2))

# optimal approach 


