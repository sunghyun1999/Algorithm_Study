import sys
input = sys.stdin.readline

def change(bulbs, cnt):
  for i in range(1, n-1):
    if bulbs[i-1] != target[i-1]:
      cnt += 1
      for j in range(i-1, i+2):
        bulbs[j] = 1 - bulbs[j]
  if bulbs[n-1] != target[n-1]:
    bulbs[n-2] = 1 - bulbs[n-2]
    bulbs[n-1] = 1 - bulbs[n-1]
    cnt += 1
  if bulbs == target:
    return cnt
  else:
    return 1e9

n = int(input())

first_off = list(map(int, input().strip()))

first_on = first_off.copy()
first_on[0] = 1 - first_on[0]
first_on[1] = 1 - first_on[1]

target = list(map(int, input().strip()))

res = min(change(first_off, 0), change(first_on, 1))
print(res if res != 1e9 else -1)