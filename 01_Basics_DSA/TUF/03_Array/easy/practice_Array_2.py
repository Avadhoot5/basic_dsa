# arrays in python

# 1. Largest Element in Array

one_arr = [3, 2, 1, 5, 2]

# brute force approach [TC: O(NlogN), SC: O(1)/O(N)]

def largest_element_brute(arr):
    arr.sort()
    return arr[-1]

# print(largest_element_brute(one_arr))

# Optimal approach [TC: O(N), SC: O(1)]

# using loop

def largest_element_opm(arr):
    max_num = arr[0]
    n = len(arr)
    for i in range(n):
        if (arr[i] > max_num): max_num = arr[i]
    return max_num

# print(largest_element_opm(one_arr))

# using recursion

def largest_element_rec(arr, i):
    if (i == len(arr) - 1): return arr[i]
    max_num = largest_element_rec(arr, i+1)
    if (arr[i] > max_num):
        return arr[i]
    else:
        return max_num

# print(largest_element_rec(one_arr, 0))

# 2. Second largest element in an array

second_arr = [42,7,19,3,88,3,7,56,91,14,91,88,27,65]

# brute force approach - 

# 1. Brute Force [TC: O(NlogN), SC: O(2N)]

def second_largest_brute(arr):
    new_set = set(arr)
    new_arr = list(new_set)
    new_arr.sort()
    return (new_arr[-2])

# print(second_largest_brute(second_arr))

# 2. TC - O(NlogN + N), SC - O(1)

def second_largest_brute_2(arr):
    n = len(arr)
    if (n < 2): return None
    arr.sort()
    largest = arr[-1]

    for i in range(n-2, -1, -1):
        if (arr[i] != largest):
            return arr[i]

    return None

# print(second_largest_brute_2(second_arr))

# Optimal approach. TC - O(N)

