def merge_arrays(arr1, arr2):

    m = len(arr1)
    n = len(arr2)

    for i in range(n-1, -1, -1):
         
        last = arr1[m-1]
        j=m-2
        while(j >= 0 and arr1[j] > arr2[i]):
            arr1[j+1] = arr1[j]
            j-=1
  
        # If there was a greater element
        if (j != m-2 or last > arr2[i]):
         
            arr1[j+1] = arr2[i]
            arr2[i] = last

    print(arr1)
    print(arr2)

merge_arrays([1, 3, 5, 7], [0, 2, 6, 8, 9])
