import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = min(arr)
end = max(arr)

result = 0
start = 0
while start <= end:
  total = 0
  mid = (start+end) // 2
  for money in arr:
    if money > mid:
      total += mid
    else:
      total += money
  if total > m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)