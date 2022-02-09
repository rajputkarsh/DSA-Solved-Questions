
def move(arr):
    divider  = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[divider], arr[i] = arr[i], arr[divider]
            divider += 1
        print(arr)
    return arr


if __name__ == '__main__':
    print(move([5, -12, 11, -13, -5, 6, -7, 5, -3, -6]))
