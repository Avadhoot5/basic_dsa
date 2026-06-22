# basic Math practice

# Basic Maths 

# extracting the digits

def extract(n):
    
    while (n>0):
        digit = n % 10
        print(digit)
        n = n//10

# extract(8129)

# 1. count the digits

def count_digits(n):
    cnt = 0
    while (n>0):
        n = n // 10
        cnt+=1
    return cnt

# print(count_digits(23234))

# using log

def count_log(n):
    import math
    
    return int(math.log10(n)) + 1

# print(count_log(2335223))

# 2. reverse a number

def reverse_num(n):
    rev = 0

    while (n>0):
        last_digit = n%10
        rev = rev*10 + last_digit
        n=n//10
    
    return rev

# print(reverse_num(9238))

# alt - 32-bit, negative and positive cases. 

def reverse_num_lc(n):
    rev = 0
    is_negative = False

    if (n<0):
        is_negative = True
        n*=-1
    
    while (n>0):
        last_digit = n % 10
        rev = rev*10 + last_digit
        n = n // 10
    
    if (rev > 2**31): return 0

    return (rev*-1) if is_negative else rev

# print(reverse_num_lc(9823))

# 3. palindrome or not.

def palindrome_check(n):
    if (n<0): return 'Not Palindrome'
    
    temp_n = n
    rev = 0
    
    while(n>0):
        last_digit = n % 10
        rev = rev*10 + last_digit
        n = n // 10
    
    return 'Palindrome' if (temp_n == rev) else 'Not Palindrome'

# print(palindrome_check(343))

# 4. armstrong numbers - eg. 371 = 3 cube 3 + 7 cube 3 + q cube 3 = 371

def armstrong_num(n):
    length = len(str(n))
    ans = 0

    for i in str(n):
        ans += (int(i)**length)
    
    return 'Armstrong' if (ans == n) else 'Not Armstrong'

# print(armstrong_num(371))
# print(armstrong_num(1634))
# print(armstrong_num(35)) #34

# 5. print all divisions.

# TC - O(N)
def print_divisors(n):

    for i in range(1, n):
        if (n % i == 0):
            print(i, end= ' ')

# print_divisors(30)

# alt method - but better

def print_divisors_b(n):
    ans = []    

    for i in range(1, int(n**0.5) + 1):
        if (n % i == 0):
            ans.append(i)
            if (n//i != i):
                ans.append(n//i)
    
    ans.sort()
    print(ans)

# print_divisors_b(30)

# 6. prime or not.

def prime_check(n):
    
    is_prime = True

    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            is_prime = False
            break

    print(f'{n} is a {'Prime' if is_prime else 'Not Prime'} number')

# prime_check(3)
# prime_check(5)
# prime_check(8)

def print_prime(n):
    
    prime_list = []

    for i in range(1, n+1):
        for j in range(2, int(i**0.5)+1):
            if (i % j == 0):
                break
        else:
            prime_list.append(i)

    print(prime_list)

# print_prime(100)


# 7. GCD / HCF - greatest common divisor / highest common factor

def gcd_hcf(a,b):
    ans = 1
    for i in range(1, min(a,b)+1):
        if (a % i == 0 and b % i == 0):
            ans = i

    print(ans)

# gcd_hcf(20,40)
# gcd_hcf(100, 85)

# Euclidean algorithm 

def gcd_hcf_ea(a,b):
    
    while (a > 0 and b > 0):
        if (a > b): a = a % b
        else: b = b % a

    return b if (a == 0) else a


# print(gcd_hcf_ea(20,40))
# print(gcd_hcf_ea(100, 85))


# Lec 5. RECURSION 

# Sum of first n terms. eg n = 5. 13 + 23 + 33 + 43 + 53 = 225

def sum_n(n):
    if (n == 0): return 0
    value = n**3
    ans = value + sum_n(n-1)
    return ans

# print(sum_n(5))

# very high run time for recursive code 

# Basic recursion problems

# print name 5 times

def print_name(name, n):
    if (n == 0): return
    print('test')
    print_name(name, n-1)

# print_name('test', 5)

# recursion - print from 1 to n

def print_asc(n):
    if (n == 0): return
    print_asc(n-1)
    print(n)

# print_asc(5)

# print from n to 1 

def print_desc(n):
    if (n == 0): return
    print(n)
    print_desc(n-1)

# print_desc(5)

# sum of first N numbers. - 2 methods - parameterised way, functional way

# parameterised 

def sum_param(n, ans):
    if (n == 0): return ans
    return sum_param(n-1, n + ans)

# print(sum_param(10, 0))

# functional 

def sum_fun(n):
    if (n == 0): return 0
    ans = sum_fun(n-1) + n
    return ans

# print(sum_fun(10))

# print fact for every number less than or equal to N

def fact(n):
    if (n == 0):
        return 1
    return n * fact(n-1)

# print(fact(4))

def print_fact(n):
    if (n == 0): return 1
    value = print_fact(n-1)
    print(n * value, end = ' ' )
    return n * value

print_fact(4)





# reverse an array

inputArr = [1, 4, 3, 2, 6, 5, 9]

# using for loop

inputArr2 = [1, 4, 3, 2, 6, 5, 9]

# result [9, 5, 6, 2, 3, 4, 1]

# check if a string is palindrome or not.

# Leetcode question - 

# Optimal solution

# Multiple recursion calls




