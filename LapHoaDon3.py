class Good:
    def __init__(self, id, name, number, price, discount):
        self.discount = discount
        self.price = price
        self.number = number
        self.name = name
        self.id = id
        self.total = price * number - discount

    def __str__(self):
        return self.id + " " + self.name + " " + str(self.number) + " " + str(self.price) + " " + str(self.discount) + " " + str(self.total)


a = list()
n = int(input())
for i in range(n):
    id = input()
    name = input()
    number = int(input())
    price = int(input())
    discount = int(input())
    a.append(Good(id, name, number, price, discount))
    # print(Good(id, name, number, price, discount))
a = sorted(a, key=lambda x: -x.total)
for i in a:
    print(i)
