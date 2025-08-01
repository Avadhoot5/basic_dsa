# 1. first occurence

# arr = [2,5,7,8,2,6,8,1]

# def lastOccr(arr, i, n):
#     if (i == len(arr)):
#         return -1
    

# ans = lastOccr(arr, 0, 8)
# print(ans)

# 2. leetcode 17 - get keypad combinations.

# def letterCombinations(digit):

#     def digitNum(digit):
        
#         if (len(digit) == 0):
#             return ['']

#         digit_To_Letters = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz',
#         }

#         ch = digit[0]
#         res = digit[1:]
#         result_Res = digitNum(res)
#         chValue = digit_To_Letters[ch]
#         lettersArray = []
#         for i in chValue:
#             for j in result_Res:
#                 lettersArray.append((i+j))
#         return lettersArray

#     if (len(digit) == 0):
#         return []
#     else:
#         return digitNum(digit)


# ans = letterCombinations('67')
# print(ans)
# print(len(ans))

# 3. tower of hanoi

# Question link
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# where, n is no of discs. A - source, B - destination, C - helper

# def toc(n, a, b, c):
#     if (n == 0):
#         return
#     toc(n-1, a, c, b)
#     print(n, a, b)
#     toc(n-1, c, b, a)

# toc(3, 'A', 'B', 'C')

# subsequence of a given string

# def getSeq(word):
#     # base case
#     if (len(word) == 0):
#         return ['']

#     ch = word[0]
#     ros = word[1:]
#     ros_Result = getSeq(ros)
#     final_Result = []
#     for i in ros_Result:
#         final_Result.append('' + i)    
#     for i in ros_Result:
#         final_Result.append(ch + i)
    
#     return final_Result

# print(getSeq('abc'))

# encode =  ["0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def printEnc(num, ans):

#     if (len(num) == 0):
#         print(ans)
#         return
    
#     if (int(num[0]) == 0):
#         return
    
#     if (len(num[0]) >= 1):
#         printEnc(num[1:], ans + encode[int(num[0])])

#     if (len(num[:2]) >= 2 and int(num[:2]) <= 26):
#         printEnc(num[2:], ans + encode[int(num[:2])])
        

# printEnc('123', '')

# def permArr(arr):
#     value = ''.join(map(str, arr))
    
#     def fn(value):

#         if (len(value) == 0):
#             return ['']
        
#         resultArr = []

#         for i in range(0, len(value)):
#             ch = value[i]
#             lstr = value[:i]
#             rstr = value[i+1:]
#             fstr = lstr + rstr
#             ans = fn(fstr)
#             for i in ans:
#                 resultArr.append(ch + i)

#         return resultArr

#     return fn(value)

# ans = permArr([1,2,3])
# print(ans)

# numbers = [1, 6, 7, 8, 11, 13, 14, 18, 19, 21, 22, 23, 25, 27, 33, 34, 35, 37, 41, 42, 49, 50, 51, 54, 56, 59, 60, 62, 65, 66, 73, 74, 77, 82, 88, 89, 90, 92]

# def bSearch(arr, n):
#     low = 0
#     high = len(arr)
    

# ans = bSearch(numbers, 19)
# print(ans)

# 10/4/25

# factorial of n 

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

# ans = fact(5)
# print(ans)

# n power x

def pow(x, n):
    if (n == 0):
        return 1
    res = pow(x, n-1) * x
    return res

# print(pow(2, 4))


# n power x using log time

