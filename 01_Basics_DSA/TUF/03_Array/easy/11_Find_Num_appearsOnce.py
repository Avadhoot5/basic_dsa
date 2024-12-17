# Find the number that appears once, and other numbers twice.

# brute force.

# TC. O(N*N). SC => O(1)

findArr = [4,1,2,1,2]
array = [1, 1, 2, 3, 3, 4, 4]

def findNumBF1(arr):
    for i in range(0, len(arr)):
        num = arr[i]
        ctr = 0
        for j in range(0, len(arr)):
            if (arr[j] == num):
                ctr += 1
        if (ctr == 1):
            return num

# print(findNumBF1(findArr))

# hashMap implement, return the element having count 1

def findNumB(arr):
    hashMap = {}
    for i in range(0, len(arr)):
        if (arr[i] in hashMap):
            hashMap[arr[i]] += 1
        else:
            hashMap[arr[i]] = 1
            
    for i in hashMap.items():
        if (i[1] == 1):
            return i[0]

print(findNumB(array))


def findNumO(arr):
    xor = 0
    for i in range(0, len(arr)):
        xor = xor ^ arr[i]
    return xor
print(findNumO(array))
