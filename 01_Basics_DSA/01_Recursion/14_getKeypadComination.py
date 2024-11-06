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
    ch = digits[0]
    ros = digits[1:]


