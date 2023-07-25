from collections import defaultdict
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_len = 0
start, end = 0, 0
count = defaultdict(int)

while end < n:
  if count[arr[end]] < k:
    count[arr[end]] += 1
    end += 1
  else:
    count[arr[start]] -= 1
    start += 1
  max_len = max(max_len, end-start)

print(max_len)