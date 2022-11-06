class ThiSinh:
    def input(self):
        self.name = input()
        self.date = input()
        self.d1 = float(input())
        self.d2 = float(input())
        self.d3 = float(input())
        self.total = self.d1 + self.d2 + self.d3
    def __str__(self):
        return self.name + " " + self.date + " " + '{:.1f}'.format(self.total)
thisinh = ThiSinh()
thisinh.input()
print(thisinh)
