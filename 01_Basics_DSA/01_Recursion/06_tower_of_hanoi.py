# tower of hanoi

# Question link
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# where, n is no of discs. A - source, B - destination, C - helper

def towerOfHanoi(n, A, B, C):
    if (n == 0):
        return
    towerOfHanoi(n-1, A, C, B)
    print(n, A, B)
    towerOfHanoi(n-1, C, B, A)

towerOfHanoi(2, 'A', 'B', 'C')
