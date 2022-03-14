
def minimizeJumps(arr, l, h):

    # https://www.youtube.com/watch?v=5Du2iSRrbEw

    maxReachable = arr[0]
    step = arr[0]
    jump = 1

    if len(arr) == 1: 
        return 0
    elif len(arr) == 0:
        return -1
    else:
        for i in range(1, len(arr)):
            
            if i == len(arr) - 1:
                return jump

            maxReachable = max(maxReachable, i + arr[i])
            step -= 1

            if step == 0:
                jump += 1
                
                if i >= maxReachable:
                    return -1
                
                step = maxReachable - i

    return jump


if __name__ == '__main__':
    arr = [70, 21, 46, 25, 54, 76, 92, 84, 47, 57, 46, 31, 38, 31, 75, 40, 61, 21, 84, 51, 86, 41]
    print(minimizeJumps(arr, 0, len(arr)-1))
