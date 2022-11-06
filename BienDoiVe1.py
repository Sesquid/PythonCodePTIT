while True:
    s = set()
    x = int(input())
    if x == 0: break;
    s.add(x)
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else: x = x * 3 + 1
        s.add(x)
    print(len(s))