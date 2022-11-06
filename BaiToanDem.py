n = int(input())
a = []
app = [0] * 201
while len(a) < n:
    x = [int(i) for i in input().split()]
    a += x

for i in a:
    app[i] = 1
tmp = max(a)
flag = 1
for i in range(1, tmp):
    if app[i] == 0:
        flag = 0
        print(i)
if flag == 1:
    print("Excellent!")
