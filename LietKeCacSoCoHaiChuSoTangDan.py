s = input()
a = set()
for i in range(0, len(s), 2):
    tmp = s[i:i + 2]
    if len(tmp) == 2:
        a.add(tmp)
a = sorted(list(a))
for i in a:
    print(i, end=' ')