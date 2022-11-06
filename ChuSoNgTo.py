a = "2357"
l = list()
def sinh(s, n):
    if len(s) >= 4:
        if '2' in s and '3' in s and '5' in s and '7' in s:
            s = int(s)
            if s % 2 != 0:
                l.append(s)
            s = str(s)
    for i in a:
        if len(s) < n:
            sinh(s + i, n)
n = int(input())
sinh("", n)
l.sort()
for i in l:
    print(i)



