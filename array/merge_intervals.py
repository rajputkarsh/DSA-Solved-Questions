def mergeIntervals(array, n):

    if n < 2:
        return array

    array.sort(key=lambda interval: interval[0])
    print(array)

    intervals = []
    intervals.append(array[0])

    for i in range(1, n):
        if array[i][0] <= intervals[-1][1]:
            intervals[-1][1] = array[i][1] if array[i][1] > intervals[-1][1] else intervals[-1][1]
        else:
            intervals.append(array[i])


    return intervals


if __name__ == '__main__':
    array = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(mergeIntervals(array, len(array)))


