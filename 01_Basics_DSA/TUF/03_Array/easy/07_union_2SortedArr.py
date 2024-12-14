# Union of two sorted arrays.

arr1 = [1, 2, 2, 3, 4, 5, 6]
arr2 = [2, 3, 4, 4, 7, 8]

# brute force approach 

def unionSortBF1(arr1, arr2):
    tempArr = []
    n, m = len(arr1), len(arr2)

    for i in range(0, n):
        if not(arr1[i] in tempArr):
            tempArr.append(arr1[i])
    
    for j in range(0, m):
        if not(arr2[j] in tempArr):
            tempArr.append(arr2[j])
    
    return tempArr

# print(unionSortBF1(arr1, arr2))

# TC O(N1logN) 

def unionSortBF2(arr1, arr2):
    union = []
    common = set() #O(N1 + N2) - if all are unique
    for i in arr1: #O(N1 log N)
        common.add(i)
    for i in arr2: #O(N2 log N)
        common.add(i)
    for i in common: #O(N1 + N2)
        union.append(i)
    return union #O(N1 + N2) - used to return the answer

# print(unionSortBF2(arr1, arr2))

# TC -> O(n1 + n2). SC -> O(n1 + n2)

def unionSortO(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    finalArr = []

    while (i < n and j < m):
        if (arr1[i] <= arr2[j]):
            if (len(finalArr) == 0 or finalArr[-1] != arr1[i]):
                finalArr.append(arr1[i])
            i += 1
        else:
            if (len(finalArr) == 0 or finalArr[-1] != arr2[j]):
                finalArr.append(arr2[j])
            j += 1

    while (i < n):
        if (len(finalArr) == 0 or finalArr[-1] != arr1[i]):
            finalArr.append(arr1[i])
        i += 1

    while (j < m):
        if (len(finalArr) == 0 or finalArr[-1] != arr2[j]):
            finalArr.append(arr2[j])
        j += 1

    return finalArr

print(unionSortO(arr1, arr2))
