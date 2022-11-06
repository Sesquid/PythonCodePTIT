f = open("CATHI.in", "r")
a = []
b = []
for x in f:
    a += [i for i in x.split()]
for i in a:
    try:
        tmp = int(i)
        if tmp < -2147483648 or tmp > 2147483647:
            b.append(str(tmp))
    except:
        b += [i]
b.sort()
for i in b:
    print(i, end=' ')