t = int(input())
for i in range(t):
    s = input()
    sum = 0
    for j in s:
        sum += int(j)
    if sum == int(str(sum)[::-1]) and sum >= 10:
        print("YES")
    else: print("NO")