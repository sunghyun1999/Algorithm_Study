from itertools import combinations

n, m = map(int, input().split())

numbers = [str(i) for i in range(1, n + 1)]
for combo in combinations(numbers, m):
    print(' '.join(combo))
