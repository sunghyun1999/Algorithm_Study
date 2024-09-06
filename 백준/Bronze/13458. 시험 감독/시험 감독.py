n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

res = n
for i in range(n):
  if a[i] - b > 0:
    res += (a[i] - b) // c + 1 if (a[i] - b) % c != 0 else (a[i] - b) // c

print(res)