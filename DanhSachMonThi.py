n = int(input())
a = list()
for i in range(n):
    s = ""
    s += input() + " " + input() + " " + input()
    a.append(s)
a.sort()
for i in a:
    print(i)
    