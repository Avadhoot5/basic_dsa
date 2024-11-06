# Get Keypad Combination

def letterCombinations(digits):
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
    
    if (len(digits) == 0):
        return []
    
    letter = ''
    for i in digits:
        letter += digit_To_Letters[i]

    def getSeq(str):
        if (len(str) == 0):
            return ['']
        ch = str[0]
        ros = str[1:]
        gsq = getSeq(ros)

        mres = []
        for i in gsq:
            mres.append('' + i)
        for i in gsq:
            mres.append(ch + i)
        
        return mres

    arrList = getSeq(letter)
    return arrList


ans = letterCombinations('25')
print(ans)





