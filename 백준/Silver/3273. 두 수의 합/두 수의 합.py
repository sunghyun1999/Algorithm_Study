import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())

num.sort()
left, right = 0, n - 1
cnt = 0

while left < right:
    sum_value = num[left] + num[right]
    if sum_value == x:
        cnt += 1
        left += 1
        right -= 1
    elif sum_value < x:
        left += 1
    else:
        right -= 1

print(cnt)
