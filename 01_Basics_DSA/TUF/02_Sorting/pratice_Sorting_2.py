# Selection sort

# select the minimum element and swap it.

# sudo code

selection_arr = [13, 46, 24, 52, 20, 9]

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if (arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    
    return arr

# selection_ans = selection_sort(selection_arr)
# print(selection_ans)

# Bubble Sort

# push the max element using ajacent swaps 

bubble_arr = [13, 46, 24, 52, 20, 9]
sorted_bubble_arr = [9, 13, 20, 24, 46, 52]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):
        did_swap = 0
        for j in range(1, i+1):
            if (arr[j-1] > arr[j]):
                arr[j-1], arr[j] = arr[j], arr[j-1]
                did_swap = 1
        if (did_swap == 0):
            break

    return arr

# bubble_ans = bubble_sort(bubble_arr)
# print(bubble_ans)

# Insertion Sort

insert_arr = [13, 46, 24, 52, 20, 9]

def insert_sort(arr):
    n = len(arr)

    for i in range(0, n):
        j = i
        while (j > 0 and arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

# insert_ans = insert_sort(insert_arr)
# print(insert_ans)

# Merge Sort - divide and merge

# Two merge sort - uses iterative method

# Merge - Two sorted list into one list that is also sorted
# Algorithm 

arr1 = [9, 13, 20, 24, 46, 52]
arr2 = [2, 3, 5, 6, 8, 16]

def two_way_merge(A, B):
    m, n = len(A), len(B)
    i, j, k = 0,0,0
    merge_arr = [0] * (m+n)

    while (i < m and j < n):
        if (A[i] < B[j]):
            merge_arr[k] = A[i]
            i += 1
            k += 1
        else:
            merge_arr[k] = B[j]
            j += 1
            k += 1
    
    for rem in range(i, m):
        merge_arr[k] = A[rem]
        k += 1
        
    for rem in range(j, n):
        merge_arr[k] = B[rem]
        k += 1

    return merge_arr

# print(two_way_merge(arr1, arr2))


# Merge Sort - uses recursive method

merge_arr = [3,4,1,6,2,5,7]

def merge(arr, low, mid, high):
    left = low
    right = mid+1
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

    for item in range(low, high):
        arr[item] = temp[item - low]

def merge_s(arr, low, high):
    if (low >= high): return
    mid = (low + high) // 2
    merge_s(arr, low, mid)
    merge_s(arr, mid+1, high)
    merge(arr, low, mid, high)

def merge_sort(arr, n):
    merge_s(arr, 0, n-1)

# merge_sort(merge_arr, len(merge_arr))
# print(merge_arr)

# recursive bubble sort

rec_bubble_arr = [13, 46, 24, 52, 20, 9]

def rec_bubble_sort(arr, n):
    if (n == 1): return arr

    swapped = False
    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            arr[i+1], arr[i]=  arr[i], arr[i+1]
            swapped = True
        if not swapped:
            return arr
    return rec_bubble_sort(arr, n-1)

# rec_bubble_sort(rec_bubble_arr, len(rec_bubble_arr))
# print(rec_bubble_arr)

# recursive insertion sort

rec_insert_arr = [13, 46, 24, 52, 20, 9]

def rec_insertion_sort(arr, n, i):
    if (i == n): return arr

    j = i

    while (j > 0 and arr[j-1] > arr[j]):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1

    return rec_insertion_sort(arr, n, i+1)

# rec_insertion_sort(rec_insert_arr, len(rec_insert_arr), 1)
# print(rec_insert_arr)

# Quick Sort

quick_arr = [4, 6, 2, 5, 7, 9, 1, 3]

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while (i < j):
        while (arr[i] <= pivot and i <= (high-1)):
            i += 1
        while (arr[j] > pivot and j >= (low+1)):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if (low < high):
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index-1)
        quick_sort(arr, p_index+1, high)

print('Before Sort', quick_arr)
quick_sort(quick_arr, 0, len(quick_arr)-1)
print('After Sort', quick_arr)


