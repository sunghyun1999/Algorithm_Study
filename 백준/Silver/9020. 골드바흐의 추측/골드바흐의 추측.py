import sys
input = sys.stdin.readline

MAX = 10000

is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for p in range(2, int(MAX**0.5) + 1):
    if is_prime[p]:
        for q in range(p * p, MAX + 1, p):
            is_prime[q] = False

T = int(input())
for _ in range(T):
    n = int(input())
    a = n // 2
    for i in range(a, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break
