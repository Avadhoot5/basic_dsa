# n power x

def power(x, n):
    if (n == 0):
        return 1
    return x * power(x, n-1)

ans = power(2, 9)
print(ans)
