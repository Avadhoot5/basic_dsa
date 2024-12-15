# Max Consecutive number of 1's

oneArr = [1, 1, 0, 1, 1, 1, 0, 1, 1]

def maxOnes(arr):
    ctr, max = 0, 0
    for i in range(0, len(arr)):
        if (arr[i] == 1):
            ctr += 1
        else:
            ctr = 0
        if (ctr > max):
                max = ctr
    return max

print(maxOnes(oneArr))
