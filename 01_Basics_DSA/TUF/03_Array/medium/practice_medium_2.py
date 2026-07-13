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

# print(stock_buy_sell(stock_arr_1))
# print(stock_buy_sell(stock_arr_2))

# Rearrange Array Elements by Sign | 2 Varieties of same Problem

# Brute. [TC: O(N + N//2), SC: O(N)]

re_arr = [3, 1, -2, -5, 2, -4]

def re_arrange_brute(arr):
    n = len(arr)
    pos_arr = []
    neg_arr = []

    for i in range(n):
        if (arr[i] < 0):
            neg_arr.append(arr[i])
        else:
            pos_arr.append(arr[i])
        
    arr = []

    for i in range(n//2):
        arr.append(pos_arr[i])
        arr.append(neg_arr[i])

    return arr

# print(re_arrange_brute(re_arr))

# Optimal [TC: O(N), SC: O(N)]

def re_arrange_opt(arr):
    n = len(arr)
    pos_idx = 0
    neg_idx = 1
    final_arr = [0] * (n)

    for i in range(n):
        if (arr[i] >= 0):
            final_arr[pos_idx] = arr[i]
            pos_idx += 2
        else:
            final_arr[neg_idx] = arr[i]
            neg_idx += 2
    return final_arr

# print(re_arrange_opt(re_arr))

# variety 2  - Not equal N//2.

# Optimal [TC: O(N), SC: O(N)]

re_arr_2 = [3, 1, -2, -5, 2, -4, 5, 9, 2, -1]

def re_arrange_opt_2(arr):
    n = len(arr)
    pos_arr = []
    neg_arr = []
    
    for i in range(n):
        if (arr[i] < 0): neg_arr.append(arr[i])
        else: pos_arr.append(arr[i])

    if (len(pos_arr) > len(neg_arr)):
        idx = 0
        for i in range(0, len(neg_arr)):
            arr[2*i] = pos_arr[i]
            arr[2*i + 1] = neg_arr[i]
        idx = 2*(len(neg_arr))
        for i in range(len(neg_arr), len(pos_arr)):
            arr[idx] = pos_arr[i]
            idx += 1
    else:
        idx = 0
        for i in range(0, len(pos_arr)):
            arr[2*i] = pos_arr[i]
            arr[2*i + 1] = neg_arr[i]
        idx = 2*(len(pos_arr))
        for i in range(len(pos_arr), len(neg_arr)):
            arr[idx] = neg_arr[i]
            idx += 1

    return arr

# print(re_arrange_opt_2(re_arr_2))

# Next Permutation 

# brute force approach - refer yt video for below approach

# 1. using recursion - generate all the possible permutation in sorted manner
# 2. using Linear search - search for the instance, and return next index.
# 3. If the value is last element, return the 1st element.

# printing permutation using recursion.

next_perm_arr = [2, 1, 5, 4, 3, 0, 0]

def next_permutation_opt(arr):
    idx = -1
    n = len(arr)

    for i in range(n-2, -1, -1):
        if (arr[i] < arr[i+1]):
            idx = i
            break

    if (idx == -1):
        return arr.reverse()
    else:
        for i in range(n-1, idx, -1):
            if (arr[i] > arr[idx]):
                arr[i], arr[idx] = arr[idx], arr[i]
                break
    tempArr = arr[idx+1::]
    tempArr.reverse()
    return arr[:idx+1] + tempArr

# print(next_permutation_opt(next_perm_arr))

# Leaders in an Array

# brute force 

leader_arr = [10, 22, 12, 3, 0, 6]

def leader_arr_brute(arr):
    n = len(arr)
    ans_arr = []

    for i in range(n):
        is_leader = True
        for j in range(i+1, n):
            if (arr[j] > arr[i]):
                is_leader = False
                break
        if (is_leader): ans_arr.append(arr[i])

    return ans_arr

# print(leader_arr_brute(leader_arr))

def leader_arr_opt(arr):
    n = len(arr)
    is_max = 0
    ans_arr = []

    for i in range(n-1, -1, -1):
        if (arr[i] > is_max):
            ans_arr.append(arr[i])
            is_max = arr[i]
    
    return ans_arr

# print(leader_arr_opt(leader_arr))

# Longest Consecutive Sequence 

longest_seq_arr_1 = [0,3,7,2,5,8,4,6,0,1]
longest_seq_arr_2 = [102,4,100,1,101,1,3,2]

# brute force approach.

def linear_search(a, x):
    for i in range(len(a)):
        if (a[i] == x):
            return True
    return False

def longest_seq_brute(arr):
    n = len(arr)
    longest = 1

    for i in range(0, n):
        cnt = 0
        x = arr[i]
        while (linear_search(arr, x) == True):
            x += 1
            cnt += 1
        longest = max(longest, cnt)
    return longest

# print(longest_seq_brute(longest_seq_arr_1))









































































