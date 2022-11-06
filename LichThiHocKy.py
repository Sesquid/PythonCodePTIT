mon = {}
l = list()
class CaThi:
    NUM_CA = 0

    def __init__(self, idMon, date, time, group):
        CaThi.NUM_CA += 1
        self.idMon = idMon
        self.id = "T" + '{:03d}'.format(self.NUM_CA)
        self.group = group
        self.name = mon[idMon]
        self.time = time
        self.date = date
        self.idMon = idMon
        revDate = self.date.split('/')
        revDate.reverse()
        self.revDate = ''.join(revDate)
        minTime = self.time.split(":")
        self.minTime = int(minTime[0]) * 60 + int(minTime[1])
    def __str__(self):
        return self.id + " " + self.idMon + " " + self.name + " " + self.date + " " + self.time + " " + self.group

nMon, nCa = map(int, input().split())
for i in range(nMon):
    idMon = input()
    mon[idMon] = input()
# for i in mon:
#     print(i)
for i in range(nCa):
    s = input().split()
    l.append(CaThi(s[0], s[1], s[2], s[3]))
l = sorted(l, key=lambda x: (x.revDate, x.minTime, x.idMon))
for i in l:
    print(i)



