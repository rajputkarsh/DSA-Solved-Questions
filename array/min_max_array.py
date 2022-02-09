def findMinMax(listArr):
    if len(listArr) == 0:
        return None, None

    if len(listArr) == 1:
        return listArr[0], listArr[0]

    min = listArr[0]
    max = listArr[0]

    for element in listArr:
        if element > max:
            max = element

        if element < min:
            min = element
    
    return min, max


if __name__ == '__main__':
    print(findMinMax([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(findMinMax([1, 2, 3, 4, 5, 6, 7, 8, 9][::-1]))
