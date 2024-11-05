# Get Subsequence - Introduction to Arraylists

# string methods

def strFun():
    test = 'hello'
    print(test)
    for i in test:
        print(i)
    print('Substring: ', test[0:2])    
    
# strFun()

# array methods

def arrFun():
    arr = []
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)
    for i in range(len(arr)):
        print(arr[i])
    
    # changing values in array 
    arr[2] = 300
    print(arr)

    # adding values at a given index
    arr.insert(2, 4000)
    print('Array after insertion ', arr)

arrFun()
