t = int(input())
a = {}
for i in range(t):
    name = input()
    stString = input()
    enString = input()
    amount = float(input())
    time = int(enString[:2]) * 60 + int(enString[-2:]) - int(stString[:2]) * 60 - int(stString[-2:])

    if name in a:
        a[name][0] += time
        a[name][1] += amount
    else:
        a[name] = [0] * 2
        a[name][0] = time
        a[name][1] = amount

i = 1
for j in a:
    print('T0{} {} {:.2f}'.format(i, j, a[j][1] * 60 / a[j][0]))
    i += 1
