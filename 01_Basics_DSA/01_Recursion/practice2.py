
# Print Decreasing using version

def recDec(n):
    if (n == 0): return
    print(n)
    recDec(n-1)

# recDec(5)

# Print Increasing using Recursion

def recInc(n):
    if (n == 0): return
    recInc(n-1)
    print(n)

# recInc(5)

#  Print Decreasing Increasing Numbers using Recursion

def recDecInc(n):
    if (n == 0): return
    print(n)
    recDecInc(n-1)
    print(n)

# recDecInc(5)

# Factorial - Question | Recursion 

def fact(n):
    if (n == 1 or n == 0):
        return 1
    ans = fact(n-1) * n
    return ans

# print(fact(5))

# Power (Linear) - Question

def powX(x, n):
    if (n == 0): 
        return 1
    ans = powX(x, n-1) * x
    return ans

# print(powX(5,2))

# Power (Linear) -  (Logarithmic) 

def powXLog(x, n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        return powXLog(x, n//2) * powXLog(x, n//2)
    else:
        return x * powXLog(x, n//2) * powXLog(x, n//2)

# print(powXLog(2, 5))

# Tower of Hanoi - Question

def toh(n, A, B, C):
    if (n == 0):
        return
    toh(n-1, A, C, B)
    print(n, A, B)
    toh(n-1, C, B, A)

# toh(3, 'A', 'B', 'C')

# Display an Array 

inputArr = [5,7,8,2,6,8,1,2,10]

def showArr(arr, idx):
    if (idx == len(arr)):
        return
    print(arr[idx])
    showArr(arr, idx+1)

# showArr(inputArr, 0)

def showRevArr(arr, idx):
    if (idx == len(arr)):
        return
    showRevArr(arr, idx+1)
    print(arr[idx])
    
# showRevArr(inputArr, 0)

# Maximum of an Array 

def maxArr(arr, idx):
    if (idx == len(arr)):
        return 0
    value = maxArr(arr, idx+1)
    return value if value > arr[idx] else arr[idx]

# print(maxArr(inputArr, 0))

# First Index of occurrence 

def firstIndex(arr, i, searchValue):
    if (i == len(arr)):
        return -1
    if (searchValue == arr[i]):
        return i
    else:
        return firstIndex(arr, i+1, searchValue)

# print(firstIndex(inputArr, 0, 2))

# Last index of array

def lastIndex(arr, i, element):
    if (i == len(arr)):
        return -1
    value = lastIndex(arr, i+1, element)
    if (value == -1):
        if (arr[i] == element):
            return i
        else:
            return -1
    else:
        return value

# print(lastIndex(inputArr, 0, 2))

def allIndices(arr, i, element):
    if (i == len(arr)):
        return []
    if (element == arr[i]):
        return [i] + allIndices(arr, i+1, element)
    else:
        return allIndices(arr, i+1, element)

    
# ans = allIndices(inputArr, 0, 2)
# print(ans)

# Get Subsequence - Introduction to Arraylists 

# subsequence of a given string
# abc -> result from bc. 

def subSeq(value):
    if (len(value) == 0):
        return ['']
    ch = value[0]
    ros = value[1:]
    res = subSeq(ros)
    tempArr = []
    for i in res:
        tempArr.append(i)
    for i in res:
        tempArr.append(ch + i)
    return tempArr

# print(subSeq('abc'))

# Get Keypad Combination
# the below approach is not right, since it uses susequence logic.

def getKeyPadCombo(dialNumber):

    digit_To_Letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def getSequence(value):
        if (len(value) == 0):
            return ['']
        ch = value[0]        
        ros = value[1:]
        res = getSequence(ros)
        charVal = digit_To_Letters[ch]
        tempArr = []
        for i in charVal:
            for j in res:
                tempArr.append(i + j)
        return tempArr

    return getSequence(str(dialNumber))

# print(getKeyPadCombo(72))

# Get Stairs Path - Question | Recursion

def getStairs(n):
    pass

print(getStairs(4))





























































