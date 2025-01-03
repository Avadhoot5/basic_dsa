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
nextArr2 = [1, 2, 3]

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
        print(finalValue)
        subList = currentValue[breakPoint+1:]
        subList.sort()
        finalValue += subList
        print(finalValue)

    else:
        arr.sort()
    
    return finalValue


print(nextPermOMine(nextArr))
print(nextPermOMine(nextArr2))

def nextPermO(arr):
    pass

print(nextPermO(nextArr))

