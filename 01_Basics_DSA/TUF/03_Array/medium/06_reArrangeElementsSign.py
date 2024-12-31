# Rearrange Array Elements by Sign | 2 Varieties of same Problem

reArr = [3, 1, -2, -5, 2, -4]

# TC. O(2N). SC. O(N)

def rearrangeBF(arr):
    posArr = []
    negArr = []
    n = len(arr)

    for i in range(0, n):
        if (arr[i] < 0):
            negArr.append(arr[i])
        else:
            posArr.append(arr[i])
    arr = []
    for i in range(0, n//2):
        arr.append(posArr[i])
        arr.append(negArr[i])

    return arr

print(rearrangeBF(reArr))

# Optimal approach 

def rearrangeO(arr):
    finalArr = [0] * (len(arr))

    posIdx = 0
    negIdx = 1
    for i in range(0, len(arr)):
        if (arr[i] > 0):
            finalArr[posIdx] = arr[i]
            posIdx += 2
        else:
            finalArr[negIdx] = arr[i]
            negIdx += 2
    return finalArr

print(rearrangeO(reArr))

# variety 2  - no equal N//2.

def rearrangeOV(arr):
    n = len(arr)
    pos, neg = [], []

    for i in range(0, n):
        if (arr[i] < 0):
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    
    maxLen = max(len(pos), len(neg))

    for i in range(0, maxLen):
        arr[i*2] = pos[i]
        arr[i*2 + 1] = neg[i]
    
    idx = (2*maxLen)
    for i in range(maxLen, n):
        arr[idx] = pos[i]

    return arr


print(rearrangeOV(reArr))