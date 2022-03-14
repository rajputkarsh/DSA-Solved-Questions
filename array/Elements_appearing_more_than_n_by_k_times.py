def findElements(array, n, k):

    frequency = dict()
    freq = int(n/k)

    for element in array:
        if frequency.get(element) is not None:
            frequency[element] += 1
        else:
            frequency[element] = 0

    elements = []
    for key in frequency.keys():
        if frequency[key] >= freq:
            elements.append(key)

    return elements

if __name__ == '__main__':
    array = [3, 1, 2, 2, 1, 2, 3, 3]
    k = 4
    print(findElements(array, len(array), k))
