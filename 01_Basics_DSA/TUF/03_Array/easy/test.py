
# remove duplicates from sorted array 

arr = [1,1,2,3,3,4,5,5,5]

def removeDup(arr):
    i = 0
    for j in range(1, len(arr)):
        if (arr[j] != arr[i]):
            arr[i+1] = arr[j]
            i += 1
    return i + 1
print(removeDup(arr))

