s = ""
test = 10
while test > 0:
    tmp = input()
    l = len(tmp.split())
    s = s + tmp + " "
    test -= l
a = list(map(int, s.split()))
for i in range(len(a)):
    a[i] = a[i] % 42
    
a = set(a)
print(len(a))
