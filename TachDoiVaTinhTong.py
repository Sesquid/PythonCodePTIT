def cal(s):
    n = len(s)
    s1, s2 = "", ""
    s1 = s[:n // 2]
    s2 = s[n // 2:]
    s = int(s1) + int(s2)
    return str(s)
s = input()
while len(s) > 1:
    s = cal(s)
    print(s)
