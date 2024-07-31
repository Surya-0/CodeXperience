def find_char(str1, str2):
    p1 = 0
    p2 = 0
    res = 0
    for char in str1:
        res = res ^ ord(char)

    for char in str2:
        res = res ^ ord(char)

    return chr(res)


s1 = "hello"
s2 = "hleo"
print(find_char(s1, s2))
