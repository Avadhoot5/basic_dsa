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

# print(insertionSort(insertArr))

# Merge Sort - divide and merge

# Two merge sort - uses iterative method

# Merge - Two sorted list into one list that is also sorted 
# Algorithm 

arr1 = [9, 13, 20, 24, 46, 52]
arr2 = [2, 3, 5, 6, 8, 16]

def twoWayMerge(A, B, m, n):
    i, j, k = 0, 0, 0
    temp = [0] * (m + n)

    while (i < m and j < n):
        if (A[i] <= B[j]):
            temp[k] = A[i]
            i += 1
            k += 1
        else:
            temp[k] = B[j]
            j += 1
            k += 1
    for rem in range(i, m):
        temp[k] = A[rem]
        k += 1
    
    for rem in range(j, n):
        temp[k] = B[rem]
        k += 1
    return temp

# print(twoWayMerge(arr1, arr2, len(arr1), len(arr1)))

# Merge Sort - uses recursive method

mergeArr = [3,4,1,6,2,5,7]

def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []

    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while (left <= mid):
        temp.append(arr[left])
        left += 1
    while (right <= high):
        temp.append(arr[right])
        right += 1

    for i in range(low, high):
        arr[i] = temp[i - low]

def mergeS(arr, low, high):
    if (low >= high):
        return
    mid = (low + high) // 2
    mergeS(arr, low, mid)
    mergeS(arr, mid + 1, high)
    merge(arr, low, mid, high)

def mergeSort(arr, n):
    mergeS(arr, 0, n-1)

# mergeSort(mergeArr, len(mergeArr))
# print(mergeArr)

# Quick sort
quickArr = [4, 6, 2, 5, 7, 9, 1, 3]

pivotLastArr1 = [9,2,6,9,1,4,4,3]

# descending code 

def partitionDesc(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while (i < j):
        while (arr[i] >= pivot and i <= high-1):
            i += 1
        while (arr[j] < pivot and j >= low + 1):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    
    return j

def quickSortDesc(arr, low, high):
    if (low < high):
        pIndex = partitionDesc(arr, low, high)
        quickSortDesc(arr, low, pIndex-1)
        quickSortDesc(arr, pIndex+1, high)
        return arr

# ans = quickSortDesc(pivotLastArr1, 0, len(pivotLastArr1)-1)
# print(ans)

# ascending code - using last element pivot

pivotLastArr2 = [9,2,6,9,1,4,4,3]

def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[high]

    while (i < j):
        while (arr[i] < pivot and i <= high - 1):
            i += 1
        while (arr[j] >= pivot and j >= low + 1):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i] = arr[i], arr[high]
    return i

def quickSort(arr, low, high):
    if (low < high):
        pIndex = partition(arr, low, high)
        quickSort(arr, low, pIndex-1)
        quickSort(arr, pIndex+1, high)
        return arr

# ans = quickSort(pivotLastArr2, 0, len(pivotLastArr2)-1)
# print(ans)

# Recursive Bubble Sort Algorithm

bubbleArrT = [13, 46, 24, 52, 20, 9]

def recBubble(arr, n):
    if (n == 1):
        return arr
    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            arr[i+1], arr[i] = arr[i], arr[i+1]
    return recBubble(arr, n-1)

# print(recBubble(bubbleArrT, len(bubbleArrT)))

# Recursive Insertion Sort Algorithm

recinsertArr = [13, 46, 24, 52, 20, 9]

def recInsert(arr, n, i):
    if (i == n):
        return arr
    for j in range(i, 0, -1):
        if (arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]

    return recInsert(arr, n, i+1)

# print(recInsert(recinsertArr, len(recinsertArr), 0))

