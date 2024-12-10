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

# dupArray2 = [1,1,2,2,2,3,3]

# def removeDuplicatesBF2(arr):
#     finalArray = []
#     low = 0
#     for i in range(0, len(arr)-1):
#         if (arr[i] == arr[i+1]):
#             low += 1
#         else:
#             finalArray.append(arr[low])
#             low += 1
#     return finalArray

# print(removeDuplicatesBF2(dupArray2))

