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

