import math

ptu, pmau, qtu, qmau = map(int, input().split())
tu = ptu * qmau + qtu * pmau
mau = pmau * qmau
g = math.gcd(tu, mau)
tu //= g
mau //= g
print('{}/{}'.format(tu, mau))