# Leaders in an Array

# brute force 

# TC. O(N*N). SC. O(N)

leaderArr = [10, 22, 12, 3, 0, 6]

def leadersInArrBF(arr):
    result = []
    n = len(arr)

    for i in range(0, n):
        isLeader = True
        for j in range(i+1, n):
            if (arr[j] > arr[i]):
                isLeader = False
                break
        if (isLeader):
            result.append(arr[i])
    return result

print(leadersInArrBF(leaderArr))

# optimal. TC. O(N). SC. O(N)

def leadersInArrO(arr):
    maxElement = 0
    n = len(arr)
    result = []

    for i in range(n-1, -1, -1):
        if (arr[i] > maxElement):
            result.append(arr[i])
            maxElement = arr[i]
    
    return result

print(leadersInArrO(leaderArr))
