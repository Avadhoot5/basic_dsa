# Print encodings.

def printEncoding(str, ans):
    
    alphaToNum = {
        '1' : 'a', '2' : 'b', '3' : 'c', '4' : 'd', '5' : 'e', '6' : 'f', '7' : 'g', '8' : 'h', '9' : 'i', '10' : 'j', '11' : 'k', '12' : 'l', '13' : 'm', '14' : 'n', '15' : 'o', '16' : 'p', '17' : 'q', '18' : 'r', '19' : 's', '20' : 't', '21' : 'u', '22' : 'v', '23' : 'w', '24' : 'x', '25' : 'y', '26' : 'z'
    }

    if (len(str) == 0):
        print(ans)
    elif (len(str) == 1):
        if (str[0] == 0):
            return
        else:
            code = alphaToNum[f'{str[0]}']
            print(ans + code)
    else:
        if (str[0] == '0'):
            return
        else:
            ch = str[0]
            ros = str[1:]
            printEncoding(ros, ans + ch)
            code = alphaToNum(str[0])
            ans = ans + code
            print(ans)



printEncoding('123', '')

