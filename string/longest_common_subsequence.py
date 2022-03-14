def findCommon(x, y, s1, s2):
    if x == 0 or y == 0:
        return 0

    print("'"+s1+"'", "'"+s2+"'")
    ans = 0

    if s1[-1] == s2[-1]:
        ans = ans + findCommon(x-1, y-1, s1[0:-1], s2[0:-1]) + 1
    else:
        ans = max(findCommon(x-1, y, s1[0:-1], s2),
                  findCommon(x, y-1, s1, s2[0:-1]))

    return ans


def findCommonDP(x, y, s1, s2, foundOnes):
    print("'"+s1+"'", "'"+s2+"'")
    if x == 0 or y == 0:
        return 0

    ans = 0

    if s1[-1] == s2[-1]:

        newAns = 0
        if foundOnes.get(s1+"-"+s2) is not None:
            newAns = foundOnes[s1[0:-1]+"-"+s2[0:-1]]
        else:
            if foundOnes.get(s2+"-"+s1) is not None:
                newAns = foundOnes[s2[0:-1]+"-"+s1][0:-1]
            else:
                newAns = findCommonDP(x-1, y-1, s1[0:-1], s2[0:-1], foundOnes)

        ans = ans + newAns + 1
    else:
        ans1 = foundOnes[s1[0:-1]+"-"+s2] if foundOnes.get(s1[0:-1]+"-" +
                                                           s2) is not None else findCommonDP(x-1, y, s1[0:-1], s2, foundOnes)
        ans2 = foundOnes[s1+"-"+s2[0:-1]] if foundOnes.get(s1+"-" +
                                                           s2[0:-1]) is not None else findCommonDP(x-1, y, s1, s2[0:-1], foundOnes)

        ans = max(ans1, ans2)


    foundOnes[s1+"-"+s2] = ans
    return ans

if __name__ == '__main__':
    s1 = "ABCDGH"
    s2 = "AEDFHR"

    arr = {}

    print(findCommon(len(s1), len(s2), s1, s2))
