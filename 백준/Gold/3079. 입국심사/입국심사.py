import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

left = 1
right = max(times) * m
answer = right

while left <= right:
    mid = (left + right) // 2

    total = 0
    for t in times:
        total += mid // t
        if total >= m:
            break

    if total >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
