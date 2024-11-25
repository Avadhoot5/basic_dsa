# Basic Maths 

# extracting the digits

def digit(n):
    while(n > 0):
        last = n % 10
        print(last)
        n = n // 10

# ans = digit(3492)

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

# reverse a number

def reverse(n):
    rev = 0
    while(n > 0):
        lastDig = n % 10
        rev = (rev * 10) + lastDig
        n = n // 10
    return rev

print(reverse(10400))



