t = int(input())
for i in range(t):
    s = input()
    res = 0
    resS = ""
    for j in s:
        try:
            res += int(j)
        except:
            resS += j
    resS = list(resS)
    resS.sort()
    print(''.join(resS), res, sep='')