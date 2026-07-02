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

print(remove_dup_set(dup_array_2))

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
