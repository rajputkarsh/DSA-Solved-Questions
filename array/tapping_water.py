def collectWater(arr):
    
    waterCollected = 0

    left  = [0]*len(arr)
    right = [0]*len(arr)

    maxLeft  = arr[0]
    maxRight = arr[-1]


    for i in range(len(arr)):
        if arr[i] > maxLeft:
            maxLeft = arr[i]

        left[i] = maxLeft

    for i in range(len(arr)-1, -1, -1):
        if arr[i] > maxRight:
            maxRight = arr[i]

        right[i] = maxRight


    for i in range(len(arr)):
        smaller = left[i] if left[i] < right[i] else right[i]
        water = smaller - arr[i] if smaller - arr[i] > 0 else 0
        waterCollected += water

    return waterCollected

            
    


array = [1, 1, 5, 2, 7, 6, 1, 4, 2, 3]

print(collectWater(array))