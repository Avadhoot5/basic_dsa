# 4 sum problem

four_sum_arr_1 = [1, 0, -1, 0, -2, 2]

# [TC: O(N*N*N*N), SC: O(N*no. of unique ans)]

def four_sum_brute(arr, target):
    n = len(arr)
    ans_set = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if ((arr[i] + arr[j] + arr[k] + arr[l]) == target):
                        temp = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        ans_set.add(temp)

    return ans_set

# print(four_sum_brute(four_sum_arr_1, 0))

# [TC: O(N*N*N), SC: O(2*No. of quads) + O(N)]

def four_sum_better(arr, target):
    n = len(arr)
    ans_set = set()

    for i in range(n):
        for j in range(i+1, n):
            hash_set = set()
            for k in range(j+1, n):
                rem = target - (arr[i] + arr[j] + arr[k])
                if (rem in hash_set):
                    temp = tuple(sorted([arr[i], arr[j], arr[k], rem]))
                    ans_set.add(temp)
                hash_set.add(arr[k])
    return ans_set

# print(four_sum_better(four_sum_arr_1, 0))

# [TC: O(N*N*N), SC: O(No. of quads)]

four_sum_arr_2 = [3,4,3,1,5,1,4,2,1,4,2,3,5,2]

def four_sum_opm(arr, target):
    arr.sort()
    n = len(arr)
    ans = []

    for i in range(n):
        if (i > 0 and arr[i] == arr[i-1]):
            continue
        for j in range(i+1, n):
            if (j > i+1 and arr[j] == arr[j-1]):
                continue
            k = j+1
            l = n-1

            while (k < l):
                current_sum = arr[i] + arr[j] + arr[k] + arr[l]
                if (current_sum < target): k += 1
                elif (current_sum > target): l -= 1
                else:
                    ans.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    while (k < l and arr[k] == arr[k-1]): k += 1
                    while (k < l and arr[l] == arr[l-1]): l -= 1

    return ans

# print(four_sum_opm(four_sum_arr_1, 0))
# print(four_sum_opm(four_sum_arr_2, 8))




