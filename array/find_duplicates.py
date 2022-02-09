def find_duplicate(nums):

    for i in range(len(nums)):

        if nums[abs(nums[i])] > 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            return abs(nums[i])

    return -1

    ### Below given solution does not cover case [2, 2, 2, 2, 2]

    # total_sum = sum(x for x in range(1, len(arr)))

    # for num in arr:
    #     total_sum -= num
    
    # return -total_sum

if __name__ == '__main__':
    print(find_duplicate([1,3,4,2,2]))