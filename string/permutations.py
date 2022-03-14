def permute(string, answer):
    if len(string) == 0:
        print(answer)
        return

    for i in range(len(string)):
        current         = string[i]
        left_substring  = string[0:i]
        right_substring = string[i+1:]

        permute(left_substring+right_substring, answer+current)


answer = ""
string = input()

permute(string, answer)

