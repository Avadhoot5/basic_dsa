# return all indices of an element in an array.

arr = [2,5,7,8,2,6,9,2,8,1]

tempArr = []

# simple solution
# def allIndices(arr, i, n):
#     if (i == len(arr)):
#         return -1
#     if (arr[i] == n):
#         tempArr.append(i)
#     return allIndices(arr, i+1, n)


# ans = allIndices(arr, 0, 2)
# print(tempArr)

# main solution

def indices(arr, i, n):
    if (i == len(arr)):
        return []
    if (arr[i] == n):
        return [i] + indices(arr, i+1, n)
    else:
        return indices(arr, i+1, n)
    

ans = indices(arr, 0, 2)
print(ans)
