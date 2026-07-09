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

# Majority Element I | Brute-Better-Optimal | Moore's Voting Algorithm 

majority_arr = [2, 2, 3, 3, 1, 2, 2]

# Brute [TC: O(N*N), SC: O(1)]

def majority_element_brute(arr):
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(n):
            if (arr[i] == arr[j]):
                count += 1        
        if (count > (n//2)):
            return arr[i]
    return -1

# print(majority_element_brute(majority_arr))

# Better. [TC: O(2N), SC: O(N)]

def majority_element_better(arr):
    n = len(arr)
    hash_arr = {}

    for i in range(n):
        if (arr[i] in hash_arr): hash_arr[arr[i]] += 1
        else: hash_arr[arr[i]] = 1

    for i in hash_arr:
        if (hash_arr[i]  > n//2):
            return i
    return -1

# print(majority_element_better(majority_arr))

# Optimal. [TC: O(N), SC: O(1)]

def majority_element_opt(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        if (count == 0):
            element = arr[i]
            count = 1
        else:
            if (arr[i] == element):
                count += 1
            else:
                count -= 1

    max_count = 0   

    for i in range(n):
        if (arr[i] == element):
            max_count += 1
        if (max_count > n//2):
            return element    

    return -1

# print(majority_element_opt(majority_arr))

# Kadane's Algorithm | Maximum Subarray Sum | Finding and Printing

max_sub_arr = [-2, -3, 4, -1, -2, 1, 5, -3]

max_sub_arr_1 = [-2, -1]

import sys
min_int = - sys.maxsize

# Brute [TC: O(N*N), SC: O(1)]

def max_subarr_brute(arr):
    n = len(arr)
    max_sum = min_int

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)
    
    return max_sum

# print(max_subarr_brute(max_sub_arr))

# Type 1: Return the max - Kadane's Algorithm [TC: O(N), SC: O(1)]

def max_subarr_opt_1(arr):
    n = len(arr)
    max_sum = min_int
    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        max_sum = max(max_sum,curr_sum)
        if (curr_sum < 0):
            curr_sum = 0

    return max_sum

# print(max_subarr_opt_1(max_sub_arr))

# Type 2: Return the sub-array [TC: O(N), SC: O(1)]

def max_subarr_opt_2(arr):
    n = len(arr)
    max_sum = min_int
    curr_sum = 0
    start_idx, end_idx = -1, -1

    for i in range(n):
        if (curr_sum == 0):
            start = i            
        curr_sum += arr[i]
        if (curr_sum > max_sum):
            max_sum = curr_sum
            start_idx = start 
            end_idx = i
        if (curr_sum < 0):
            curr_sum = 0

    return (start_idx, end_idx)

# print(max_subarr_opt_2(max_sub_arr))

#  Best Time to Buy and Sell Stock 

# [TC: O(N), SC: O(1)]

stock_arr_1 = [7, 1, 5, 3, 6, 4]
stock_arr_2 = [7,6,4,3,1]

def stock_buy_sell(arr):
    n = len(arr)
    min_element = arr[0]
    max_profit = 0

    for i in range(1, n):
        profit = arr[i] - min_element
        max_profit = max(profit, max_profit)
        min_element = min(arr[i], min_element)

    return max_profit

print(stock_buy_sell(stock_arr_1))
print(stock_buy_sell(stock_arr_2))

















































































