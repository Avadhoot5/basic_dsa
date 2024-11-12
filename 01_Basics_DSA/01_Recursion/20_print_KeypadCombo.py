# print keypad combination

def printKPC(que, ans):
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

    if (len(que) == 0):
        print(ans)
        return 

    ch = que[0]
    roq = que[1:]
    chValue = digit_To_Letters[ch]
    roqResult = printKPC(roq, ch + ans)
    for i in roqResult:
        printKPC(roq, i)




printKPC('23', '')

# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']