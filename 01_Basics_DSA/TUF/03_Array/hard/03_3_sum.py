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



