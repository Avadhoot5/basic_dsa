# Merge Sort - divide and merge

# Two merge sort - uses iterative method

# Merge - Two sorted list into one list that is also sorted
# Algorithm 

arr1 = [9, 13, 20, 24, 46, 52]
arr2 = [2, 3, 5, 6, 8, 16]

def twoWayMerge(A, B, m, n):
    i, j, k = 0,0,0
    finalArr = [0] * (m+n)

    while (i < m and j < n):
        if (A[i] < B[j]):
            finalArr[k] = A[i]
            k += 1
            i += 1
        else:
            finalArr[k] = B[j]
            k += 1
            j += 1
    for rem in range(i, m):
        finalArr[k] = A[rem]
        k += 1
    for rem in range(j, n):
        finalArr[k] = B[rem]
        k += 1
    return finalArr

# print(twoWayMerge(arr1, arr2, 6, 6))

# Merge Sort - uses recursive method

