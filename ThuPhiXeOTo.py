
def getFee(numOfSeats):
    return 10000 if numOfSeats == 5 else(
        15000 if numOfSeats == 7 else(
            20000 if numOfSeats == 2 else(
                50000 if numOfSeats == 29 else 70000
            )
        )
    )

res = {}
n = int(input())
for i in range(n):
    a = list(input().split())
    status = a[3]
    if status == 'IN':
        numOfSeats = int(a[2])
        # print(getFee(numOfSeats))
        day = a[4]
        if day in res:
            res[day] += getFee(numOfSeats)
        else: res[day] = getFee(numOfSeats)
for i in res:
    print('{}: {}'.format(i, res[i]))