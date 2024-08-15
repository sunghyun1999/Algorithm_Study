import sys

input = sys.stdin.readline
m = int(input())
S = set()

for _ in range(m):
  calc = input().split()
  if calc[0] == 'add':
    S.add(int(calc[1]))
  elif calc[0] == 'remove':
    S.discard(int(calc[1]))
  elif calc[0] == 'check':
    print(1 if int(calc[1]) in S else 0)
  elif calc[0] == 'toggle':
    if int(calc[1]) in S:
      S.remove(int(calc[1]))
    else:
      S.add(int(calc[1]))
  elif calc[0] == 'all':
    S = set(range(1, 21))
  elif calc[0] == 'empty':
    S.clear()
