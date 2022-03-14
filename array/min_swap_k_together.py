def findSwaps(arr, n, k):
    # sliding window approach

    window_size = 0
    bad_elements_in_window = n
    bad_elements_in_initial_window = 0
    window_start = 0

    for element in arr:
        if element <= k:
            window_size += 1

    print("window size = ", window_size)

    for i in range(window_size):
        if arr[i] > k:
            bad_elements_in_initial_window += 1

    print("bad elements in first window = ", bad_elements_in_initial_window)

    for i in range(window_size, len(arr)):



    return bad_elements_in_window

    
# print(findSwaps([19, 9], 5, 18))

print(findSwaps([2, 1, 5, 6, 3], 5, 3))
