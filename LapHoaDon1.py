class Customer:
    NUM_CUS = 0
    def __init__(self, name, total):
        Customer.NUM_CUS += 1
        self.name = name
        self.total = total
        self.id = "KH" + '{:02d}'.format(Customer.NUM_CUS)
        self.bill = 0
        tmp = self.total
        f = tmp - 100
        if f > 0:
            tmp = 100
            self.bill += f * 200
        s = tmp - 50
        if s > 0:
            self.bill += s * 150
            tmp = 50
        if tmp > 0:
            self.bill += tmp * 100
        extra = 0.05 if self.total > 100 else(
            0.03 if self.total > 51 else 0.02
        )
        self.bill += extra * self.bill
    def __str__(self):
        return self.id + ' ' + self.name + " " + str(round(self.bill))

n = int(input())
customers = []
for i in range(n):
    name = input()
    old = int(input())
    new = int(input())
    total = new - old
    customers.append(Customer(name, total))
    customers = sorted(customers, key= lambda x: (-x.bill))
for i in customers:
    print(i)
