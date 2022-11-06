import math

tu, mau = map(int, input().split())
g = math.gcd(tu, mau)
tu //= g
mau //= g
print('{}/{}'.format(tu, mau))