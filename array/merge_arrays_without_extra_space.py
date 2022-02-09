def merge_arrays(arr1, arr2):
    
    ptr = 0

    # edit the smaller array
    if len(arr1) < len(arr2):
        for i in range(len(arr1)):
            if arr1[i] > arr2[ptr]:
                # swap
                arr1[i] = arr1[i] + arr2[ptr]
                arr2[ptr] = arr1[i] - arr2[ptr]
                arr1[i] = arr1[i] - arr2[ptr]
            else:
                ptr += 1

        print(arr1, end=" ")
        print(arr2)
        
    else:
        for i in range(len(arr2)):
            if arr2[i] > arr1[ptr]:
                # swap
                arr1[ptr] = arr1[ptr] + arr2[i]
                arr2[i] = arr1[ptr] - arr2[i]
                arr1[ptr] = arr1[ptr] - arr2[i]
            else:
                ptr += 1

        print(arr2, end=" ")
        print(arr1)

merge_arrays([1, 3, 5, 7], [0, 2, 6, 8, 9])
