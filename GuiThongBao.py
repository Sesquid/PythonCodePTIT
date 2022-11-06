t = int(input())
for i in range(t):
    s = input()
    if len(s) <= 100: print(s)
    else:
        list = s.split()
        s = ""
        for i in list:
            if len(s + i + " ") <= 100:
                s += i + " "
            else: break
        print(s)