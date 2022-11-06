import re

a = list()
n = int(input())
for i in range(n):
    s = input()
    s = re.split("\\D+", s)
    for i in s:
        try:
            x = int(i)
            a.append(x)
        except:
            a
a.sort()
for i in a:
    print(i)