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

encodings =  ["0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def printEnc(nu, ans):

    if len(nu) == 0:                  
        print(ans)
        return
    
    if int(nu[0]) == 0:           
        return
    
    if len(nu) >= 1:                                                                          
        printEnc(nu[1:], ans + encodings[int(nu[0])])
    
    if int(nu[:2]) <= 26 and len(nu) >= 2:      
        printEnc(nu[2:], ans + encodings[int(nu[:2])])

printEnc('123', '')
