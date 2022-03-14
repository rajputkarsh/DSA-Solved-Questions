


def find_smallest_index(arr):
    smallest = 0

    for i in range(1, len(arr)):
        if arr[smallest] > arr[i]:
            smallest = i

    print("Smallest in {0} is {1}".format(arr, arr[smallest]))

    return smallest

def count_inversions(arr):
    count = 0
    for i in range(len(arr)-2):
        smaller_than_i = find_smallest_index(arr[i+1::])+i+1
        print("Pair - ({0}, {1}) and indices-{2}, {3} ".format(arr[i], arr[smaller_than_i], i, smaller_than_i))
        if arr[i] > arr[smaller_than_i]:
            arr[i], arr[smaller_than_i] = arr[smaller_than_i], arr[i]
            count += 1
        else:
            print("Breaking loop as {0} > {1}".format(arr[i], arr[smaller_than_i]))
            break
        print(arr)
        print()

    print("Count = ",count)


array = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]
count_inversions(array)
