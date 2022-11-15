import functools


class Person:
    def __init__(self, name, phone, day):
        self.day = day
        self.phone = phone
        self.name = name

    def getName(self):
        return self.name.split()[-1]

    def __str__(self):
        return self.name + ": " + self.phone + " " + self.day


def cmp(a: Person, b: Person):
    if a.getName() == b.getName():
        if a.name < b.name: return -1
        return 1
    if a.getName() < b.getName(): return -1
    return 1

l = list()
with open("SOTAY.txt") as f:
    x = " "
    day = ""
    phone = ""
    name = ""
    while True:
        x = f.readline()
        if len(x) == 0: break
        if not x[0].isdigit() and x[5].isdigit():
            day = x[:-1].split()[1]
        else:
            if not x[0].isdigit(): name = x[:-1]
            else:
                if not x[-1].isdigit():
                    phone = x[:-1]
                else: phone = x
                l.append(Person(name, phone, day))
l = sorted(l, key=functools.cmp_to_key(cmp))
with open("DIENTHOAI.txt", "w") as k:
    for i in l:
        k.write(i.__str__())
        k.write("\n")


