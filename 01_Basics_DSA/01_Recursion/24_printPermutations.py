# Print permutations

def printPT(str, ans):

    if (len(str) == 0):
        print(ans)
        return
    
    for i in range(0, len(str)):
        ch = str[i]
        lstr = str[:i]
        rstr = str[i+1:]
        ros = lstr + rstr
        printPT(ros, ans + ch)

printPT('abc', '')
