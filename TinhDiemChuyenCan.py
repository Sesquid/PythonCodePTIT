class Student:
    def __init__(self, id, name, className):
        self.id = id
        self.name = name
        self.className = className
        self.note = ""
    def setMark(self, mark):
        self.mark = mark
        self.note = "KDDK" if self.mark == 0 else ""
    def getId(self):
        return self.id
    def __str__(self):
        return self.id + " " + self.name + " " + self.className + " " + str(self.mark) + " " + self.note

a = list()
n = int(input())
for i in range(n):
    id = input()
    name = input()
    className = input()
    a.append(Student(id, name, className))
for i in range(n):
    s = input().split()
    mark = s[1]
    res = 10
    for i in mark:
        res = res - 2 if i == 'v' else(
            res - 1 if i == 'm' else res
        )
    res = max(res, 0)
    for j in a:
        if j.getId() == s[0]:
            j.setMark(res)
for j in a:
    print(j)





