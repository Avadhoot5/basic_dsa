# Last index ques.

arr = [2,5,7,8,2,6,8,1]

def lastIndex(arr, i, element):
    if (i == len(arr)):
        return -1
    val = lastIndex(arr, i+1, element)
    if (val == -1):
        if (arr[i] == element):
            return i
        else:
            return -1
    else:
        return val

ans = lastIndex(arr, 0, 8)
print(ans)
