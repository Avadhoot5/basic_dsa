# 1. Left Rotate array by 1.

rotateArr = [1,2,19,3,88,56,91,14,27,65]

def rotateArrByOne(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

# print(rotateArrByOne(rotateArr))

# 2. Left Rotate array by K places.

# Brute force 
# TC. O(d) + O(n-d) + O(d) => O(n+d)
# SC. O(d)

def rotateArrByDBF(arr, n, d):
    d = d % n
    temp = []
    for i in range(0, d):
        temp.append(arr[i])
    
    for i in range(d, n):
        arr[i-d] = arr[i]
        
    for i in range(n-d, n):
        arr[i] = temp[i-(n-d)]
    return arr

# print(rotateArrByDBF(rotateArr, len(rotateArr), 3))
# TC => O(N) and SC => O(1)

# optimal solution 
rotateArrNew = [1,2,19,3,88,56,91,14,27,65]

# alt approach - return arr[d:] + arr[:d]

def rotateArrByDO(arr, n, d):
    d = d % n
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])
    arr.reverse()
    return arr

print(rotateArrByDO(rotateArrNew, len(rotateArrNew), 3))

# right rotate by D places.

# optimal solution 

rotateArrNew2 = [1,2,3,4,5,6,7]

def rightRotate(arr, n, d):
    d = d % n
    arr.reverse()
    arr[:d] = reversed(arr[:d])
    arr[d:] = reversed(arr[d:])
    return arr


print(rightRotate(rotateArrNew2, len(rotateArrNew2), 3))
