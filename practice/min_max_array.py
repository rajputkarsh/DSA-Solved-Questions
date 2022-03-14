def findMinMax(arr):

    if len(arr) < 1:
        print(None)
        return 0

    (minNum, maxNum) = (arr[0], arr[0])

    for num in arr:
    
        # compare for max
        if num > maxNum:
            maxNum = num

        # compare for min
        if num < minNum:
            minNum = num

    print("Min - {0} and Max - {1}".format(minNum, maxNum))

array = [1000, 11, 445, 1, 330, 3000]
findMinMax(array)
findMinMax([])