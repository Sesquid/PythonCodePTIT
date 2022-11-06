a = open("DATA1.in", "r")
b = open("DATA2.in", "r")
x = []
y = []
for i in a:
    x += [x.lower() for x in i.split()]
for i in b:
    y += [x.lower() for x in i.split()]

res = set(x).difference(set(y))
y = set(y).difference(set(x))

x = sorted(list(res))
y = sorted(list(y))
for i in x:
    print(i, end=' ')
print()
for i in y:
    print(i, end=' ')
