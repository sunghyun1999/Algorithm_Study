def width(game, winner):
  for i in range(3):
    tmp = set(game[i])
    if len(tmp) == 1:
      winner.add(list(tmp)[0])

def height(game, winner):
  for j in range(3):
    tmp = set()
    for i in range(3):
      tmp.add(game[i][j])
    if len(tmp) == 1:
      winner.add(list(tmp)[0])

def diagonal(game, winner):
  tmp = set()
  for i in range(3):
    tmp.add(game[i][i])
  if len(tmp) == 1:
    winner.add(list(tmp)[0])
  tmp = set()
  for i in range(3):
    tmp.add(game[i][2-i])
  if len(tmp) == 1:
    winner.add(list(tmp)[0])

while True:
  test_case = input()
  if test_case == 'end':
    break
  answer = 'invalid'
  game = []
  for i in range(0, 9, 3):
    game.append(list(test_case[i:i+3]))
  winner = set()
  width(game, winner)
  height(game, winner)
  diagonal(game, winner)
  if '.' in winner:
    winner.remove('.')
  if len(winner) == 0:
    if test_case.count('X') == 5 and test_case.count('O') == 4:
      answer = 'valid'
  elif len(winner) == 1 and list(winner)[0] == 'X':
    if test_case.count('X') == test_case.count('O') + 1:
      answer = 'valid'
  elif len(winner) == 1 and list(winner)[0] == 'O':
    if test_case.count('X') == test_case.count('O'):
      answer = 'valid'
      
  print(answer)