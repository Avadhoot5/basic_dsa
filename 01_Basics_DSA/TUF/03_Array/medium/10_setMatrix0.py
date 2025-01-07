# Set Matrix Zeroes | O(1) Space Approach

# Brute force 
# 1.) traverse in the matrix and search for 0s. and mark the respective col and row elements with -1.
# 2.) Again loop through the matrix and convert the -1 to 0s

# TC. O(N*M) + O(N+M) + O(N*M)

matrix = [[1,1,1],[1,0,1],[1,1,1]]

def setMatrixZeroBF(matrix, n, m):

    def markRow(matrix, n, m, i):
        for j in range(0, m):
            if (matrix[i][j] != 0):
                matrix[i][j] = -1

    def markCol(matrix, n, m, j):
        for i in range(0, n):
            if (matrix[i][j] != 0):
                matrix[i][j] = -1
    
    # Finding 0s, and marking the entire rows and cols to -1.
    for i in range(0, n):
        for j in range(0, m):
            if (matrix[i][j] == 0):
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == -1):
                matrix[i][j] = 0
    return matrix

ans = setMatrixZeroBF(matrix, len(matrix), len(matrix[0]))
print(ans)

# Output: [[1,0,1],[0,0,0],[1,0,1]]

# better approach. TC. -> O 2*(N*M). SC -> O(N+M)

matrixB = [[1,1,1],[1,0,1],[1,1,1]]

def setMatrixZeroB(matrix, n , m):
    rowM = [0] * n
    colM = [0] * m

    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == 0):
                rowM[i] = 1
                colM[j] = 1

    for i in range(n):
        for j in range(m):
            if (rowM[i] or colM[j]):
                matrix[i][j] = 0
    
    return matrix

print(setMatrixZeroB(matrixB, len(matrixB), len(matrixB[0])))

# optimal approach 

def setMatrixZeroO(matrix, n , m):
    # colM = [0] * m -> matrix[0][..]
    # rowM = [0] * n -> matrix[..][0]
    colZero = 1

    for i in range(0, n):
        for j in range(0, m):
            if (matrix[i][j] == 0):

                # mark the i-th row
                matrix[i][0] = 0
                # mark the j-th col
                if (j != 0):
                    matrix[0][j] = 0
                else:
                    colZero = 0
    for i in range(1, n):
        for j in range(1, m):
            if (matrix[i][j] != 0):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
    
    if (matrix[0][0] == 0):
        for j in range(m):
            matrix[0][j] = 0

    if (colZero == 0):
        for i in range(n):
            matrix[i][0] = 0

    return matrix
    
ans = setMatrixZeroO(matrixB, len(matrixB), len(matrixB[0]))
print(ans)

