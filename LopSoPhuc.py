t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    a = complex(a, b)
    b = complex(c, d)
    c = (a + b) * a
    d = (a + b) ** 2
    print("{} + {}i, {} + {}i".format(int(c.real), int(c.imag), int(d.real), int(d.imag)))
