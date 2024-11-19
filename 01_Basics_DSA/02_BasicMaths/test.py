# Grokking algorithms 

# Binary Search

numbers = [1, 6, 7, 8, 11, 13, 14, 18, 19, 21, 22, 23, 25, 27, 33, 34, 35, 37, 41, 42, 49, 50, 51, 54, 56, 59, 60, 62, 65, 66, 73, 74, 77, 82, 88, 89, 90, 92]

def bSearch(arr, n):
    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (high + low) // 2
        guess = arr[mid]

        if (guess == n):
            return mid
        elif (n < guess):
            high = mid - 1
        elif (n > guess):
            low = mid + 1
    return None

ans = bSearch(numbers, 113)
print(ans)
