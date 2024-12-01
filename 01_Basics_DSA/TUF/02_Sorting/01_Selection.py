# Selection sort

# sudo code

inputArr = [13, 46, 24, 52, 20, 9]

def selection(arr):

    for i in range(0, len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if (arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]

    return arr

print(selection(inputArr))

