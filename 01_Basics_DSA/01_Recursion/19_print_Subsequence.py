# Print Subsequence

def printSub(word):
    if (len(word) == 0):
        return ''
    ch = word[0]
    ros = word[1:]
    printSub(ros)


printSub('abc')

