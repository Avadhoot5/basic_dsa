# print the maxium element of an array.

arr = [42,7,19,3,88,56,91,14,27,65]


def maxVal(arr, i):
    if (i == len(arr) - 1):
        return arr[i]    
    mesa = maxVal(arr, i+1)
    if (mesa > arr[i]):
        return mesa
    else:
        return arr[i]

ans = maxVal(arr, 5)
print(ans)
