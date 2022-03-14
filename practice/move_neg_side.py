from operator import le


def move(arr):
    ptr = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1

    print(arr)

array = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
move(array)
