def countAndSay(string, n):

    if len(string) < 1:
        return ""

    ans = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            ans = ans + str(count) + str(string[i-1])
            count = 1

    ans = ans + str(count) + str(string[-1])

    if n == 1:
        return ans
    else:
        return countAndSay(ans, n-1)

if __name__ == '__main__':
    string = "1211"
    n = 4
    print(countAndSay(string, n))