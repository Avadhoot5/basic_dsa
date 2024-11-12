# Print Subsequence

def printSS(que, ans):
    if (len(que) == 0):
        print(ans)
        return
        
    ch = que[0]
    roq = que[1:]
    printSS(roq, ch + ans)
    printSS(roq, '' + ans)

printSS('abc', '')
