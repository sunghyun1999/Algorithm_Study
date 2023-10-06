import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def game(t):
  global answer
  if len(s) == len(t):
    if s == t:
      answer = 1
    return
  if t[-1] == 'A':
    game(t[:-1])
  if t[0] == 'B':
    game(t[::-1][:-1])

answer = 0
s = input().strip()
t = input().strip()

game(t)
print(answer)