# Largest Subarray with Zero Sum | Amazon | MMT

sub_arr_1 = [1, -1, 3, 2, -2, -8, 1, 7, 10, 23]
sub_arr_2 = [15,-2, 2, -8, 1, 7, 10, 23]

# [TC: O(N*N), SC: O(1)]

def largest_sub_arr_better(arr):
    n = len(arr)
    max_len = 0

    for i in range(n):
        curr_sum = arr[i]
        for j in range(i+1, n):
            curr_sum += arr[j]
            if (curr_sum == 0):
                max_len = max(max_len, j-i+1)

    return max_len

# print(largest_sub_arr_better(sub_arr_2))

# Optimal [TC: O(N), SC: O(N)]

def largest_sub_arr_opm(arr):
    n = len(arr)
    pre_sum = 0
    hash_map = {}
    max_len = 0

    for i in range(n):
        pre_sum += arr[i]

        if (pre_sum == 0):
            max_len = i + 1
        else:
            if (pre_sum in hash_map):
                max_len = max(max_len, i - hash_map[pre_sum])
            else:
                hash_map[pre_sum] = i 

    return max_len

print(largest_sub_arr_opm(sub_arr_1))
print(largest_sub_arr_opm(sub_arr_2))
