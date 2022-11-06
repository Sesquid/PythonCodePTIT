class Gamer:
    def __init__(self, id , name, time):
        self.id = id
        self.name = name
        self.time = time
        self.timeString = "{} gio {} phut".format(time // 60, time % 60)
    def __str__(self):
        return self.id + " " + self.name + " " + self.timeString

gamers = []
n = int(input())
for i in range(n):
    id = input()
    name = input()
    st = input()
    en = input()
    time =(int(en[:2]) * 60 + int(en[-2:])) - (int(st[:2]) * 60 + int(st[-2:]))
    gamers.append(Gamer(id, name, time))
gamers = sorted(gamers, key=lambda x: (-x.time))
for i in gamers:
    print(i)

