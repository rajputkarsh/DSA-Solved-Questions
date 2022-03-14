
def minimizeHeights(arr, k):

    print("checking")
    # solution 1 - produces differences between absolute shortest and absolute longest towers

    # avgHeight = sum(arr)/len(arr)

    # print(arr)
    # print(avgHeight)

    # for i in range(len(arr)):
        
    #     if arr[i] > avgHeight:
    #         # tower is taller than average, now check if subtracting height makes it closer to average
    #         if abs(arr[i] - k - avgHeight) <= abs(arr[i] - avgHeight):
    #             # after reducing tower's height, it is closer to average. Thus, reduce height
    #             arr[i] -= k

    #     elif arr[i] < avgHeight:
    #         # tower is smaller than average, now check if adding heigh makes it closer to average
    #         if abs(arr[i] + k - avgHeight) <= abs(arr[i] - avgHeight):
    #             arr[i] += k

    # print(arr)
    # print()

    # return (max(arr) - min(arr))

    # solution 2 - produces minimized difference

    # https://www.youtube.com/watch?v=29uyA4F9t5I

    arr.sort()
    # sort the array so as to make optimal pairs
    
    n = len(arr)

    ans = arr[n-1] - arr[0]
    min_height = 0
    max_height = 0

    for i in range(1, len(arr)):

        if arr[i] >= k:

            max_height = max(arr[i-1]+k, arr[n-1]-k)
            min_height = min(arr[i]-k, arr[0]+k)
            ans = min(ans, max_height-min_height)

        else:
            continue

    return ans


if __name__ == '__main__':
    arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
    print(minimizeHeights(arr, 3))
