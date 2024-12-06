# Zero matrix 

def zeroMatrix(matrix, n, m):
    # Write your code here.
    col = [0] * m
    row = [0] * n

    for i in range(0, n):
        for j in range(0, m):
            if (matrix[i][j] == 0):
                col[j] = -1
                row[i] = -1

    for i in range(0, n):
        for j in range(0, m):
            if (row[i] == -1 or col[j] == -1):
                matrix[i][j] = 0                

    return matrix
