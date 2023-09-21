import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = []
for _ in range(n):
  memo.append(input().strip())
memo.sort()

res = set()
for _ in range(m):
  post = list(input().strip().split(','))
  for keyword in post:
    start = 0
    end = len(memo) - 1
    while start <= end:
      mid = (start + end) // 2
      if memo[mid] == keyword:
        res.add(keyword)
        break
      elif memo[mid] > keyword:
        end = mid - 1
      else:
        start = mid + 1
  print(len(memo) - len(res))