# Hashing Maps TC Collisions Division Rule of Hashing

# number hashing

arr = [1,2,5,2,1,3,2,9,7,6]

hashArr = {}

def countNum(n):
    for i in range(0, len(arr)-1):
        if (arr[i] in hashArr):
            hashArr[arr[i]] += 1
        else:
            hashArr[arr[i]] = 1
    return hashArr.get(n)

# print(countNum(3))

alphaArr = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e']

alphaHash = {}

def charHash(ch):
    for i in alphaArr:
        if (i in alphaHash):
            alphaHash[i] += 1
        else:
            alphaHash[i] = 1
    return alphaHash[ch]

# print('Character appears')
# print(charHash('d'))

# # Hashing - methods 
# 1. Division Method
# 2. Folding Method
# 3. Mid square Method

# 1. Frequencies of Limited Range Array Elements
# Output: [0, 2, 2, 0, 1] Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

# arr = [2, 3, 2, 3, 5]
inputArr = [2, 1, 1]

def freqElements(arr):
    hashArr = [0] * (len(arr) + 1)

    for i in arr:
        hashArr[i] += 1

    return hashArr[1:]

print(freqElements(inputArr))


# 2. Find highest/lowest frequency element

