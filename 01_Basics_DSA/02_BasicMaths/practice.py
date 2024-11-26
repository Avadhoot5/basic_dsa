# Basic Maths 

# extracting the digits

def digit(n):
    while(n > 0):
        last = n % 10
        print(last)
        n = n // 10

# ans = digit(3492)

# 1. count the digits 

def countDigit(n):
    ctr = 0
    while (n > 0):
        ctr += 1
        n = n // 10
    return ctr

# ans = countDigit(329)
# print(ans)

import math

def countWithLog(n):
    count = int(math.log10(n) + 1)
    return count

# print(countWithLog(9424))

# whenever division comes then the TC is log.

# TC - Log10(n) - no of iterations depends on the the division. log2(n) = if n // 2

# 2. reverse a number

def reverse(n):
    rev = 0
    while(n > 0):
        lastDig = n % 10
        rev = (rev * 10) + lastDig
        n = n // 10
    return rev

# print(reverse(10400))

# 3. palindrome or not.

def palindrome(n):
    rev = 0
    temp = n
    while (temp > 0):
        lastDigit = temp % 10
        rev = (rev*10) + lastDigit
        temp = temp // 10

    if (rev == n):
        print('Palindrome')
    else:
        print('Not Palindrome')

# palindrome(3253)

# 4. armstrong numbers - eg. 371 = 3 cube 3 + 7 cube 3 + q cube 3 = 371

def armStrong(n):
    temp = n
    sum = 0
    while (n > 0):
        lastD = n % 10
        sum += (lastD*lastD*lastD)
        n = n // 10
    
    if (sum == temp):
        print('Armstrong Number')
    else:
        print('Not Armstrong Number')

# armStrong(371)

# 5. print all divisions.

def printDivisor(n):
    for i in range(1, n+1):
        if (n % i == 0):
            print(i)

# TC. is O(n)

# printDivisor(36) 

# alt method - but better

def printDivisorALt(n):
    myList = []
    # O(sqrt(n))
    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            myList.append(i)
            if(n//i != i):
                myList.append(int(n//i))
    # (n * log(n))
    myList.sort()
    # (O(n)) 
    for i in myList:
        print(i)

# printDivisorALt(36)

# TC =  O(sqrt(n)) + (n * log(n)) + (O(n)) 

# 6. prime or not.

def primeCheck(n):
    if (n == 1):
        print('Not Prime Number')
        return
    if (n == 2):
        print('Prime Number')
        return
    isPrime = True
    for i in range(2, int((n**0.5)) + 1):
        if (n % i == 0):
            isPrime = False
            break
    if (isPrime):
        print('Prime Number')
    else:
        print('Not Prime Number')

# primeCheck(8)

# 7. GCD / HCF - greatest common divisor / highest common factor

def gcd(a, b):
    ans = 0
    for i in range(1, a+1):
        if (a % i == 0 and b % i == 0):
            ans = i
    return ans

print(gcd(11, 23))

