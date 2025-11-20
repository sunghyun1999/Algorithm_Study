import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

left, right = 1, max(lines)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    for line in lines:
        total += line // mid

    if total >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
