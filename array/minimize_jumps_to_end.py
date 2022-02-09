
def minimizeJumps(arr, l, h):

    if (h == l):
        return 0
 

    if (arr[l] == 0):
        return float('inf')
 
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minimizeJumps(arr, i, h)
            if (jumps != float('inf') and
                       jumps + 1 < min):
                min = jumps + 1
 
    return min


if __name__ == '__main__':
    arr = [70, 21, 46, 25, 54, 76, 92, 84, 47, 57, 46, 31, 38, 31, 75, 40, 61, 21, 84, 51, 86, 41]
    print(minimizeJumps(arr, 0, len(arr)-1))
