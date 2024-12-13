# Linear Search

arr = [42,7,19,3,88,56,91,14,27,65]

def findElement(arr, k):
    isPresent = False
    for i in range(0, len(arr)):
        if (arr[i] == k):
            isPresent = True
            break
    return isPresent

print(findElement(arr, 27))

