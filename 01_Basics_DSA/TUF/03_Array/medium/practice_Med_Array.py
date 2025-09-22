# Two sum problem 

# arr = [], target = k

# two types - 1. If sum exists return Yes/No. 2. Sum do exist return the indexes of the elements

twoArr = [2, 6, 5, 8, 11]

# TC. O(N*N). SC. O(1)

def twoSumProblemBF1(arr, k):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j] == k):
                return [i, j]
    return 'NO'

# print(twoSumProblemBF1(twoArr, 16))

def twoSumProblemBetter(arr, k):
    n = len(arr)
    hashArr = {}

    for i in range(n):
        diff = k - arr[i]
        if (diff in hashArr):
            return 'YES'
        # [hashArr[diff], i]
        hashArr[arr[i]] = i
    return 'No'

# print(twoSumProblemBetter(twoArr, 16))

def twoSumProblemO(arr, k):
    arr.sort()
    n = len(arr)
    left = 0
    right = n-1

    while (left < right):
        currentSum = arr[left] + arr[right]
        if (currentSum == k):
            return 'YES'
        elif (currentSum < k):
            left += 1
        else:
            right -=1
    return 'NO'

# print(twoSumProblemO(twoArr, 16))

# Sort an array of 0's 1's & 2's - 

sortArr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]

def sortArrBF(arr):
    arr.sort()
    return arr

# print(sortArrBF(sortArr))

# Better approach

def sortArrBetter(arr):
    count0, count1, count2 = 0,0,0
    n = len(arr)

    for i in range(n):
        if (arr[i] == 0):
            count0 += 1
        elif (arr[i] == 1):
            count1 += 1
        else:
            count2 += 1
    
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, count0 + count1):
        arr[i] = 1
    for i in range(count0 + count1, n):
        arr[i] = 2
    return arr

# print(sortArrBetter(sortArr))

# DNF - dutch national flag algo 

def sortArrO(arr):
    n = len(arr)
    low, mid = 0, 0
    high = n-1

    while (mid <= high):
        if (arr[mid] == 0):
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif (arr[mid] == 1):
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

# print(sortArrO(sortArr))

# Majority Element I | Brute-Better-Optimal | Moore's Voting Algorithm 

majorityArr = [2, 2, 3, 3, 1, 2, 2]

