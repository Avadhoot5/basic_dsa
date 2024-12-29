#  Best Time to Buy and Sell Stock 

# TC => O(N). SC. O(1)

# stockArr = [7, 1, 5, 3, 6, 4]
stockArr = [7,6,4,3,1]

def stockArrB(arr):
    maxProfit = 0
    minimum = arr[0]

    for i in range(1, len(arr)):
        profit = arr[i] - minimum
        maxProfit = max(profit, maxProfit)
        minimum = min(minimum, arr[i])

    return maxProfit

print(stockArrB(stockArr))

