# predict the output

def pred(n):
    if (n == 0):
        return 
    print('Pre' + str(n))
    pred(n-1)
    print('In' + str(n))
    pred(n-1)
    print('Post' + str(n))

pred(2)
