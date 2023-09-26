import sys
input = sys.stdin.readline

pillar = []
n = int(input())
for _ in range(n):
  l, h = map(int, input().split())
  pillar.append((l, h))

pillar.sort(key=lambda x: x[0])
max_height = 0
for i in range(len(pillar)):
  if pillar[i][1] > max_height:
    max_height = pillar[i][1]
    high = i

area = pillar[high][1]
curr_h = pillar[0][1]
for i in range(high):
  if curr_h < pillar[i+1][1]:
    area += (pillar[i+1][0]-pillar[i][0]) * curr_h
    curr_h = pillar[i+1][1]
  else:
    area += (pillar[i+1][0]-pillar[i][0]) * curr_h

curr_h = pillar[n-1][1]
for i in range(n-1, high, -1):
  if curr_h < pillar[i-1][1]:
    area += (pillar[i][0]-pillar[i-1][0]) * curr_h
    curr_h = pillar[i-1][1]
  else:
    area += (pillar[i][0]-pillar[i-1][0]) * curr_h

print(area)