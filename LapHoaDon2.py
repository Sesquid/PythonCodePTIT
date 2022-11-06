import re
from datetime import date
class RentedRoom:
    NUM_CUS = 1
    def __init__(self, name, room, totalDays, totalFee):
        self.id = "KH" + '{:02d}'.format(RentedRoom.NUM_CUS)
        RentedRoom.NUM_CUS += 1
        self.name = name
        self.room = room
        self.totalDays = totalDays
        self.totalFee = totalFee
    def __str__(self):
        return self.id + " " + self.name + " " + self.room + " " + str(self.totalDays) + " " + str(self.totalFee)

a = list()
n = int(input())
for i in range(n):
    name = input()
    room = input()
    dayCome = re.split("/", input())
    dayLeft = re.split("/", input())
    totalDays = 1 + (date(int(dayLeft[2]), int(dayLeft[1]),
                         int(dayLeft[0])) - date(int(dayCome[2]), int(dayCome[1]), int(dayCome[0]))).days
    serviceFee = int(input())
    totalFee = serviceFee + totalDays * (25 if int(room[0]) == 1 else (
        34 if int(room[0]) == 2 else 50 if int(room[0]) == 3 else 80
    ))
    a.append(RentedRoom(name, room, totalDays, totalFee))
a = sorted(a, key=lambda x: (-x.totalFee))
for i in a:
    print(i)
