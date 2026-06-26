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
