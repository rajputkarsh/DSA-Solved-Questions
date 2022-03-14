def findThreeNums(arr, n , k):
    ans = 0

    arr.sort()

    for i in range(n-2):
        l = i+1
        r = n-1

        while l < r:
            if arr[i] + arr[l] + arr[r] == k:
                ans = 1
                break

            elif arr[i] + arr[l] + arr[r] < k:
                l += 1
            else:
                r -= 1

        if ans == 1:
            break

    return ans


array = [1, 4, 45, 6, 10, 8]
target = 13

print(findThreeNums(array, len(array), target))

