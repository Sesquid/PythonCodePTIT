import re

t = int(input())
for i in range(t):
    s = input()
    flag = 1
    ck = re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
    if not ck: flag = 0
    else:
        list = re.split('\.', s)
        for i in list:
            if int(i) > 255:
                flag = 0
                break
    print("YES" if flag == 1 else "NO")