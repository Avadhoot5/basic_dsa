# Hashing Maps TC Collisions Division Rule of Hashing

# number hashing

arr = [1,2,5,2,1,3,2,9,7,6]

hashArr = {}

def countNum(n):
    for i in range(0, len(arr)-1):
        if (arr[i] in hashArr):
            hashArr[arr[i]] += 1
        else:
            hashArr[arr[i]] = 1
    return hashArr.get(n)

print(countNum(3))

alphaArr = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e']

alphaHash = {}

def charHash(ch):
    for i in alphaArr:
        if (i in alphaHash):
            alphaHash[i] += 1
        else:
            alphaHash[i] = 1
    return alphaHash[ch]

print('Character appears')
print(charHash('d'))
