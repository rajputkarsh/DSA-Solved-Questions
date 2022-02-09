
def minimizeHeights(arr, k):
    avg_height = sum(arr)/len(arr)
    print(avg_height)

    for i in range(len(arr)):
        
        if arr[i] < avg_height and abs(avg_height - arr[i]) > abs(arr[i]+k - avg_height):
            arr[i] += k
            print("\tAdding at", i)
        elif arr[i] > avg_height and abs(arr[i] - avg_height) > abs(avg_height - arr[i]-k):
            arr[i] -= k
            print("\tSubtracting at", i)
        else:
            print("\tDoing Nothing i={0}, arr[i]={1}, avg_height={2}".format(i, arr[i], avg_height))
    print()
    print(arr)

    return (max(arr) - min(arr))

if __name__ == '__main__':
    arr = [5, 5, 8, 6, 4, 10, 3, 8, 9, 10]
    print(minimizeHeights(arr, 5))