def second_largest_optimal(arr):
    n = len(arr)
    if len(arr) < 2: return None

    largest, second_largest = arr[0], None

    for i in range(1, n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif (arr[i] != largest and (second_largest is None or arr[i] > second_largest)):
            second_largest = arr[i]
            
    return second_largest

# print(second_largest_optimal(second_arr))

# Print second smallest

def second_smallest_opm(arr):
    n = len(arr)
    if n < 2: return None

    smallest, second_smallest = arr[0], None

    for i in range(1, n):
        if (arr[i] < smallest):
            second_smallest = smallest
            smallest = arr[i]
        elif (arr[i] != smallest and (second_smallest is None or arr[i] < second_smallest)):
            second_smallest = arr[i]
    
    return second_smallest

# print(second_smallest_opm(second_arr))

# check if the array is sorted.

array_1 = [1, 2, 2, 3, 3, 4]
array_2 = [1,2,1,19,3,88,56,91,14,27,65]

def check_sorted_array(arr):
    n = len(arr)
    is_sorted = True

    for i in range(n-1):
        if not(arr[i] <= arr[i+1]):
            is_sorted = False
            break
    
    return is_sorted

# print(check_sorted_array(array_1))
# print(check_sorted_array(array_2))

# Remove duplicates from the sorted array.

dup_array = [1, 2, 3, 3, 4, 5, 5, 7, 8, 8]

# 1. Bruteforce approach [TC: O(N), SC: O(N)]

def remove_duplicates_brute(arr):
    n = len(arr)
    final_arr = []

    for i in range(n):
        if (arr[i] not in final_arr):
            final_arr.append(arr[i])
    
    return final_arr

# print(remove_duplicates_brute(dup_array))

# 2. Similar implementation in set [TC: O(N), SC: O(N)]

dup_array_2 = [1,1,2,2,2,3,3]

def remove_dup_set(arr):
    n = len(arr)
    if n < 2: return arr
    ans_set = set()

    for i in range(n):
        if arr[i] not in ans_set:
            ans_set.add(arr[i])    

    return list(ans_set)

# print(remove_dup_set(dup_array_2))

# 3. Optimal approach

dup_array_3 = [1, 2, 3, 3, 4, 5, 5, 7, 8, 8]

def remove_dup_opm(arr):
    i = 0
    n = len(arr)

    for j in range(1, n):
        if (arr[i] != arr[j]):
            arr[i+1] = arr[j]
            i+=1
    return i+1

# print(remove_dup_opm(dup_array_3))

# 1. Left Rotate array by 1.

rotate_arr_1 = [1,2,19,3,88,56,91,14,27,65]

def rotate_array_by_1(arr):
    n = len(arr)
    temp = arr[0]

    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[-1] = temp

# print('Array before: ', rotate_arr_1)
# rotate_array_by_1(rotate_arr_1)
# print('Array after: ', rotate_arr_1)

# 2. Left Rotate array by K places.

# Brute force -> [TC: O(N+D), SC: O(D)]

def rotate_array_brute(arr, d):
    n = len(arr)
    d = d % n
    temp = []

    for i in range(d):
        temp.append(arr[i])
    
    for j in range(d, n):
        arr[j-d] = arr[j]
    
    for k in range(n-d, n):
        arr[k] = temp[k-(n-d)]
    
    return arr

# print('Array before: ', rotate_arr_1)
# rotate_array_brute(rotate_arr_1, 3)
# print('Array after: ', rotate_arr_1)

# optimal solution [TC: O(N), SC: O(1)]

rotate_arr_2 = [1,2,19,3,88,56,91,14,27,65]

def rotate_array_opm(arr, d):

    def reverse(arr, left, right):
        while (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    n = len(arr)
    d = d % n

    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)

    return arr

# print('Array before: ', rotate_arr_2)
# rotate_array_opm(rotate_arr_2, 3)
# print('Array after: ', rotate_arr_2)

# Move Zeros to End 

zero_arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

def move_zero_brute(arr):
    n = len(arr)
    temp = []

    for i in range(n):
        if (arr[i] != 0): temp.append(arr[i])
    
    for i in range(len(temp)):
        arr[i] = temp[i]
    
    for i in range(len(temp), n):
        arr[i] = 0

    return arr

# print('Array before: ', zero_arr)
# move_zero_brute(zero_arr)
# print('Array after: ', zero_arr)

def move_zero_opm(arr):
    n = len(arr)
    j = -1

    for i in range(n):
        if (arr[i] == 0):
            j = i
            break

    for i in range(j+1, n):
        if (arr[i] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

# print('Array before: ', zero_arr)
# move_zero_opm(zero_arr)
# print('Array after: ', zero_arr)

# Linear Search

linear_arr = [42,7,19,3,88,56,91,14,27,65]

def linear_search(arr, num):
    n = len(arr)
    
    for i in range(n):
        if (arr[i] == num):
            return i
    return -1

# print(linear_search(linear_arr, 27))

# Union of two sorted arrays.

# Case 1: Arrays are unsorted - Go with the set approach.

union_arr_1 = [1, 2, 2, 3, 4, 5, 6]
union_arr_2 = [2, 3, 4, 4, 7, 8]

# brute force approach 

def union_arr_brute(arr1, arr2):
    seen = set()
    ans = []

    for x in arr1 + arr2:
        if x not in seen:
            seen.add(x)
            ans.append(x)
    
    return ans

# print(union_arr_brute(union_arr_1, union_arr_2))

def union_arr_opm(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i, j = 0,0
    ans_arr = []

    while (i < m and j < n):
        if (arr1[i] <= arr2[j]):
            if (len(ans_arr) == 0 or ans_arr[-1] != arr1[i]):
                ans_arr.append(arr1[i])
            i+=1
        else:
            if (len(ans_arr) == 0 or ans_arr[-1] != arr2[j]):
                ans_arr.append(arr2[j])
            j+=1
    
    while (i < m):
        if (len(ans_arr) == 0 or ans_arr[-1] != arr1[i]):
            ans_arr.append(arr1[i])
        i+=1
    while (j < n):
        if (len(ans_arr) == 0 or ans_arr[-1] != arr2[j]):
            ans_arr.append(arr2[j])
        j+=1
    
    return ans_arr

# print(union_arr_opm(union_arr_1, union_arr_2))

# Intersection of Sorted Arrays 

intersect_arr_1 = [1, 2, 2, 3, 4, 5, 6]
intersect_arr_2 = [2, 3, 5, 6, 7, 8]

def intersection_brute(arr1, arr2):
    ans_set = set() # SC: O(n1 + n2)

    for i in arr1: # TC: O(n1 * n2)
        if i in arr2:
            ans_set.add(i)
    
    return list(ans_set)    # SC: O(n1 + n2), TC: O(n1 + n2)

# print(intersection_brute(intersect_arr_1, intersect_arr_2))
 
def intersection_opm(arr1, arr2):
    ans_arr = []
    m = len(arr1)
    n = len(arr2)
    i, j = 0,0

    while (i < m and j < n):
        if (arr1[i] < arr2[j]):
            i += 1
        elif (arr1[i] > arr2[j]):
            j += 1
        else:
            if (len(ans_arr) == 0 or ans_arr[-1] != arr1[i]):
                ans_arr.append(arr1[i])
            i += 1
            j += 1

    return ans_arr

# print(intersection_opm(intersect_arr_1, intersect_arr_2))

# missing number in an array

miss_num_ar = [9,6,4,2,3,5,7,0,1]

# BF -> TC = O(n*n) SC = O(1)

def missing_num_brute(arr):
    n = len(arr)

    for i in range(0, n+1):
        if not(i in arr):
            return i

# print(missing_num_brute(miss_num_ar))

# Better -> TC = O(N), SC = O(N)

def missing_num_better(arr):
    n = len(arr)
    hash_arr = [0] * (n+1)

    for i in range(n):
        hash_arr[arr[i]] = 1
    
    for i in range(len(hash_arr)):
        if (hash_arr[i] == 0):
            return i

# print(missing_num_better(miss_num_ar))

def missing_num_opm1(arr):
    n = len(arr)
    total_sum = (n*(n+1))//2
    arr_sum = 0
    
    for i in range(n):
        arr_sum += arr[i]
    
    return (total_sum - arr_sum)

# print(missing_num_opm1(miss_num_ar))

def missing_num_opm2(arr):
    n = len(arr)
    xor1, xor2 = 0, 0

    for i in range(n):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ i
    xor2 = xor2 ^ n
    return xor1 ^ xor2

# print(missing_num_opm2(miss_num_ar))

# Max Consecutive number of 1's

consecutive_one_arr = [1, 1, 0, 1, 1, 1, 0, 1, 1]

def max_consecutive_one(arr):
    n = len(arr)
    count, max_count = 0, 0

    for i in range(n):
        if (arr[i] == 1):
            count += 1
            if (count > max_count):max_count = count
        else:
            count = 0
    return max_count

# print(max_consecutive_one(consecutive_one_arr))

# Find the number that appears once, and other numbers twice.

find_num_arr = [1, 1, 2, 3, 3, 4, 4]

def find_num_opm(arr):
    n = len(arr)
    xor = 0

    for i in range(n):
        xor = xor ^ arr[i]
    
    return xor

# print(find_num_opm(find_num_arr))






