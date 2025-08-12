# Lec 5. Recursion 

# Sum of first n terms. eg n = 5. 13 + 23 + 33 + 43 + 53 = 225

# very high run time for recursive code 

def recFn(n):
    if (n == 0):
        return 0
    value = n**3
    return value + recFn(n-1)

# print(recFn(5)) 

# Basic recursion problems

# print name 5 times

def printName(n):
    if (n == 0):
        return 
    print('test name')
    printName(n-1)

# printName(5)

# recursion - print from 1 to n

def print1ToN(n):
    if (n == 0):
        return
    print1ToN(n-1)
    print(n)

# print1ToN(10)

# print from n to 1 

def printNTo1(n):
    if (n == 0):
        return
    print(n)
    printNTo1(n-1)

# printNTo1(10)

# sum of first N numbers. - 2 methods - parameterised way, functional way

def sumOfNnumParameter(i, sum):
    if (i == 0):
        print(sum)
        return
    return sumOfNnumParameter(i-1, sum+i)

# sumOfNnumParameter(10, 0)

def sumOfNnum(n):
    if (n == 0):
        return 0
    value = n + sumOfNnum(n-1) 
    return value

# print(sumOfNnum(10))

def fact(n):
    if (n == 0):
        return 1
    value = n * fact(n-1)
    return value

# print(fact(5))

# print fact for every number less than or equal to N

def factPrint(n):
    if (n==0):
        return 1
    value = n * factPrint(n-1)
    print(value)
    return value

# factPrint(5)

# reverse an array

inputArr = [1, 4, 3, 2, 6, 5, 9]

# using for loop

def revArr(arr):
    newArr = []
    for i in range(len(arr)-1, -1, -1):
        newArr.append(arr[i])
    return newArr

# print(revArr(inputArr))

def revTwoPointer(arr):
    l = 0
    r = len(arr)-1

    while (l <= r):
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    return arr

# print(revTwoPointer(inputArr))

inputArr2 = [1, 4, 3, 2, 6, 5, 9]

def revUsingRecursion(l, r, arr):
    if (l >= r):
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return revUsingRecursion(l+1, r-1, arr)

# ans = revUsingRecursion(0, 6, inputArr2)
# # print(ans)

def revOne(i, arr):
    if (i >= len(arr)//2):
        return arr
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    return revOne(i+1, arr)

# print(revOne(0, inputArr2))

# result [9, 5, 6, 2, 3, 4, 1]

# check if a string is palindrome or not.

def palindrome(i, s):
    if (i >= len(s)//2):
        return 'Palindrome'
    if (s[i] != s[len(s)-1-i]):
        return 'Not Palindrome'
    else:
        return palindrome(i+1, s)

# print(palindrome(0,'teset'))

# Leetcode question - 

# Optimal solution
def palindromeLCO(s):
    l = 0
    r = len(s)-1

    def alphaNum(c):
    # ord function returns the unicode of the specific character.
        return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
    
    while (l < r):
        while (l < r and not alphaNum(s[l])):
            l += 1
        while (r > l and not alphaNum(s[r])):
            r -= 1
        if (s[l].lower() != s[r].lower()):
            return False
        l, r = l+1, r-1

    return True

# result = palindromeLCO('A man, a plan, a canal: Panama')
# print(result)

# Multiple recursion calls
def fibo(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibo(n-1) + fibo(n-2)

# print(fibo(5))




