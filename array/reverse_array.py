
def reverseArray(list_array):
    start = 0
    end = len(list_array) - 1

    while start < end:
        list_array[start], list_array[end] = list_array[end], list_array[start]
        start += 1
        end -= 1

    return list_array


if __name__ == '__main__':
    print(reverseArray([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(reverseArray([1, 2, 3, 4, 5, 6, 7, 8]))
