chan = list()
le = list()
n = int(input())
pos = []
while True :
    x = [int(x) for x in input().split()]
    pos += x
    if len(pos) == n : break

for i in range(n):
    tmp = pos[i]
    if tmp % 2 != 0:
        le.append(tmp)
        pos[i] = 0
    else:
        chan.append(tmp)
        pos[i] = 1
cid = 0
lid = 0
chan.sort()
le = sorted(le, key=lambda x: (-x))
for i in pos:
    if i == 0:
        print(le[lid], end=' ')
        lid += 1
    else:
        print(chan[cid], end=' ')
        cid += 1
