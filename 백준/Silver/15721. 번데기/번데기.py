a = int(input())
t = int(input())
say = int(input())

bundegi = []
bun = degi = 1
turn = 0

while True:
  prev_n = bun
  turn += 1
  for _ in range(2):
    bundegi.append((bun, 0))
    bun += 1
    bundegi.append((degi, 1))
    degi += 1
  for _ in range(turn+1):
    bundegi.append((bun, 0))
    bun += 1
  for _ in range(turn+1):
    bundegi.append((degi, 1))
    degi += 1
  if prev_n <= t < bun:
    print(bundegi.index((t, say)) % a)
    break