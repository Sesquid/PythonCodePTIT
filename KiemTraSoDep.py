t = int(input())
for i in range(t):
    s = input()
    r = set(s)
    a = set()
    b = set()
    if len(r) == 2:
        for i in range (len(s)):
            if i % 2 == 0: a.add(s[i])
            else: b.add(s[i])
        if len(a) == 1 and len(b) == 1:
            print("YES")
        else: print("NO")
    else: print("NO")