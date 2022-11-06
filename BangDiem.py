from decimal import Decimal, ROUND_HALF_UP

class student:
    NUM_STU = 0
    def __init__(self, name, mark):
        student.NUM_STU += 1
        self.id = "HS" + '{:02d}'.format(student.NUM_STU)
        self.name = name
        self.mark = mark.quantize(Decimal('0.1'), ROUND_HALF_UP)
        self.rank = "XUAT SAC" if mark >= 9 else (
            "GIOI" if 8 <= mark <= 8.9 else (
                "KHA" if 7 <= mark <= 7.9 else (
                    "TB" if 5 <= mark <= 6.9 else "YEU"
                )
            )
        )
    def __str__(self):
        return self.id + " " + self.name + " " + '{:.1f}'.format(self.mark) + " " + self.rank

stus = list()
t = int(input())
for i in range(t):
    name = input()
    a = [Decimal(x) for x in input().split()]
    mark = a[0] + a[1] + Decimal(sum(a))
    mark /= 12

    stus.append(student(name, mark))
stus = sorted(stus, key = lambda x : (-x.mark, x.id))
for i in stus:
    print(i)

