# First index ques.

arr = [2,5,7,8,2,6,8,1]

# the below code is not optimal.
# since we are going till the end and then returning back and checking for the element.

def firstOccr(arr, i, element):
    if (i == len(arr)):
        return -1
    value = firstOccr(arr, i+1, element)
    if (element == arr[i]):
        return i
    else:
        return value

# ans = firstOccr(arr, 0, 3)
# print(ans)

def firstOccrOptimal(arr, i, element):
    if (i == len(arr)):
        return -1
    if (element == arr[i]):
        return i
    else:
        return firstOccr(arr, i+1, element)

ans = firstOccrOptimal(arr, 0, 8)
print(ans)
