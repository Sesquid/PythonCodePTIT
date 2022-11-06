n = int(input())
a = list()

while len(a) < n:
    s = input()
    a.append(s)
    if len(a) == 1 or a[-2] == "":
        cnt = 0
        print(s + ": ", end='')
        while len(a) < n:
            s = input()
            a.append(s)
            if s == "": break
            cnt += 1
        print(cnt)
# print(a)
