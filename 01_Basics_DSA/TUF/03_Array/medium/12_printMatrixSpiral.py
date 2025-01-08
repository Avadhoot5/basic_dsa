# Spiral Traversal of a Matrix | Spiral Matrix

# implementation logic
# code clean check

# TC. O(N*M). SC. O(N)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# 1 2 3
# 4 5 6
# 7 8 9

def spiralTrav(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # assigning directions
    top = 0
    left = 0
    right = m - 1
    bottom = n - 1
    result = []

    while (top <= bottom and right <= left):
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        if (top <= bottom):
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if (left <= right):
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return matrix

print(spiralTrav(matrix))

# Output: [1,2,3,6,9,8,7,4,5]

