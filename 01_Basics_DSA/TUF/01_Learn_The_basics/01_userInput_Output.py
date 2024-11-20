# input output in python 

n = input('Enter a number: ')
print(n)

# Data types - gfg

def dataSize(str):
    if (str == 'Character'):
        return 1
    if (str == 'Integer'):
        return 4
    if (str == 'Long'):
        return 8
    if (str == 'Float'):
        return 4
    if (str == 'Double'):
        return 8

ans = dataSize('Character')
print(ans)
