import re


class CaThi:
    NUM_CATHI = 0
    def __init__(self, date, time, room):
        CaThi.NUM_CATHI += 1
        self.id = "C" + '{:03d}'.format(CaThi.NUM_CATHI)
        self.date = date
        self.time = time
        self.room = room
        tmpdate = list(re.split("/", date))
        tmpdate.reverse()
        self.tmpdate = ''.join(tmpdate)
        tmpTime = list(re.split(":", time))
        self.tmpTime = int(tmpTime[0]) * 60 + int(tmpTime[1])
    def __str__(self):
        return self.id + " " + self.date + " " + self.time + " " + self.room

a = list()
f = open("CATHI.in", "r")
t = int(f.readline())
for i in range(t):
    date = f.readline()
    date = date[:len(date) - 1]
    time = f.readline()
    time = time[:len(time) - 1]
    room = f.readline()
    # room = room[:len(room) - 1]
    a.append(CaThi(date, time, room))
a = sorted(a, key=lambda x: (x.tmpdate, x.tmpTime, x.id))
for i in a:
    print(i, end='')