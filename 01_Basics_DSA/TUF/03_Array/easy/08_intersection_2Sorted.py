# Intersection of Sorted Arrays 

arr1 = [1, 2, 2, 3, 4, 5, 6]
arr2 = [2, 3, 5, 6, 7, 8]

def intersectionBF1(a, b):
    temp = set()
    for i in a:
        if (i in b):
            temp.add(i)
    return list(temp)

# print(intersectionBF1(arr1, arr2))

def intersectionO(a, b):
    finalArr = []
    m = len(a)
    n = len(b)
    i, j = 0, 0
    while (i < m and j < n):
        if (a[i] < b[j]):
            i += 1
        elif (b[j] < a[i]):
            j += 1
        else:
            finalArr.append(a[i])
            i += 1
            j += 1

    return finalArr

print(intersectionO(arr1, arr2))

