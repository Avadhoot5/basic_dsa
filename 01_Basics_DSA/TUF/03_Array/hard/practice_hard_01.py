# Pascal Triangle

# 3 types of questions - 
# 1. find the element at that place R and C.
# 2. Print the Nth row of pascal triangle.
# 3. given N, print the entire triangle.

# 1st type.
# 5C3 -> row = 5; col = 3; ans = 6

# [TC: O(R), SC: O(1)]

def element_n_c_r(n, r):
    res = 1
    n, r = n-1, r-1

    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    
    return res

# print(element_n_c_r(5, 3))

# 2nd type 

# brute - [TC: O(N* R), SC: O(1)]

def print_n_row_brute(n):

    for i in range(1, n+1):
        value = element_n_c_r(n, i)
        print(value, end = ' ')

# print_n_row_brute(5)

# better - [TC: O(N), SC: O(1)]

def print_n_row_better(n):
    res = 1
    ans = [1]
    for i in range(1, n):
        res = res * (n-i)
        res = res // (i)
        ans.append(res)
    return ans 

# print(print_n_row_better(6))

# 3rd Type

# [TC: O(N*N), SC: O(1) - returning the ans]

def pascal_tri(n):
    temp = []

    for i in range(1, n+1):
        temp.append(print_n_row_better(i))
    
    return temp

# print(pascal_tri(6))



