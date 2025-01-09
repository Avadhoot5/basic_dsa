# Count Subarray sum Equals K 

longArr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
longArr2 = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]

# Brute force. TC. O(N*N). SC. O(1)

def longSubB(arr, k):
    count = 0
    n = len(arr)

    for i in range(0, n):
        currentSum = 0
        for j in range(i, n):
            currentSum += arr[j]            
            if (currentSum == k):
                count += 1
    return count

# print(longSubB(longArr2, 3))

# Better approch. TC. O(NlogN). SC. O()

def longSumO(arr, k):
    n = len(arr)
    hashMap = {}
    preSum = 0
    cnt = 0
    hashMap[0] = 1

    for i in range(0, n):
        preSum += arr[i]
        rem = preSum - k
        if (rem in hashMap):
            cnt += hashMap[rem]
        if (preSum in hashMap):
            hashMap[preSum] += 1
        else:
            hashMap[preSum] = 1
    return cnt


print(longSumO(longArr2, 3))

