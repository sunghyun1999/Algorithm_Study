n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        left = triangle[i-1][j-1] if j > 0 else 0
        right = triangle[i-1][j] if j < i else 0

        triangle[i][j] += max(left, right)

print(max(triangle[-1]))