# n power x

def power(x, n):
    if (n == 0):
        return 1
    return x * power(x, n-1)

# ans = power(2, 9)
# print(ans)

# n power x using log time

def powerL(x, n):
    if (n == 0):
        return 1
    if (n % 2 == 0):
        return powerL(x, n//2) * powerL(x, n//2)
    else:
        return x * powerL(x, n//2) * powerL(x, n//2)

ans = powerL(2, 7)
print(ans)
