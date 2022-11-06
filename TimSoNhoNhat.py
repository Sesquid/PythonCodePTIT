import re
t = int(input())
for i in range(t):
    tmp = input()
    tmp = 'z' + tmp + 'z'
    s = re.split("[a-zA-Z]+", tmp)
    res = 10 ** 20
    # print(s)
    for i in range (1, len(s) - 1):
        res = min(res, int(s[i]))
    print(res)