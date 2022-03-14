def countPairs(array, n, k):
    pairs = 0
    number_freq = {}

    for i in range(n):
        if number_freq.get(array[i]) is not None:
            number_freq[array[i]] += 1
        else:
            number_freq[array[i]] = 1

    for i  in range(n):
        pairs = pairs + (number_freq.get(k-array[i]) if number_freq.get(k-array[i]) is not None else 0)

        if k - array[i] == array[i]:
            pairs -= 1

    return int(pairs/2)


if __name__ == '__main__':
    array = [1, 5, 7, 1]
    k = 6

    print(countPairs(array, len(array), k))
