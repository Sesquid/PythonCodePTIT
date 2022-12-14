l = list()
n = int(input())
for i in range(n):
    name = input()
    attach = input()
    status = input()
    l.append([name, attach, status])
l = sorted(l, key=lambda x: x[0])
res = list()
for i in l:
    if i[2] == "Turned in late" and (i[1].isdigit() or i[1][:2] != "No"):
        res.append(i[0].replace(" - ", "-").split("-")[0])
print(len(res))
for i in res:
    print(i)