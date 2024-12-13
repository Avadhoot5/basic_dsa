
# move zeros 

inputArr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

def moveZero(arr, n):
    j = -1
    for i in range(0, n):
        if (arr[i] == 0):
            j = i
            break
    
    for i in range(j+1, n):
        if (arr[i] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

print(moveZero(inputArr, len(inputArr)))
