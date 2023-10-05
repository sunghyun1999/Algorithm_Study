import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def game(t):
  if len(t) == len(s):
    if t == s:
      print(1)
      return
    else:
      print(0)
      return
  if t[-1] == 'A':
    game(t[:-1])
  if t[-1] == 'B':
    game(t[:-1][::-1])

s = input().strip()
t = input().strip()

game(t)