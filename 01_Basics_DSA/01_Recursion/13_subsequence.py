# subsequence of a given string

# abc -> result from bc. 


def recStr(str):
    if (len(str) == 0):
        return ['']
    ch = str[0]
    ros = str[1:]
    rres = recStr(ros)
    mres = []
    for i in rres:
        mres.append('' + i)
    for i in rres:
        mres.append((ch + i))
    return mres

ans = recStr('abc')

print(ans)
