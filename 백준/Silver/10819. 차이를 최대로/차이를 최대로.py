from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
perm = permutations(data, n)

answer = 0
for p in perm:
    tmp = 0
    for i in range(n-1):
        tmp += abs(p[i] - p[i+1])
    answer = max(answer, tmp)

print(answer)
