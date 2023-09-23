import sys
input = sys.stdin.readline

p, m = map(int, input().split())

game = []
for _ in range(p):
  level, id = input().split()
  level = int(level)
  if len(game) == 0:
    game.append([(level, id)])
  else:
    entrance = False
    for i in range(len(game)):
      if len(game[i]) == m:
        continue
      if game[i][0][0] - 10 <= level <= game[i][0][0] + 10:
        game[i].append((level, id))
        entrance = True
        break
    if entrance == False:
      game.append([(level, id)])

for g in game:
  g.sort(key=lambda x: x[1])
  if len(g) == m:
    print("Started!")
  else:
    print("Waiting!")
  for i in g:
    print(i[0], i[1])