import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, b):
        return math.sqrt((self.x - b.x) * (self.x - b.x) + (self.y - b.y) * (self.y - b.y))


class Triangle:
    def __init__(self, a) -> None:
        self.p1 = Point(a[0], a[1])
        self.p2 = Point(a[2], a[3])
        self.p3 = Point(a[4], a[5])

    def is_valid(self):
        check = (self.p1.x * (self.p2.y - self.p3.y)
                 + self.p2.x * (self.p3.y - self.p1.y)
                 + self.p3.x * (self.p1.y - self.p2.y))

        return False if check == 0 else True

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        return '{:.2f}'.format(0.25 * math.sqrt((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b)))


n = int(input())
a = []
while True:
    try:
        a += [float(i) for i in input().split()]
    except:
        break
for i in range(n):
    tri = Triangle(a[i * 6: i * 6 + 6])
    print("INVALID" if not tri.is_valid() else tri.area())
