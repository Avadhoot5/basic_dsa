# Print Decreasing using recursion

def printDec(n):
    if (n == 0): return
    print(n)
    printDec(n-1)

# printDec(5)

# Print Increasing using Recursion

def printInc(n):
    if (n == 0): return 
    printInc(n-1)
    print(n)

# printInc(5)

#  Print Decreasing Increasing Numbers using Recursion

def printIncDec(n):
    if (n == 0): return
    print(n)
    printIncDec(n-1)
    print(n)

# printIncDec(5)

# Factorial - Question | Recursion 

def fact(n):
    if (n == 0): return 1
    return n * fact(n-1)

# print(fact(5))

# Power (Linear) - Question

def powL(x, n):
    if (n == 0): return 1
    return x * powL(x, n-1)

# print(powL(2, 5))
# print(powL(2, 8))

# Power (Linear) -  (Logarithmic) 

def powO(x, n):
    if (n == 0): return 1
    value = powO(x, n//2)
    if (n % 2 == 0):
        return value * value
    else:
        return x * value * value

# print(powO(2, 5))
# print(powO(2, 8))

# Tower of Hanoi - Question

def toh(n, A, B, C):
    if (n == 0): return
    toh(n-1, A, C, B)
    print(n, A, '->', B)
    toh(n-1, C, B, A)

# toh(3, 'A', 'B', 'C')

# Display an Array 

inputArr = [5,7,8,2,6,8,1,2,10]

def showArr(arr, idx):
    if (idx == len(arr)): return
    print(arr[idx])
    showArr(arr, idx+1)

# showArr(inputArr, 0)

def showRevArr(arr, idx):
    if (idx == len(arr)): return
    showRevArr(arr, idx+1)
    print(arr[idx])

# showRevArr(inputArr, 0)

# Maximum of an Array 

def maxArr(arr, idx):
    if (idx == len(arr)-1): return arr[idx]
    misa = maxArr(arr, idx+1)
    if (misa > arr[idx]):
        return misa
    else:
        return arr[idx]

# print(maxArr(inputArr, 0))

# First Index of occurrence 

def firstIndex(arr, i, searchValue):
    if (i == len(arr)): return -1
    if (arr[i] == searchValue):
        return i
    else:
        return firstIndex(arr, i+1, searchValue)

# print(firstIndex(inputArr, 0, 2))

# Last index of array

def lastIndex(arr, i, element):
    if (i == len(arr)): return -1
    value = lastIndex(arr, i+1, element)
    if (value == -1):
        if (arr[i] == element):
            return i
        else:
            return -1
    return value

# print(lastIndex(inputArr, 0, 2))

def allIndices(arr, i, element):
    if (i == len(arr)): return []
    if (arr[i] == element):
        return [i] + allIndices(arr, i+1, element)
    else:
        return allIndices(arr, i+1, element)

# ans = allIndices(inputArr, 0, 2)
# print(ans)

# Get Subsequence - Introduction to Arraylists

# subsequence of a given string

# abc -> result from bc. 

def recStr(str):
    if (len(str) == 0): return ['']

    ch = str[0]
    ros = str[1:]
    rros = recStr(ros)
    mres = []
    for i in rros:
        mres.append('' + i)
    for i in rros:
        mres.append(ch + i)
    return mres

# print(recStr('abc'))

# get keypad combinations

# Leetcode 17. 
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digit):

    if (len(digit) == 0):
        return ['']

    def show_letter(num):
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        return digit_to_letters[num]
    
    chr = digit[0]
    rnum = digit[1:]
    mres = []
    rrnum = letterCombinations(rnum)
    chr_text = show_letter(chr)
    for i in rrnum:
        for j in chr_text:
            mres.append(j + i)
    return mres

# ans = letterCombinations('67')

# print(ans)

# print(len(ans))

# Get Stairs Path - Question | Recursion

def getStairs(n):
    if (n < 0): return []
    if (n == 0): return ['']
    
    jump1 = getStairs(n-1)
    jump2 = getStairs(n-2)
    jump3 = getStairs(n-3)

    mres = []

    for i in jump1:
        mres.append('1' + str(i))
    for i in jump2:
        mres.append('2' + str(i))
    for i in jump3:
        mres.append('3' + str(i))
    return mres

ans = getStairs(4)
print(ans)


