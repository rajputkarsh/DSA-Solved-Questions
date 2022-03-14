
def isRotation(str1, str2):
    return str2 in str1+str1
    return 1 if str2 in str1+str1 else 0

if __name__ == '__main__':
    str1 = "ABCD"
    str2 = "CDAB"

    print(isRotation(str1, str2))