# Print encodings.

encode = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def printEncoding(str, ans):

    if (len(str) == 0):
        print(ans)
        return
    
    if (int(str[0]) == 0):
        return
    
    if (len(str) >= 1):
        printEncoding(str[1:], ans + encode[int(str[0])])

    if (int(str[:2]) <= 26 and len(str[:2]) >= 2):
        printEncoding(str[2:], ans + encode[int(str[:2])])

printEncoding('12103', '')

# Alternate method


def printEncoding(que, ans):
    if (len(que) == 0):
        print(ans)
        return
    elif (len(que) == 1):
        if (int(que) == 0):
            return
        else:
            print(ans + str(encode[int(que)]))
            return
    else:
        char = que[0]
        roq = que[1:]

        if (int(char) == 0):
            return
        else:
            printEncoding(roq, ans + str(encode[int(char)]))

        char12 = que[:2]
        roq12 = que[2:]

        if (int(char12) <= 26):
            printEncoding(roq12, ans + str(encode[int(char12)]))


printEncoding('12103', '')
