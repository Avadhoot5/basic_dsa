# basic Math practice

# Basic Maths 
# extracting the digits

def extractNum(n):
    while (n > 0):
        last = n % 10
        print(last)
        n = n // 10

# extractNum(923524)

# 1. count the digits

def countDigit(n):
    ctr = 0
    while (n > 0):
        ctr += 1
        n = n // 10
    return ctr

# print(countDigit(32239))

# using log
import math

def countDigit2(n):
    return int(math.log10(n)) + 1

# print(countDigit2(32239))

# 2. reverse a number

def revNum(n):
    rev = 0
    while (n > 0):
        lastDig = n % 10
        rev = (rev * 10) + lastDig
        n = n // 10
    return rev

# print(revNum(7789))
# print(revNum(10400)) #401

# alt - 32-bit, negative and positive cases. 

# 3. palindrome or not.

def palindrome(n):
    rev = 0
    originalN = n

    while (n > 0):
        lastDig = n % 10
        rev = rev*10 + lastDig
        n = n // 10

    return 'Palindrome' if (rev == originalN) else 'Not Palindrome'

# print(palindrome(1221))
# print(palindrome(3253))


# 4. armstrong numbers - eg. 371 = 3 cube 3 + 7 cube 3 + q cube 3 = 371

def armStrong(n):
    digitSum = 0
    originalN = n
    len_of_digit = len(str(n))

    while (n>0):
        digit = n % 10
        digitSum += (digit**len_of_digit)
        n = n // 10
    return 'ArmStrong Number' if (originalN == digitSum) else 'Not an ArmStrong'

# print(armStrong(371))
# print(armStrong(1634))
# print(armStrong(35)) #134

# 5. print all divisions.

# TC - O(N)

def printDivisor(n):
    ansList = []
    for i in range(1, n+1):
        if (n % i == 0):
            ansList.append(i)
    return ansList

# print(printDivisor(36))

# alt method - but better

def printDivisor2(n):
    ansList = []

    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            ansList.append(i)
            if (n//i != i):
                ansList.append(n//i)
    ansList.sort()
    return ansList

# print(printDivisor2(36))

# 6. prime or not.

def primeCheck(n):
    isPrime = True
    if (n==1):
        isPrime= False
    
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            isPrime = False
            break

    return isPrime

# print(primeCheck(8))
# print(primeCheck(7))

# 7. GCD / HCF - greatest common divisor / highest common factor

def gcd(a, b):
    ans = 0
    for i in range(1, min(a,b)+1):
        if (a % i == 0 and b % i == 0):
            ans = i
    return ans

# print(gcd(20, 40))

# Euclidean algorithm 

def gcdEuc(a, b):
    while (a > 0 and b > 0):
        if (a > b):
            a = a % b
        else:
            b = a % b
    if (a == 0):
        return b
    else:
        return a

# print(gcdEuc(20, 40))

# short version

def gcdEucAlt(a,b):
    while b != 0:
        print(f'old A: {a}')
        print(f'old B: {b}')
        a, b = b, a % b
        print(f'New A: {a}')
        print(f'New B: {b}')
    return a

print(gcdEucAlt(40, 20))




