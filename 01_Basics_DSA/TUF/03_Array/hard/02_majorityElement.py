# Majority Element II | Brute-Better-Optimal

# Return all the integers appearing more the floor of n/3 times

majority_arr = [1,1,1,1,3,2,2,2]

# Brute [TC: O(N*N), SC: O(1)]

def majority_element_brute(arr):
    n = len(arr)
    ans = []

    for i in range(n):
        if (arr[i] not in ans):
            count = 0
            for j in range(n):
                if (arr[i] == arr[j]):
                    count += 1
            if (count > (n//3)):
                ans.append(arr[i])
        if (len(ans) == 2): break
    return ans 

# print(majority_element_brute(majority_arr))

# Better - HashMap [TC: O(N), SC: O(N)]

def majority_element_better(arr):
    n = len(arr)
    hash_map = {}
    result = []

    for num in arr:
        hash_map[num] = hash_map.get(num, 0) + 1

        if (hash_map[num] > n//3):
            if (num not in result): result.append(num)

    return result

# print(majority_element_better(majority_arr))

# Optimal [TC: O(N), SC: O(1)]

import sys 

def majority_element_optimal(arr):
    n = len(arr)
    min_int = -sys.maxsize

    element1, element2 = min_int, min_int
    count1, count2 = 0, 0

    for i in range(n):
        if (count1 == 0 and element2 != arr[i]):
            count1 = 1
            element1 = arr[i]
        elif (count2 == 0 and element1 != arr[i]):
            count2 = 1
            element2 = arr[i]
        elif (element1 == arr[i]): count1 += 1
        elif (element2 == arr[i]): count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    max_count1, max_count2 = 0,0

    for i in range(n):
        if (element1 == arr[i]):
            max_count1 += 1
        elif(element2 == arr[i]):
            max_count2 += 1
    
    ans = []

    if (max_count1 > n//3): ans.append(element1)
    if (max_count2 > n//3): ans.append(element2)

    return ans 

print(majority_element_optimal(majority_arr))



