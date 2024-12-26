# Majority Element I | Brute-Better-Optimal | Moore's Voting Algorithm 

majorityArr = [2, 2, 3, 3, 1, 2, 2]

# BF. TC O(N*N)

def majorityElementBF(arr):
    n = len(arr)

    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if (arr[j] == arr[i]):
                count += 1
        if (count > (n//2)):
            return arr[i]

# print(majorityElementBF(majorityArr))

# better solution. SC O(N). TC O(NlogN) + O(N)

def majorityElementB(arr):
    hashMap = {}
    n = len(majorityArr)
    
    for i in range(0, n):
        if (arr[i] in hashMap):
            hashMap[arr[i]] += 1
        else:
            hashMap[arr[i]] = 1
    
    for i in hashMap:
        if (hashMap[i] > (n/2)):
            return i

    return -1

# print(majorityElementB(majorityArr))


