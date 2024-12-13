# Move Zeros to End 

# brute force - TC => O(N) + O(X) + O(N-X) => O(2N)
# SC => O(N) 

inputArr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

def moveZeroBF(arr, n):
    temp = []
    for i in range(0, n):
        if (arr[i] != 0):
            temp.append(arr[i])

    for i in range(0, len(temp)):
        arr[i] = temp[i]
    
    for i in range(len(temp), n):
        arr[i] = 0

    return arr

# print(moveZeroBF(inputArr, len(inputArr)))

def moveZeroO(arr, n):
    j = -1
    for i in range(0,len(arr)):
        if (arr[i] == 0):
            j = i
            break
    
    for i in range(j+1, len(arr)):
        if (arr[i] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


print(moveZeroO(inputArr, len(inputArr)))

