# Hashing Maps TC Collisions Division Rule of Hashing

# number hashing

countArr = [1,2,5,2,1,3,2,9,7,6]

# creating an array of size with maximum number allowed. Max num - 9 present in array

def countNumArr(arr, n):
    hashArr = [0] * 10
    for i in range(0, len(arr)):
        hashArr[arr[i]] += 1

    return hashArr[n]

# print(countNumArr(countArr, 2))

# character hashing 

alphaArr = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e']

def charHash(chr, arr):
    charArr = [0] * 26

    for c in arr:
        index = ord(c) - ord('a')
        charArr[index] += 1

    return charArr[ord(chr) - ord('a')]

# print(charHash('a', alphaArr))

# hashing using hashMap - dict in python

def countNum(arr, n):
    hashMap = {}
 
    for item in arr:
        hashMap[item] = hashMap.get(item, 0) + 1

    return hashMap.get(n, -1)

# print(countNum(countArr, 2))

def charHashOptimal(chr, arr):
    hashMap = {}

    for i in arr:
        hashMap[i] = hashMap.get(i, 0) + 1

    return hashMap.get(chr, -1)

# print(charHashOptimal('a', alphaArr))


# 1. Frequencies of Limited Range Array Elements - Count frequency of each element in the array
# Output: [0, 2, 2, 0, 1] Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

# arr = [2, 3, 2, 3, 5]

freqArr = [1,2,5,2,1,3,2,9,7,6]

def freqElements(arr):
    hashMap = {}

    for i in arr:
        hashMap[i] = hashMap.get(i, 0) + 1
    # printing the values
    for i in hashMap:
        print(f'Element {i} occured {hashMap[i]} times')

# freqElements(freqArr)

# Find highest/lowest frequency element

freqArr2 = [1,2,5,2,5,2,1,3,3,2,9,9,7,6,6]

def highLow(arr):
    hashMap = {}

    for i in arr:
        hashMap[i] = hashMap.get(i, 0) + 1
    
    maxCount, minCount = 0, len(arr)-1
    maxElement, minElement = 0, 0

    for i in hashMap.items():
        print(i)
        if (i[1] > maxCount):
            maxCount= i[1]
            maxElement = i[0]
        if (i[1] < minCount):
            minCount = i[1]
            minElement = i[0]
    print(f'Maximum Element is {maxElement} with count: {maxCount}')
    print(f'Minimum Element is {minElement} with count: {minCount}')

# highLow(freqArr2)

