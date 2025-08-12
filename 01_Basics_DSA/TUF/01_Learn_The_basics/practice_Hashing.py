# Hashing Maps TC Collisions Division Rule of Hashing

# number hashing

countArr = [1,2,5,2,1,3,2,9,7,6]

def countNumArr(arr, n):
    pass


def countNum(arr, n):
    hashMap = {}

    for i in range(len(arr)):
        if (arr[i] in hashMap):
            hashMap[arr[i]] += 1
        else:
            hashMap[arr[i]] = 1

    if (hashMap.get(n)):
        return hashMap[n]
    else:
        return -1        

print(countNum(countArr, 5))