def majorityElementBF(arr):
    n = len (arr)
    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if (arr[i] == arr[j]):
                count += 1
        if (count > (n//2)):
            return arr[i]
    return -1

# print(majorityElementBF(majorityArr))


def majorityElementB(arr):
    n = len(arr)
    hashMap = {}

    for i in range(0, n):
        hashMap[arr[i]] = hashMap.get(arr[i], 0) + 1
    
    for i in hashMap:
        if (hashMap[i] > n//2):
            return i

# print(majorityElementB(majorityArr))

def majorityElement(arr):
    count, element = 0,0
    n = len(arr)

    for i in range(n):
        if (count == 0):
            count = 1
            element = arr[i]
        elif (element == arr[i]):
            count += 1
        else:
            count -=1
    
    maxCount = 0
    for i in range(n):
        if (arr[i] == element):
            maxCount += 1
        if (maxCount > n//2):
            return arr[i]
    return -1

# print(majorityElement(majorityArr))

# Kadane's Algorithm | Maximum Subarray Sum | Finding and Printing

maxSubArr = [-2, -3, 4, -1, -2, 1, 5, -3]

# brute force approach. TC. O(N*N*N). SC. O(1)

# better approach TC. O(N*N). SC. O(1) 

def maxSubarraySumB(arr):
    n = len(arr)
    maxSum = arr[0]

    for i in range(0, n):
        currentSum = 0
        for j in range(i, n):
            currentSum += arr[j]
            maxSum = max(maxSum, currentSum)
    return maxSum

# print(maxSubarraySumB(maxSubArr))

import sys
min_int = -sys.maxsize - 1

def maxSubarraySumO(arr):
    n = len(arr)
    maxSum = min_int
    currentSum = 0

    for i in range(n):
        currentSum += arr[i]    

        if (currentSum > maxSum):
            maxSum = currentSum

        if (currentSum < 0):
            currentSum = 0

    return maxSum

# print(maxSubarraySumO(maxSubArr))

# follow up que - print the subarray 

def maxSubarraySumO2(arr):
    n = len(arr)
    maxSum = min_int
    currentSum = 0
    start, startIdx, endIdx = -1, -1, -1

    for i in range(n):
        if (currentSum == 0):
            start = i
        currentSum += arr[i]    

        if (currentSum > maxSum):
            maxSum = currentSum
            startIdx = start
            endIdx = i

        if (currentSum < 0):
            currentSum = 0

    return [startIdx, endIdx]

# print(maxSubarraySumO2(maxSubArr))

# stock buy and sell

#  Best Time to Buy and Sell Stock 

# TC => O(N). SC. O(1)

# stockArrN = [7,6,4,3,1]

stockArr = [7, 1, 5, 3, 6, 4]

def stockArrB(arr):
    n = len(arr)
    minimum = arr[0]
    profit = 0

    for i in range(1, n):
        cost = arr[i] - minimum
        profit = max(cost, profit)
        minimum = min(minimum, arr[i])
    return profit

# print(stockArrB(stockArr))

# Rearrange Array Elements by Sign | 2 Varieties of same Problem

reArr = [3, 1, -2, -5, 2, -4]

# TC. O(N + N/2). SC. O(N)

def reArrangeBF(arr):
    n = len(arr)
    posArr = []
    negArr = []

    for i in range(n):
        if (arr[i] > 0):
            posArr.append(arr[i])
        else:
            negArr.append(arr[i])
    arr = []

    for i in range(n//2):
        arr.append(posArr[i])
        arr.append(negArr[i])

    return arr

# print(reArrangeBF(reArr))

def reArrangeBetter(arr):
    n = len(arr)
    temp = [0] * n

    pIdex, nIdx = 0, 1

    for i in range(n):
        if (arr[i] >= 0):
            temp[pIdex] = arr[i]
            pIdex += 2
        else:
            temp[nIdx] = arr[i]
            nIdx += 2

    return temp

# print(reArrangeBetter(reArr))

# variety 2  - no equal N//2.

reArr2 = [3, 1, -2, -5, 2, -4, 5, 9, 2]

def reArrangeO(arr):
    n = len(arr)
    pos, neg = [], []

    for i in range(n):
        if (arr[i] >= 0):
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    if (len(pos) > len(neg)):
        for i in range(0, len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        nextIdx = 2 * (len(neg))
        for i in range(len(neg), len(pos)):
            arr[nextIdx] = pos[i]
            nextIdx += 1
    else:
        for i in range(0, len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        nextIdx = 2 * (len(pos))
        for i in range(len(pos), len(neg)):
            arr[nextIdx] = neg[i]
            nextIdx += 1
    return arr

# print(reArrangeO(reArr2))

# Next Permutation 

nextArr = [2, 1, 5, 4, 3, 0, 0]
# nextArr2 = [1,3,2]


def nextPermO(arr):
    n = len(arr)
    idx = -1

    for i in range(n-2, -1, -1):
        if (arr[i] < arr[i+1]):
            idx = i
            break
    if (idx == -1):
        arr.reverse()
        return arr
    
    for i in range(n-1, idx, -1):
        if (arr[i] > arr[idx]):
            arr[i], arr[idx] = arr[idx], arr[i]
            break
    arr[idx+1:] = reversed(arr[idx+1:])
    return list(arr)

# print(nextPermO(nextArr))

# Leaders in an Array

# brute force 

# TC. O(N*N). SC. O(N)

leaderArr = [10, 22, 12, 3, 0, 6]

def leadersInArrBF(arr):
    n = len(arr)
    ansArr = []

    for i in range(n):
        isLeader = True
        for j in range(i+1, n):
            if (arr[j] > arr[i]):
                isLeader = False
                break
        if (isLeader):
            ansArr.append(arr[i])
    return ansArr

# print(leadersInArrBF(leaderArr))

def leadersInArrO(arr):
    n = len(arr)
    result = []
    maxElement = 0

    for i in range(n-1, -1, -1):
        if (arr[i] > maxElement):
            result.append(arr[i])
            maxElement = arr[i]

    return result

# print(leadersInArrO(leaderArr))

# Longest Consecutive Sequence 

nums = [0,3,7,2,5,8,4,6,0,1]
nums2 = [102,4,100,1,101,1,3,2]

# brute force approach.

def linearSearch(a, x):
    for i in range(len(a)):
        if (a[i] == x):
            return True
    return False

def longestSqBF1(arr):
    n = len(arr)
    longest = 1

    for i in range(n):
        x = arr[i]
        count = 0
        while (linearSearch(arr, x) == True):
            count += 1
            x += 1
        longest = max(count, longest)
    return longest

# print(longestSqBF1(nums2))

import sys
min_int = -sys.maxsize - 1

def longestSqB(arr):
    arr.sort()
    n = len(arr)
    longest = 1
    lastSmaller = min_int
    countCurrent = 0

    for i in range(n):
        if (arr[i]-1 == lastSmaller):
            countCurrent += 1
            lastSmaller = arr[i]
        elif (arr[i] != lastSmaller):
            countCurrent = 1
            lastSmaller = arr[i]

        longest = max(longest, countCurrent)

    return longest

# print(longestSqB(nums2))

def longestSqO(arr):
    newSet = set(arr)
    count = 0
    longest = 1

    for i in newSet:
        if (i-1 not in newSet):
            x = i
            count = 1
            while (x + 1 in newSet):
                count += 1
                x += 1
            longest = max(longest, count)

    return longest

# print(longestSqO(nums2))

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

    for i in range(0, n):
        for j in range(0, m):
            if (matrix[i][j] == 0):
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)

    for i in range(0, n):
        for j in range(0, m):
            if (matrix[i][j] == -1):
                matrix[i][j] = 0

    return matrix

# ans = setMatrixZeroBF(matrix, len(matrix), len(matrix[0]))
# print(ans)


matrixB = [[1,1,1],[1,0,1],[1,1,1]]

def setMatrixZeroB(matrix, n , m):
    markRow = [0] * n 
    markCol = [0] * m

    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == 0):
                markRow[i] = 1
                markCol[j] = 1
    for i in range(n):
        for j in range(m):
            if (markRow[i] or markCol[j]):
                matrix[i][j] = 0
    
    return matrix

# print(setMatrixZeroB(matrixB, len(matrixB), len(matrixB[0])))

matrixO = [[1,1,1],[1,0,1],[1,1,1]]

def setMatrixZeroO(matrix, n, m):
    
    # column[m] -> matrix[0][..]
    # rows[n] -> matrix[..][0]

    col0 = 1

    for i in range(n):
        for j in range(m):
            if (matrix[i][j] == 0):
                # mark column
                if (j != 0):
                    matrix[0][j] = 0
                else:
                    col0 = 0
                # mark row
                matrix[i][0] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if (matrix[0][j] == 0 or matrix[i][0] == 0):
                matrix[i][j] = 0
    if (matrix[0][0] == 0):
        for j in range(m):
            matrix[0][j] = 0
    if (col0 == 0):
        for i in range(n):
            matrix[i][0]

    return matrix

# print(setMatrixZeroO(matrixO, len(matrixO), len(matrixO[0])))


# Rotate Matrix/Image by 90 Degrees

matrixRotate = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrixRotate2 = [[1,2,3],[4,5,6],[7,8,9]]

# TC. O(N*N). SC. O(N*N)

# 123    741
# 456 -> 852
# 789    963

def rotateMatrixBF1(matrix, n):
    final = []

    for i in range(0, n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(matrix[j][i])
        final.append(temp)

    return final

# print(rotateMatrixBF1(matrixRotate2, len(matrixRotate2)))


def rotateMatrixO(matrix, n):

    for i in range(n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix

# print(rotateMatrixO(matrixRotate2, len(matrixRotate2)))

# Spiral Traversal of a Matrix | Spiral Matrix

# implementation logic
# code clean check

# TC. O(N*M). SC. O(N)

spiralMatrix = [[1,2,3],[4,5,6],[7,8,9]]

# 1 2 3
# 4 5 6
# 7 8 9

def spiralTrav(matrix):
    n = len(matrix)
    m = len(matrix[0])

    top, left = 0, 0
    right = m-1
    bottom = n-1
    result = []
    
    while (left <= right and top <= bottom):

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

    return result

# print(spiralTrav(spiralMatrix))

# Output: [1,2,3,6,9,8,7,4,5]

# Count Subarray sum Equals K 

longArr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
longArr2 = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]

# Brute force. TC. O(N*N). SC. O(1)

def longSubB(arr, k):
    count = 0
    n = len(arr)

    for i in range(n):
        currentSum = 0
        for j in range(i, n):
            currentSum += arr[j]
            if (currentSum == k):
                count += 1
    return count
            
print(longSubB(longArr2, 3))

def longSubO(arr, k):
    n = len(arr)
    hashMap = {}
    hashMap[0] = 1
    count = 0
    preSum = 0

    for i in range(n):
        preSum += arr[i]
        rem = preSum - k
        if (rem in hashMap):
            count += hashMap[rem]
        if (preSum in hashMap):
            hashMap[preSum] += 1
        else:
            hashMap[preSum] = 1

    return count

print(longSubO(longArr2, 3))

