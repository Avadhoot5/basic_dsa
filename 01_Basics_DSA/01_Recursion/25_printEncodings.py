# Print encodings.

def printEncoding(str, ans):
    
    encode = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

