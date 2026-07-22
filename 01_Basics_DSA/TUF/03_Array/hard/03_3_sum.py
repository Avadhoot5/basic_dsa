# 3 sum problem

# arr[i] + arr[j] + arr[k] = 0; where (i!=j!=k)

que_arr = [-1,0,1,2,-1,-4]

# Brute [TC: O(N*N*N * log(no of unique elements)), SC: 2*O(No. of triplets)]

def three_sum_brute(arr):
    n = len(arr)
    ans_set = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    ans_set.add(triplet)

    return [list(i) for i in ans_set]

# print(three_sum_brute(que_arr))

def three_sum_better(arr):
    n = len(arr)
    ans_set = set()

    for i in range(n):
        hash_set = set()
        for j in range(i+1, n):
            third = -(arr[i] + arr[j])
            if (third in hash_set):
                temp = tuple(sorted([arr[i], arr[j], third]))
                ans_set.add(temp)

            hash_set.add(arr[j])

    return [list(ans) for ans in ans_set]

print(three_sum_better(que_arr))

que_arr_2 = [0,2,2,-1,-1,-2,-2,0,-1,0,2,2,-2]

def three_sum_opm(arr):
    arr.sort()
    n = len(arr)
    ans = []

    for i in range(0, n):
        if (i > 0 and arr[i] == arr[i-1]):
            continue

        j = i + 1
        k  = n-1

        while (j < k):
            curr_sum = arr[i] + arr[j] + arr[k]
            if (curr_sum < 0):
                j += 1
            elif (curr_sum > 0):
                k -= 1
            else:
                ans.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while (j < k and arr[j] == arr[j-1]): j+=1
                while (j < k and arr[k] == arr[k+1]): k-=1
    return ans

print('Que Arr 1:', three_sum_opm(que_arr))
print('Que Arr 2:', three_sum_opm(que_arr_2))


