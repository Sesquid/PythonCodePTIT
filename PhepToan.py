
def BT(a, i, sum, res, m):
    if i >= len(a): return
    if sum == m:
        print(res)
    # elif sum < m and m > 0 or sum > m and m < 0:
    BT(a, i + 1, sum + a[i], res + "+" + str(a[i]), m)
    BT(a, i + 1, sum - a[i], res + "-" + str(a[i]), m)
    BT(a, i + 1, sum * a[i], res + "*" + str(a[i]), m)

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
BT(a, 1, a[0], str(a[0]), m)