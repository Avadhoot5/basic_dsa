# Longest Consecutive Sequence 

nums = [0,3,7,2,5,8,4,6,0,1]
nums2 = [102,4,100,1,101,1,3,2]

# brute force approach.

def linearSearch(a, x):
    for i in range(len(a)):
        if (a[i] == x):
            return True
    return False

def longestSqBF1(arr):
    n = len(arr)
    longest = 1

    for i in range(0, n):
        cnt = 0
        x = arr[i]
        while (linearSearch(arr, x) == True):
            x += 1
            cnt += 1
        longest = max(longest, cnt)
    return longest

# print(longestSqBF1(nums))

# Better.

def longestSeqB(arr):
    arr.sort()
    if (len(arr) == 0):
        return 0
    n = len(arr)
    longest = 1
    lastSmall = -1000000
    cnt = 0

    for i in range(0, n):
        if (arr[i]-1 == lastSmall):
            cnt += 1
            lastSmall = arr[i]
        elif (arr[i] != lastSmall):
            cnt = 1
            lastSmall = arr[i]
        longest = max(cnt, longest)
    return longest

# print(longestSeqB(nums))

# my approach 

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

def longestSqO(arr):
    n = len(arr)
    setArr = set()
    for i in range(0, n):
        setArr.add(arr[i])
    
    longest = 1
    
    for i in setArr:
        if (i-1 not in setArr):
            x = i
            cnt = 1
            while (x+1 in setArr):
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    
    return longest


print(longestSqO(nums))
print(longestSqO(nums2))

