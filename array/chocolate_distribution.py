def findMinDifference(arr, m):

    arr.sort()
    i = m-1
    minDiff = 99999

    while i < len(arr):
        diff = arr[i] - arr[i-m+1]
        if diff < minDiff:
            minDiff = diff
        i += 1

    return minDiff


array = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5

print(findMinDifference(array, m))
