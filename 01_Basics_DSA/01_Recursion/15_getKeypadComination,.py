# get keypad combinations

# Leetcode 17. 
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digit):

    def showDigit(digit):
        if (len(digit) == 0):
            return ['']

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

        ch = digit[0]
        res = digit[1:]
        result_Res = showDigit(res)

        arrList = []
        chValue = digit_To_Letters[ch]
        for i in chValue:
            for j in result_Res:
                arrList.append(i + j)
        return arrList

    if len(digit) == 0:
        return []
    else:
        return showDigit(digit)

ans = letterCombinations('67')
print(ans)
print(len(ans))

