import functools
import re

class Student:
    def __init__(self, date, time, roomID, subjectName, group, numOfStu, sID):
        self.date = date
        self.time = time
        self.roomID = roomID
        self.subjectName = subjectName
        self.group = group
        self.numOfStu = numOfStu
        revDate = list(re.split("/", self.date))
        revDate.reverse()
        self.revDate = ''.join(revDate)
        minTime = list(re.split(":", self.time))
        self.minTime = int(minTime[0]) * 60 + int(minTime[1])
        self.sID = sID
        # print(self.minTime, self.revDate)
    def __str__(self):
        return self.date + " " + self.time + " " + self.roomID + " " + self.subjectName + " " + self.group + " " + self.numOfStu

students = list()
m = open("MONTHI.in", "r")
l = open("LICHTHI.in", "r")
c = open("CATHI.in", "r")
t = int(m.readline()[:-1])
l.readline()
c.readline()
for i in range(t):
    date = c.readline()[:-1]
    time = c.readline()[:-1]
    roomID = c.readline()
    if roomID[-1] == '\n': roomID = roomID[:-1]
    m.readline()
    subjectName = m.readline()[:-1]
    m.readline()
    tmp = l.readline()
    if tmp[-1] == '\n': tmp = tmp[:-1]
    tmp = tmp.split()
    sID = tmp[0]
    group = tmp[2]
    numOfStu = tmp[-1]
    students.append(Student(date, time, roomID, subjectName, group, numOfStu, sID))
students = sorted(students, key = lambda x: (x.revDate, x.minTime, x.sID))
for i in students:
    print(i)