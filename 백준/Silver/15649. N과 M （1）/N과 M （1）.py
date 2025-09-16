from itertools import permutations

n, m = map(int, input().split())

numbers = [str(i) for i in range(1, n + 1)]
for combo in permutations(numbers, m):
    print(' '.join(combo))
