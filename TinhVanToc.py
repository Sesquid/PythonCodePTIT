import re
from datetime import datetime
class Athlete:
    def __init__(self, name, unit, finishTime):
        tmp = re.split(":", finishTime)
        t = int(tmp[0]) * 60 + int(tmp[1]) - 360
        self.finishTime = t
        tmp = (unit + " " + name).upper().split()
        self.id = ""
        for i in tmp:
            self.id += i[0]
        self.name = name
        self.unit = unit
        t /= 60
        self.velo = round(120 / t)
    def __str__(self):
        return self.id + " " + self.name + " " + self.unit + " " + str(self.velo) + " Km/h"

a = list()
n = int(input())
for i in range(n):
    name = input()
    unit = input()
    finishTime = input()
    a.append(Athlete(name, unit, finishTime))
a = sorted(a, key=lambda x: (x.finishTime))
for i in a:
    print(i)

