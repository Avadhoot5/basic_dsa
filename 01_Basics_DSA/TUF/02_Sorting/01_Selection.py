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

# print(selection(inputArr))

# Bubble Sort

bubbleArr = [13, 46, 24, 52, 20, 9]

def bubble(arr, n):
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if (arr[j] > arr[j+1]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

print(bubble(bubbleArr, len(bubbleArr)))
