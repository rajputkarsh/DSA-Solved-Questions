def findSubString(string, n):
    
    longest = ""
    for i in range(0, n):
        #  odd length
        l, r = i, i
        while l >= 0 and r < n and string[l] == string[r]:
            if r - l + 1 > len(longest):
                longest = string[l:r+1]
            r += 1
            l -= 1

        #  even length
        l, r = i, i+1
        while l >= 0 and r < n and string[l] == string[r]:
            if r - l + 1 > len(longest):
                longest = string[l:r+1]
            r += 1
            l -= 1

    return longest

if __name__ == '__main__':
    string = "xw"
    print(findSubString(string, len(string)))
