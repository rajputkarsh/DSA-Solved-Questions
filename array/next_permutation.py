
def next_permutation(arr):
    # https://www.youtube.com/watch?v=LuLCLgMElus
    if arr == None or len(arr) <= 1:
        return -1

    i = len(arr) - 2

    print("before Swapping", arr)

    while i>=0 and arr[i] >= arr[i+1]:
        i -= 1

    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1

        print("I = ", i, " and val = ", arr[i])
        print("J = ", j, " and val = ", arr[j])


        arr[i], arr[j] = arr[j], arr[i]


    print("After Swapping - ", arr)

    rev = arr[i+1::]
    return arr[:i+1:] + rev[::-1]



array = [1,4,2,3,5]

print(next_permutation(array))

# for element in next_permutation(array):
#     print(element)