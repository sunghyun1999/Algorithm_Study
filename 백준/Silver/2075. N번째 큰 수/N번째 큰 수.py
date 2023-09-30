import sys
input = sys.stdin.readline
import heapq

arr = []
n = int(input())
for _ in range(n):
  data = list(map(int, input().split()))
  for num in data:
    if len(arr) < n:
      heapq.heappush(arr, num)
    else:
      if num > arr[0]:
        heapq.heappop(arr)
        heapq.heappush(arr, num)
      else:
        continue

print(arr[0])