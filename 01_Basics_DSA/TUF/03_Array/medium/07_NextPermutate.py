# Next Permutation 

# brute force approach
# 1. using recursion - generate all the possible permutation in sorted manner
# 2. using Linear search - search for the instance, and return next index.
# 3. If the value is last element, return the 1st element.

# printing permutation using recursion.

def nextPermBF(value):
    pass

# print(nextPermBF(312))

nextArr = [2, 1, 5, 4, 3, 0, 0]
nextArr2 = [1,3,2]

# Self tried algorithm 

def nextPermOMine(arr):
    breakPoint = -1
    n = len(arr)
    elementIdx = -1
    currentValue = [i for i in arr]
    finalValue = []

    for i in range(0, n):
        if (arr[i] < arr[i+1]):
            breakPoint = i
            break
    if (breakPoint != -1):
        smallest = arr[breakPoint+1]
        for j in range(breakPoint+1, n):
            if (arr[j] > arr[breakPoint]):
                if (smallest > arr[j]):
                    smallest = arr[j]
                    elementIdx = j
        currentValue[breakPoint], currentValue[elementIdx] = currentValue[elementIdx], currentValue[breakPoint]

        # adding the elements till the breakpoint
        finalValue += currentValue[:breakPoint+1]
        # print(finalValue)
        subList = currentValue[breakPoint+1:]
        subList.sort()
        finalValue += subList
        # print(finalValue)

    else:
        arr.sort()
    
    return finalValue

print(nextPermOMine(nextArr))
print(nextPermOMine(nextArr2))

nextArrN = [2, 1, 5, 4, 3, 0, 0]

def nextPermO(arr):
    idx = -1
    n = len(arr)

    for i in range(n-2, -1, -1):
        if (arr[i] < arr[i+1]):
            idx = i
            break

    if (idx == -1):
        return arr.reverse()
    else:
        for i in range(n-1, idx, -1):
            if (arr[i] > arr[idx]):
                arr[i], arr[idx] = arr[idx], arr[i]
                break
    tempArr = arr[idx+1::]
    tempArr.reverse()
    return arr[:idx+1] + tempArr

print(nextPermO(nextArrN))

