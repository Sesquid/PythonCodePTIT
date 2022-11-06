import functools


class student:
    def __init__(self, name, ACcnt, submitTime):
        self.name = name
        self.ACcnt = ACcnt
        self.submitTime = submitTime
    def __str__(self):
        return self.name + " " + str(self.ACcnt) + " " + str(self.submitTime)

def cmp(a, b):
    if a.ACcnt == b.ACcnt:
        return a.submitTime - b.submitTime
    return b.ACcnt - a.ACcnt
l = list()
t = int(input())

for i in range(t):
    name = input()
    ACcnt, submitTime = map(int, input().split())
    l.append(student(name, ACcnt, submitTime))
    l = sorted(l, key = functools.cmp_to_key(cmp))
for i in l:
    print(i)

