# Selection sort

# select the minimum element and swap it.

# sudo code

inputArr = [13, 46, 24, 52, 20, 9]

def selection(arr):

    for i in range(0, len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr

# print(selection(inputArr))

# Bubble Sort

# push the max element using ajacent swaps 

bubbleArr = [13, 46, 24, 52, 20, 9]

def bubble(arr, n):
    for i in range(n-1, -1, -1):
        didSwap = 0
        for j in range(0, i):
            if (arr[j] > arr[j+1]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
                didSwap = 1
        if (didSwap == 0):
            break
    return arr

# print(bubble(bubbleArr, len(bubbleArr)))

# Insertion Sort

insertArr = [13, 46, 24, 52, 20, 9]

def insert(arr):

    for i in range(0, len(arr)):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr
print(insert(insertArr))


 