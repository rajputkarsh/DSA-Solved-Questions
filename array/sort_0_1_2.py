
def sort_using_l_m_h(arr):

    # assume that 0 - low - 1 are 0, low to high - 1 are 1 and high to len(arr) - 1 are 2
    # mid will be used to determine the conditions for the loop 

    low  = 0
    mid  = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid]  == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr

def sort_by_counting(arr):
    #count the number of 0s, 1s and 2s and then create the array
    zeroes = 0
    ones   = 0
    twos   = 0
    
    i = 0
    
    for element in arr:
        if element == 0:
            zeroes += 1
        elif element == 1:
            ones += 1
        else:
            twos +=1

    for j in range(zeroes):
        arr[i] = 0
        i += 1

    for j in range(ones):
        arr[i] = 1
        i += 1

    for j in range(twos):
        arr[i] = 2
        i += 1

    return arr


if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

    print(sort_using_l_m_h(arr))
    print(sort_by_counting(arr))