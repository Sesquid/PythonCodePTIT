def check(n):
    for i in range (0, len(n)):
        if n[i] != '4' and n[i] != '7':
            return False
    return True

t = int(input())
while t > 0:
    t -= 1
    n = input()
    print("YES" if check(n) else "NO")
    