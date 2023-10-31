n = int(input())
skyline = []
answer = 0
for _ in range(n):
  x, y = map(int, input().split())
  while len(skyline) > 0 and skyline[-1] > y:
    answer += 1
    skyline.pop()
  if len(skyline) > 0 and skyline[-1] == y:
    continue
  skyline.append(y)

while len(skyline) > 0:
  if skyline[-1] > 0:
    answer += 1
  skyline.pop()

print(answer)