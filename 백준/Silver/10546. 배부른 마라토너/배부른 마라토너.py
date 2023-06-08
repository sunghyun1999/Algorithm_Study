import sys
input = sys.stdin.readline

n = int(input())
names = dict()

for _ in range(n):
  name = input()
  if name in names.keys():
    names[name] += 1
  else:
    names[name] = 1

for _ in range(n-1):
  name = input()
  names[name] -= 1

for name in names.keys():
  if names[name] != 0:
    print(name)