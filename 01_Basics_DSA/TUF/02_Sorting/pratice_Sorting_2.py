# Selection sort

# select the minimum element and swap it.

# sudo code

selection_arr = [13, 46, 24, 52, 20, 9]

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if (arr[j] < arr[min]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    
    return arr

# selection_ans = selection_sort(selection_arr)
# print(selection_ans)

# Bubble Sort

# push the max element using ajacent swaps 

bubble_arr = [13, 46, 24, 52, 20, 9]
sorted_bubble_arr = [9, 13, 20, 24, 46, 52]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):
        did_swap = 0
        for j in range(1, i+1):
            if (arr[j-1] > arr[j]):
                arr[j-1], arr[j] = arr[j], arr[j-1]
                did_swap = 1
        if (did_swap == 0):
            break

    return arr

# bubble_ans = bubble_sort(bubble_arr)
# print(bubble_ans)

# Insertion Sort

insert_arr = [13, 46, 24, 52, 20, 9]

def insert_sort(arr):
    n = len(arr)

    for i in range(0, n):
        j = i
        while (j > 0 and arr[j-1] > arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr

insert_ans = insert_sort(insert_arr)
print(insert_ans)

