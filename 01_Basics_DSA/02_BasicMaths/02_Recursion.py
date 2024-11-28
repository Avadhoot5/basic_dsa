# Lec 5. Recursion 

# Sum of first n terms. eg n = 5. 13 + 23 + 33 + 43 + 53 = 225

# very high run time for recursive code 
def cubeNum(n):
    if (n == 0):
        return 0
    return n**3 + cubeNum(n-1)

# print(cubeNum(5))

