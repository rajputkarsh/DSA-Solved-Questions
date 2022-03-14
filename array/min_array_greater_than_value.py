


def findArray(arr, target):

    arr.sort(reverse=True)

    size = 0
    currentSum = 0

    if arr[-1] > target:
        return size
    
    for element in arr:
        if currentSum >= target:
            return size
        else:
            currentSum += element
            size += 1

    return (0 if currentSum < target else size)


def findContiguousArray(arr, target):
    i = 0
    j = 0
    minSize = len(arr)

    if sum(arr) < target:
        return 0

    if min(arr) > target:
        return 0

    if len(arr) <= 0:
        return 0

    while i <= len(arr)-1 and j <= len(arr)-1:
        print("checking window {0}-{1} : Sum - {2}".format(i, j, sum(arr[i:j+1])), end="\t")
        if sum(arr[i:j+1]) >= target:
            if j+1-i < minSize:
                minSize = j+1-i
            i += 1
        else:
            j += 1

        print("minsize = {0}".format(minSize))

    return minSize


array = [10, 2, 3]
m = 6

print(findContiguousArray(array, m))
