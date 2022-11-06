s1 = input()
s2 = input()
ind = int(input())
ind -= 1
res = s1[:ind] + s2 + s1[ind:]
print(res)