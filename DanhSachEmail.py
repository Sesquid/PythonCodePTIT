f = open("CONTACT.in", "r")
a = set()
for x in f:
    a.add(x.lower())
a = list(a)
a.sort()
for i in a:
    print(i)