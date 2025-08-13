# sudo code

# Selection sort - select the minimum element and swap it.

inputArr = [13, 46, 24, 52, 20, 9]

def selectionSort(arr):
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# print(selectionSort(inputArr))

# Bubble Sort

# push the max element using ajacent swaps 

# bubbleArr = [13, 46, 24, 52, 20, 9]
bubbleArr = [1, 2, 3, 4, 5, 6]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):
        didSwap = 0
        for j in range(0, i):
            if (arr[j] > arr[j+1]):
                didSwap = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if (didSwap == 0):
                break
            print('runs')
    return arr

# print(bubbleSort(bubbleArr))

# Insertion Sort - takes an element and places it in its current position

insertArr = [13, 46, 24, 52, 20, 9]

def insertionSort(arr):
    n = len(arr)

    for i in range(0, n):
        j = i
        while (j > 0 and arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

print(insertionSort(insertArr))
