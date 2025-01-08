# Rotate Matrix/Image by 90 Degrees

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]

# TC. O(N*N). SC. O(N*N)

def rotateMatrixBF1(matrix, n):
    final = []

    for i in range(0, n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(matrix[j][i])
        final.append(temp)
    return final

print(rotateMatrixBF1(matrix, len(matrix)))
# print(rotateMatrixBF1(matrix2, len(matrix2)))

# optimal approach 


def rotateMatrixO(matrix):
    n = len(matrix)
    for i in range(n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

    return matrix

print(rotateMatrixO(matrix))