def powLog(x, n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        return pow(x, n // 2) * pow(x, n // 2)
    else:
        return x * pow(x, n // 2) * pow(x, n // 2)

# print(powLog(2, 5))


# predict the output

def predict(n):
    if (n == 0):
        return
    print('Pre ' + str(n))
    predict(n-1)
    print('In ' + str(n))
    predict(n-1)
    print('Post ' + str(n))

# predict(2)

# tower of hanoi

# Question link
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# where, n is no of discs. A - source, B - destination, C - helper

def towerOhHanoi(n, A, B, C):
    if (n == 0):
        return
    towerOhHanoi(n-1, A, C, B)
    print(n, A, B)
    towerOhHanoi(n-1, C, B, A)

# towerOhHanoi(3, 'A', 'B', 'C')

arr = [42,7,19,3,88,56,3,14,27,3,65,91]

def displayArr(arr, idx):
    if (idx < 0):
        return
    print(arr[idx])
    displayArr(arr, idx-1)

# displayArr(arr, len(arr)-1)

# maximum in an array

def maxElementArr(arr, idx):
    if (idx == len(arr)):
        return 0
    currentValue = maxElementArr(arr, idx+1)
    if (arr[idx] > currentValue):
        return arr[idx]
    else:
        return currentValue

# print(maxElementArr(arr, 0))

# return first Index in an array.

def firstIndex(arr, idx, element):
    if (idx == len(arr)):
        return -1
    if (arr[idx] == element):
        return idx
    else:
        return firstIndex(arr, idx+1, element)

# print(firstIndex(arr, 0, 3))

# return last Index in an array.

def lastIndex(arr, idx, element):
    if (idx == len(arr)):
        return -1
    value = lastIndex(arr, idx+1, element)
    if (value == -1):
        if (arr[idx] == element):
            return idx
        else:
            return value
    else:
        return value

# print(lastIndex(arr, 0, 3))

# all indices in an array

def allIndices(arr, idx, element):
    if (idx == len(arr)):
        result = []
        return result
    value = allIndices(arr, idx+1, element)
    if (element == arr[idx]):
        value.append(idx)
        return value
    else:
        return value

# print(allIndices(arr, 0, 3))

# subsequence of a given string

# abc -> result from bc. 

def subStr(value):
    if (len(value) == 0):
        return ['']
    char = value[0]
    rss = value[1:]
    answer = subStr(rss)
    mres = []
    for i in answer:
        mres.append('' + i)
    for i in answer:
        mres.append(char + i)
    return mres

# print(subStr('abc'))

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
        char = value[0]
        ros = value[1:]
        digToString = digit_To_Letters[char]
        rres = getSequence(ros)
        mres = []
        for i in digToString:
            for j in rres:
                mres.append(i + j)
        return mres   

    answer = getSequence(dialNumber)
    return answer

# print(getKeyPadCombo('67'))

# Get Stairs Path - Question | Recursion

def getStairs(n):
    if (n == 0):
        return ['']
    if (n < 0):
        return []
    
    path1 = getStairs(n-1)
    path2 = getStairs(n-2)
    path3 = getStairs(n-3)
    result = []

    for i in path1:
        result.append('1' + i)
    
    for i in path2:
        result.append('2' + i)
    
    for i in path3:
        result.append('3' + i)
    
    return result

# print(getStairs(4))

# Get maze paths 

def getMazePath(sr, sc, dr, dc):
    if (sr == dr and sc == dc):
        return ['']

    hPath = []
    vPath = []

    if (sc < dc):
        hPath = getMazePath(sr, sc+1, dr, dc)
    if (sr < dr):
        vPath = getMazePath(sr+1, sc, dr, dc)

    paths = []
    for i in hPath:
        paths.append('h' + i)
    for i in vPath:
        paths.append('v' + i)

    return paths

# print(getMazePath(1,1,3,3))

# Get maze paths with jump value

def getMazePaths(sr, sc, dr, dc):

    if (sr == dr and sc == dc):
        return ['']    
    paths = []
    for hs in range(1, (dc-sc)+1):
        hPath = getMazePaths(sr, sc + hs, dr, dc)
        for i in hPath:
            paths.append('h' + str(hs) + i)

    for vs in range(1, (dr-sr)+1):
        vPath = getMazePaths(sr + vs, sc, dr, dc)
        for i in vPath:
            paths.append('v' + str(vs) + i)

    for ds in range(1, (dc-sc)+1 and (dr-sr)+1):
        dPath = getMazePaths(sr + ds, sc + ds, dr, dc)
        for i in dPath:
            paths.append('d' + str(ds) + i)
    return paths

# print(getMazePaths(1, 1, 3, 3))

# Print Subsequence

def printSeq(ques, ans):

    if (len(ques) == 0):
        print(ans)
        return
    char = ques[0]
    ros = ques[1:]
    printSeq(ros, ans + '')
    printSeq(ros, ans + char)

# printSeq('abc', '')

# printKPC - keypad combo

# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# ad,ae,af,bd,be,bf,cd,ce,cf

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

def printKPC(ques, ans):
    if (len(ques) == 0):
        print(ans)
        return
    char = ques[0]
    ros = ques[1:]
    value = digit_To_Letters[char]
    for i in value:
        printKPC(ros, ans + i)

# printKPC('678', '')

# print stair paths
def getStairs(n, path):
    if (n == 0):
        print(path)
        return
    if (n < 0):
        return

    getStairs(n-1, path + '1')
    getStairs(n-2, path + '2')
    getStairs(n-3, path + '3')

# getStairs(4, '')

# print the maze Paths.

def printMazePath(sr, sc, dr, dc, ans):
    if (sr == dr and sc == dc):
        print(ans)
        return

    if (sr < dr):
        printMazePath(sr+1, sc, dr, dc, ans + 'v')
    if (sc < dc):
        printMazePath(sr, sc+1, dr, dc, ans + 'h')

# printMazePath(1, 1, 3, 3, '')

# print the maze Paths with Jump

def printMPJ(sr, sc, dr, dc, ans):

    if (sr == dr and sc == dc):
        print(ans)
        return
    
    for hs in range(1, (dc - sc)+1):
        printMPJ(sr, sc + hs, dr, dc, ans + 'h' + str(hs))
    
    for vs in range(1, (dr - sr) + 1):
        printMPJ(sr + vs, sc, dr, dc, ans + 'v' + str(vs))
    
    for ds in range(1, (dr-sr)+1 and (dc-sc)+1):
        printMPJ(sr + ds, sc + ds, dr, dc, ans + 'd' + str(ds))
    
# printMPJ(1, 1, 3, 3, '')

# Print permutations

def printPT(ques, ans):
    if (len(ques) == 0):
        print(ans)
        return
    
    for i in range(len(ques)):
        char = ques[i]
        lString = ques[:i]
        rString = ques[i+1:]
        ros = lString + rString
        printPT(ros, ans + char)

# printPT('abc', '')

# Print encoding - 2 types to solve this .

encode = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def printEncoding(que, ans):

    if (len(que) == 0):
        print(ans)
        return
    if (len(que) == 1):
        if (int(que) == 0):
            return
        else:
            print(ans + str(encode[int(que)]))
    else:
        char = que[0]
        roq = que[1:]

        if (int(char) == 0):
            return
        else:
            printEncoding(roq, ans + str(encode[int(char)]))
        
        char12 = que[:2]
        roq = que[2:]
        
        if (int(char12) <= 26):
            printEncoding(roq, ans + str(encode[int(char12)]))


# printEncoding('12103', '')
# print('Break Point')
# printEncoding('123', '')



