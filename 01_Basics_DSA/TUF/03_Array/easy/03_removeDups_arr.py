# Remove duplicates from the sorted array.

dupArray = [1, 2, 3, 3, 4, 5, 5, 7, 8, 8]

# Bruteforce approach -

# 1. new array, copy unique elements.

def removeDuplicatesBF1(arr):
    finalArray = []
    for i in arr:
        if not(i in finalArray):
            finalArray.append(i)
    return finalArray

# print(removeDuplicatesBF1(dupArray))

# 2. Similar implementation in set.

def removeDuplicatesBFSet(arr):
    # finalSet = set(arr)
    # return list(finalSet)
    finalSet = set()
    for i in arr:
        finalSet.add(i)
    return list(finalSet)

# print(removeDuplicatesBFSet(dupArray))

dupArray2 = [1,1,2,2,2,3,3]

def removeDuplicatesBF2(arr):
    i = 0
    for j in range(1, len(arr)):
        if (arr[i] != arr[j]):
            arr[i+1] = arr[j]
            i += 1
    return i+1

print(removeDuplicatesBF2(dupArray2))

