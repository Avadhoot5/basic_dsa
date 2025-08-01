
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
    pass

# print(longestSub(longArrB, 3))

# Find Second Largest Element in Array

inputArr = [4, 9, 0, 2, 8 , 7, 1]

def secondLargest(arr):
    large, secondLarge = 0, -1
    for i in range(0, len(arr)):
        if (arr[i] > large):
            secondLarge = large
            large = arr[i]
        elif (arr[i] < large and arr[i] > secondLarge):
            secondLarge = arr[i]
    return secondLarge

# print(secondLargest(inputArr))

def secondSmallest(arr):
    small, secondSmall = arr[0],arr[0]
    for i in range(0, len(arr)):
        if (arr[i] < small):
            secondSmall = small
            small = arr[i]
        elif (arr[i] > small and arr[i] < secondSmall):
            secondSmall = arr[i]
    return secondSmall    

# print(secondSmallest(inputArr))

# Remove duplicates from the sorted array.

dupArray = [1, 2, 3, 3, 4, 5, 5, 7, 8, 8]

# brute force 1

def removeDuplicatesBF1(arr):
    pass

removeDuplicatesBF1(dupArray)




