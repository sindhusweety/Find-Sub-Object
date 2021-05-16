"""
find a substring from a given string
"""
def check_sub(sub, substring):
    if len(sub) == 0 and len(substring) == 0:
        return True
    if sub[0] in substring:
        index = substring.index(sub[0])
        substring = substring[index + 1: ]
        sub = sub[1 : ]
        return check_sub(sub, substring)
    return False
def recursive(string_n, string, sub_n, sub):
    if sub_n == string_n:
        return sub
    for i in range(string_n - sub_n + 1):
        substring = string[i : i + sub_n]
        if check_sub(sub, substring):
            return substring
    return recursive(string_n, string, sub_n + 1, sub)

def solution(string, sub):
    return  recursive(len(string), string, len(sub), sub)

print(solution('fgfdsfaabacabcda', 'fabc'))
