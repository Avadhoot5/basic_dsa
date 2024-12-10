
# check if the array is sorted.

arr1 = [1, 2, 2, 3, 3, 4]
arr2 = [1,2,1,19,3,88,56,91,14,27,65]

def sortedArr(arr):
    isSorted = True
    for i in range(0, len(arr)-1):
        if not(arr[i] <= arr[i+1]):
            isSorted = False
            break
    return isSorted

print(sortedArr(arr1))
print(sortedArr(arr2))

