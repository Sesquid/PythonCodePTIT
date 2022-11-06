import re

tab = [[10, 12, 14, 20],
       [10, 11, 13, 16],
       [9, 10, 12, 14],
       [8, 9, 11, 13]]

class NV:
    def __init__(self, id, name, room, salary):
        self.salary = salary
        self.room = room
        self.name = name
        self.id = id
    def __str__(self):
        return self.id + " " + self.name + " " + self.room + " " + str(self.salary)
pBan = {}
l = list()
n = int(input())
for i in range(n):
    x = re.split("\s", input(), maxsplit = 1)
    pBan[x[0]] = x[1]
n = int(input())
for i in range(n):
    id = input()
    name = input()
    room = pBan[id[-2:]]
    bSalary = int(input())
    dayOn = int(input())
    x = int(id[1 : 3])
    salary = 1000 * dayOn * bSalary * (tab[ord(id[0]) - ord('A')][0 if 1 <= x <= 3 else 1 if 4 <= x <= 8 else 2 if 9 <= x <= 15 else 3])
    l.append(NV(id, name, room, salary))
for i in l:
    print(i)