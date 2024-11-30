# Lec 5. Recursion 

# Sum of first n terms. eg n = 5. 13 + 23 + 33 + 43 + 53 = 225

# very high run time for recursive code 
def cubeNum(n):
    if (n == 0):
        return 0
    return n**3 + cubeNum(n-1)

# print(cubeNum(5))

# Basic recursion problems

# print name 5 times

def printName(n):
    if (n == 0):
        return
    print('name')
    printName(n-1)

# printName(5)

# recursion - print from 1 to n

def recPrint(n):
    if (n == 0):
        return
    recPrint(n-1)
    print(n)

# recPrint(8)

# print from n to 1 

def recPrint1ToN(n):
    if (n == 0):
        return
    print(n)
    recPrint1ToN(n-1)

# recPrint1ToN(5)

# backtrack 1 to n

def print1ToNBT(i, n):
    if (i == 0):
        return
    print1ToNBT(i-1, n)
    print(i)

# print1ToNBT(3,3)

# backtrack n to 1

def printNto1BT(i, n):
    if (i > n):
        return
    printNto1BT(i+1, n)
    print(i)

# printNto1BT(1, 3)

# sum of first N numbers. - 2 methods - parameterised way, functional way

def sumOfNnumParameter(i, sum):
    if (i < 1):
        print(sum)
        return
    sumOfNnumParameter(i-1, sum+i)

# sumOfNnumParameter(10, 0)

def sumOfNnum(n):
    if (n == 0):
        return 0
    return n + sumOfNnum(n-1)

# print(sumOfNnum(10))

def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

# print(fact(4))

# print fact for every number less than or equal to N

def factPrint(n):
    if (n==0):
        return 1
    value = factPrint(n-1)
    print(value * n, end = ' ')
    return value * n

# factPrint(3)

# reverse an array

arr = [1, 4, 3, 2, 6, 5]

# using for loop

def revFor(arr):
    newArr = []
    for i in range(len(arr)-1, -1, -1):
        newArr.append(arr[i])
    return newArr

# print(revFor(arr))


def revTwoPointer(l, r, arr):
    if (l >= r):
        return
    arr[l], arr[r] = arr[r], arr[l]
    revTwoPointer(l+1, r-1, arr)
    return arr

# print(revTwoPointer(0, 5, arr))

def revOne(i, n, arr):
    if (i >= n//2):
        return
    arr[i], arr[n-i] = arr[n-i], arr[i]
    revOne(i+1, n, arr)
    return arr

# print(revOne(0, 5, arr))

# check if a string is palindrome or not.

def palindrome(i, s):
    if (i >= len(s)//2):
        return 'Palindrome'
    if(s[i] != s[len(s)-i-1]):
        return 'Not Palindrome'
    else:
        return palindrome(i+1, s)

# print(palindrome(0,'teset'))

# Leetcode question - 

def palindromeLC(s):
    ans = ''
    for i in s:
        if (i.isalnum()):
            ans += i
    return ans.lower() == ans[::-1].lower()

# result = palindromeLC('A man, a plan, a canal: Panama')
# print(result)

# Optimal solution

def palindromeLCO(s):
    l = 0
    r = len(s) - 1

    def alphaNum(c):
        (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))

    while(l < r):
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if (s[l] != s[r]):
            return False
        l, r = l+1, r-1
    return True

# result = palindromeLC('A man, a plan, a canal: Panama')
# print(result)

# Multiple recursion calls

def fibo(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    last = fibo(n-1)
    secondLast = fibo(n-2)
    return last + secondLast

# print(fibo(5))

