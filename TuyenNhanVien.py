class Applicant:
    NUM_APP = 0
    def __init__(self, name, point):
        Applicant.NUM_APP += 1
        self.name = name
        self.point = point
        self.id = "TS0" + '{}'.format(Applicant.NUM_APP)
        self.rank = "XUAT SAC" if self.point > 9.5 else(
            "DAT" if 8 <= self.point <= 9.5 else(
                "CAN NHAC" if 5 <= self.point < 8 else "TRUOT"
            )
        )
    def __str__(self):
        return self.id + " " + self.name + " " + "{:.2f}".format(self.point) + " " + self.rank

applicants = []
t = int(input())
for i in range(t):
    name = input()
    lt = float(input())
    if lt > 10: lt /= 10
    th = float(input())
    if th > 10: th /= 10
    point = (th + lt) / 2
    applicants.append(Applicant(name, point))
applicants = sorted(applicants, key=lambda x: (-x.point))
for i in applicants:
    print(i)

