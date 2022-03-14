def findSum(arr):
    maxSum = -99999999
    currentSum = 0

    for element in arr:
        currentSum += element

        if currentSum > maxSum:
            maxSum = currentSum
    
        currentSum = 0 if currentSum < 0 else currentSum

    print("Max sum is", maxSum)


array = [-1, -2, -3, -4]
findSum(array)