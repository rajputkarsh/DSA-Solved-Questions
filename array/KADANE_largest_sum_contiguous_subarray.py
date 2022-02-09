from sys import maxsize

def findSubArray(arr):
    max_sum = -maxsize - 1
    current_sum = 0

    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        if max_sum < current_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum


def findSubArray2(arr):
    max_sum = arr[0]
    current_sum = 0

    for i in range(len(arr)):
        current_sum = current_sum + arr[i]
        if current_sum < 0:
            current_sum = 0

        # Do not compare for all elements. Compare only
        # when  current_sum > 0
        elif (max_sum < current_sum):
            max_sum = current_sum

    return max_sum


def findSubArrayDP(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def findSubArrayElements(arr):
     
    max_sum = -maxsize - 1
    current_sum = 0
    start = 0
    end = 0
    s = 0
 
    for i in range(len(arr)):
 
        current_sum += arr[i]
 
        if max_sum < current_sum:
            max_sum = current_sum
            start = s
            end = i
 
        if current_sum < 0:
            current_sum = 0
            s = i+1
 
    print("Maximum contiguous sum is %d" % (max_sum))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))
    print(arr[start:end+1])

if __name__ == '__main__':
    arr = [-2, 1, 2, 3, -2, 5]
    print(findSubArray(arr))
    findSubArrayElements(arr)
