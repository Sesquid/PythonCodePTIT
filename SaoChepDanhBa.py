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


l = list()
with open("SOTAY.txt") as f:
    x = " "
    day = ""
    phone = ""
    name = ""
    while True:
        try:
            x = f.readline().strip()
            if x[:4] == "Ngay":
                day = x.split()[1]
            elif not x[0].isdigit():
                name = x
            else:
                phone = x
                l.append(Person(name, phone, day))
        except:
            break
        
l = sorted(l, key=lambda x: (x.getName(), x.name))

open("DIENTHOAI.txt", "w").writelines('\n'.join([i.__str__() for i in l]))
