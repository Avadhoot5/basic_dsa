# display an array using recursion

arr = [42,7,19,3,88,56,14,27,65,91]

def displayArr(arr, i):
    if (i == len(arr)):
        return
    print(arr[i])
    displayArr(arr, i+1)

# displayArr(arr, 2)

def displayRevArr(arr, i):
    if (i == len(arr)):
        return
    displayRevArr(arr, i+1)
    print(arr[i])

displayRevArr(arr, 0)


