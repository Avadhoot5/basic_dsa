
# remove duplicates from sorted array 

arr = [1,1,2,3,3,4,5,5,5]

def removeDup(arr):
    i = 0
    for j in range(1, len(arr)):
        if (arr[j] != arr[i]):
            arr[i+1] = arr[j]
            i += 1
    return i + 1

# print(removeDup(arr))

# Intersection

arr1 = [1, 2, 2, 3, 4, 5, 6]
arr2 = [2, 3, 5, 6, 7, 8]



# longest subarray with sum k - optimal

longArrB =[1, 2, 3, 0, 0, 1, 1, 1, 4, 2, 3]

def longestSub(arr, k):
    n = len(arr)
    left, right = 0, 0
    length = 0
    sum = 0

    while (right < n):
        while (left <= right and sum > k):
            sum = sum - arr[left]
            left+=1
        if (sum == k):
            length = max(length, right-left + 1)
        right+=1
        if (right < n):
            sum += arr[right]
    return length

print(longestSub(longArrB, 3))
