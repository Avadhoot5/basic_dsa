# Print Decreasing using recursion

def recDec(n):
    if (n == 0): return
    print(n)
    recDec(n-1)

# recDec(8)

# Print Increasing using Recursion

def recInc(n):
    if (n == 0): return
    recInc(n-1)
    print(n)

# recInc(8)

#  Print Decreasing Increasing Numbers using Recursion

def recDecInc(n):
    if (n == 0): return
    print(n)
    recDecInc(n-1)
    print(n)

# recDecInc(8)


