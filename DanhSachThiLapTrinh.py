import re


class Team:
    NUM_ID = 0

    def __init__(self, name, teamName, uni):
        Team.NUM_ID += 1
        self.id = "C" + '{:.3d}'.format(Team.NUM_ID)
        self.name = name
        self.teamName = teamName
        self.uni = uni

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.teamName, self.uni)

uName = {}
n = int(input())
for i in range(n):
    tName = input()
    x = re.split("[^\w]+")
    uName[x[0]] = input()
n = int(input())
for i in range(n):
    name = input()