# Sort an array of 0, 1, and 2

# brute force. TC - O(NlogN) SC - O(N)

# using any of the sorting algo (built in library)

inputArr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]

def sortArrBF(arr):
    arr.sort()
    return arr

# print(sortArrBF(inputArr))

# Better approach

def sortArrB(arr):
    count0, count1, count2 = 0, 0, 0

    for i in range(0, len(arr)):
        if (arr[i] == 0):
            count0 += 1
        elif (arr[i] == 1):
            count1 += 1
        else:
            count2 += 1
    idx = 0
    for i in range(count0):
        arr[idx] = 0
        idx += 1

    for i in range(count1):
        arr[idx] = 1
        idx += 1
    
    for i in range(count2):
        arr[idx] = 2
        idx += 1
    
    return arr

# print(sortArrB(inputArr))

# optimal approach

def sortArrO(arr):
    n = len(arr)
    low, mid = 0, 0
    high = n-1

    while(mid <= high):
        if (arr[mid] == 0):
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif (arr[mid] == 1):
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr

print(sortArrO(inputArr))
