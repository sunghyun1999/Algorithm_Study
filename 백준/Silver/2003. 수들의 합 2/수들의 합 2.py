import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current_sum = 0
count = 0

for right in range(n):
    current_sum += arr[right]

    while current_sum >= m:
        if current_sum == m:
            count += 1
        current_sum -= arr[left]
        left += 1

print(count)
