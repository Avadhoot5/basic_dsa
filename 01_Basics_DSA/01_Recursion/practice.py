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


