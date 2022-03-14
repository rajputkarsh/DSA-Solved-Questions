
def count(s):
    # To store the count of 0s and 1s
    count0 = 0
    count1 = 0

    # To store the count of maximum
    # substrings str can be divided into
    cnt = 0

    for i in range(len(s)):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

        if count0 == count1:
            cnt += 1

    # It is not possible to
    # split the string
    if count0 != count1:
        return -1

    return cnt

string = "0100110101"
print(count(string))