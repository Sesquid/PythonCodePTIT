def check(s):
    k = list(s)
    k.reverse()
    if s == ''.join(k):
        return True
    return False

f = open("VANBAN.in", "r")
a = []
for x in f:
    a += [i for i in x.split() if check(i)]
b = [len(i) for i in a]
d = {}
maxN = max(b)
for i in a:
    if len(i) == maxN:
        if i in d:
            d[i] += 1
        else: d[i] = 1
for i in d:
    print(i, d[i])