from array import array


def findCommon(array1, array2, array3, n1, n2, n3):

    x, y, z = 0, 0, 0
    common = []

    while x < n1 and y < n2 and z < n3:
        if array1[x] == array2[y] and array1[x] == array3[z]:
            if array1[x] not in common:
                common.append(array1[x])
            x += 1
            y += 1
            z += 1
        elif array1[x] < array2[y]:
            x += 1
        elif array2[y] < array3[z]:
            y += 1
        else:
            z += 1
        
    return common

if __name__ == '__main__':
    array1 = [1, 5, 10, 20, 40, 80]
    array2 = [6, 7, 20, 80, 100]
    array3 = [3, 4, 15, 20, 30, 70, 80, 120]

    print(findCommon(array1, array2, array3, len(array1), len(array2), len(array3)))
