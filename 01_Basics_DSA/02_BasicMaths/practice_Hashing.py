# Hashing Maps TC Collisions Division Rule of Hashing

# number hashing
arr = [1,2,5,2,1,3,2,9,7,6]

def count_num(n, arr):
    count = 0
    
    for i in range(len(arr)):
        if (arr[i] == n):
            count += 1
    return count

# print(count_num(1, arr))

hashArr = {}

def countNum(arr, n):
    for i in range(0, len(arr)):
        if (arr[i] in hashArr):
            hashArr[arr[i]] += 1
        else:
            hashArr[arr[i]] = 1
    return hashArr.get(n)

# print(countNum(arr, 2))

alphaArr = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e']

def charHash(arr, ch):
    alphaHash = {}
    
    for i in range(len(arr)):
        if (arr[i] in alphaHash):
            alphaHash[arr[i]] += 1
        else:
            alphaHash[arr[i]] = 1
    
    print(alphaHash)
    return alphaHash.get(f'{ch}')

# print('Character appears:', charHash(alphaArr, 'd'))

# # Hashing - methods 

# 1. Division Method
# 2. Folding Method
# 3. Mid square Method

# 1. Frequencies of Limited Range Array Elements

# arr = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1] Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.

inputArr = [2, 3, 2, 3, 5]

def freqElements(arr):
    hash_arr = [0] * (len(arr)+1)

    for i in range(len(arr)):
        hash_arr[arr[i]] += 1
    
    return hash_arr[1:]

# print(freqElements(inputArr))

# 2. Find highest/lowest frequency element

freqArr = [1,2,5,2,1,3,2,9,7,6]

def highLow(arr, n):
    hash_arr = {}

    for i in arr:
        hash_arr[i] = hash_arr.get(i, 0) + 1

    max_count, min_count = 0, n
    max_element, min_element = 0, 0

    for i in hash_arr:
        if (hash_arr[i] > max_count):
            max_count = hash_arr[i]
            max_element = i
        if (hash_arr[i] < min_count):
            min_count = hash_arr[i]
            min_element = i

    print(f'The Max Element is {max_element}, with count {max_count}')
    print(f'The Min Element is {min_element}, with count {min_count}')

highLow(freqArr, len(freqArr))
