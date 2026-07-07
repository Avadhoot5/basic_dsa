# Two sum problem 

# arr = [], target = k

# two types - 1. If sum exists return Yes/No. 2. Sum do exist return the indexes of the elements

two_sum_arr = [2, 6, 5, 8, 11]

# Type 1 

def two_sum_arr_brute_type_1(arr, k):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if (i == j): continue
            if (arr[i] + arr[j] == k):
                return 'Yes'
    return 'No'

# print(two_sum_arr_brute_type_1(two_sum_arr, 14))

def two_sum_arr_brute_type_2(arr, k):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if (i == j): continue
            if (arr[i] + arr[j] == k):
                return [i, j]
    return -1

# print(two_sum_arr_brute_type_2(two_sum_arr, 14))

# Type 2 Optimal. [TC: O(N), SC: O(N)]

def two_sum_arr_opm_type_2(arr, k):
    n = len(arr)
    hash_arr = {}

    for i in range(n):
        rem = k - arr[i]
        if (rem in hash_arr):
            return [hash_arr[rem], i]
        hash_arr[arr[i]] = i
    return -1

# print(two_sum_arr_opm_type_2(two_sum_arr, 14))

# Type 1 Optimal [TC: O(NlogN) + O(N), SC: O(1)]

def two_sum_arr_opm_type_1(arr, k):
    n = len(arr)
    arr.sort()
    left, right = 0, n-1
    curr_sum = 0

    while (left < right):
        curr_sum = arr[left] + arr[right]
        if (curr_sum == k): return 'Yes'
        elif (curr_sum < k): left+=1
        else: right-=1

    return 'No'

# print(two_sum_arr_opm_type_1(two_sum_arr, 14))

# Sort an array of 0, 1, and 2

sort_arr_012 = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]

# Better Solution. [TC: O(2N), SC: O(1)]

def sort_arr_num_better(arr):
    n = len(arr)
    count_0, count_1, count_2 = 0, 0, 0

    for i in range(n):
        if arr[i] == 0: count_0 += 1
        elif arr[i] == 1: count_1 += 1
        else: count_2 += 1
    
    for i in range(count_0):
        arr[i] = 0
    
    for i in range(count_0, count_0+count_1):
        arr[i] = 1
    
    for i in range(count_0+count_1, n):
        arr[i] = 2
    return arr

# print(sort_arr_num_better(sort_arr_012))

# Optimal Solution -> DNF [TC: O(N), SC:O(1)]

def sort_arr_num_opm(arr):
    n = len(arr)
    low, mid = 0, 0
    high = n-1

    while (mid <= high):
        if (arr[mid] == 0):
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif (arr[mid] == 1): mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# print(sort_arr_num_opm(sort_arr_012))


























































































