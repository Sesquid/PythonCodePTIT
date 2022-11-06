import math

primes = []
def SieveOfEratosthenes():
    num = 11000
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while (p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
            primes.append(p)
            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

SieveOfEratosthenes()
n = int(input())
a = list(map(int, input().split()))
res = -1
for i in a:
    tmpRes = math.inf

    for j in primes:
        tmpRes = min(tmpRes, abs(i - j))
    res = max(res, tmpRes)
print(res)
