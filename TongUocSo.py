a = [0] * 2000001
prime = [True] * 2000002


def SieveOfEratosthenes():
    global prime
    num = 2000001
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

def snt():
    global a
    for i in range(0, 2000001):
        if prime[i]:
            a[i] = i
    i = 2
    while i * i <= 2000001:
        if prime[i]:
            for j in range(i, 2000001, i):
                if i == j: continue
                tmp = j
                while tmp % i == 0:
                    tmp /= i
                    a[j] += i
        i += 1
SieveOfEratosthenes()
snt()
# for i in a:
#     print(i, end=' ')
n = int(input())
res = 0
for i in range(1, n + 1):
    tmp = int(input())
    res += a[tmp]
print(res)