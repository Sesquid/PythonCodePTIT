t = int(input())
while t > 0:
    t -= 1
    n = input()
    print("YES" if n[0] == n[-2] and n[1] == n[-1] else "NO")