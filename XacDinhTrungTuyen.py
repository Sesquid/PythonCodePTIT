class Teacher:
    NUM_TEACHER = 0
    def __init__(self, name, mark, major):
        Teacher.NUM_TEACHER += 1
        self.major = major
        self.id = "GV" + '{:02d}'.format(Teacher.NUM_TEACHER)
        self.name = name
        self.rank = "TRUNG TUYEN" if mark >= 18 else "LOAI"
        self.mark = mark
    def __str__(self):
        return self.id + " " + self.name + " " + self.major + " " + '{:.1f}'.format(self.mark) + " " + self.rank

a = list()
n = int(input())
for i in range(n):
    name = input()
    major = input()
    itMark = float(input())
    majorMark = float(input())
    mark = itMark * 2 + majorMark + (2 if major[1] == '1' else
                                     1.5 if major[1] == '2' else
                                     1 if major[1] == '3' else 0)
    major = ("TOAN" if major[0] == 'A'
             else "LY" if major[0] == 'B'
             else "HOA")
    a.append(Teacher(name, mark, major))
a = sorted(a, key=lambda x: (-x.mark))
for i in a:
    print(i)