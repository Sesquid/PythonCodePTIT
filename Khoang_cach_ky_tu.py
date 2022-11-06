t = int(input())
for i in range (t):
    s = input()
    r = s
    r = list(r)
    r.reverse()
    r = ''.join(r)
    flag = 1
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(r[i]) - ord(r[i + 1])):
            flag = 0
            break
    print("YES" if flag == 1 else "NO")