
class film:
    NUM_ID = 0
    def __init__(self, tl, date, name, epi):
        self.epi = epi
        self.name = name
        self.date = date
        self.tl = tl
        film.NUM_ID += 1
        self.id = "P" + '{:03d}'.format(self.NUM_ID)
        revDate = date.split("/")
        revDate.reverse()
        self.revDate = ''.join(revDate)
    def __str__(self):
        return self.id + " " + self.tl + " " + self.date + " " + self.name + " " + str(self.epi)


theloai = {}
l = list()
nTheLoai, nPhim = map(int, input().split())
for i in range(nTheLoai):
    theloai["TL" + '{:03d}'.format(i + 1)] = input()
for i in range(nPhim):
    tl = theloai[input()]
    date = input()
    name = input()
    epi = int(input())
    l.append(film(tl, date, name, epi))
l = sorted(l, key=lambda x: (x.revDate, x.name, -x.epi))
for i in l:
    print(i)