import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

good_cnt = 0
for k in range(n):
  target = arr[k]
  left, right = 0, n-1

  while left < right:
    if left == k:
      left += 1
      continue
    if right == k:
      right -= 1
      continue

    sum_value = arr[left] + arr[right]
    if sum_value == target:
      good_cnt += 1
      break
    elif sum_value < target:
      left += 1
    else:
      right -= 1

print(good_cnt)
