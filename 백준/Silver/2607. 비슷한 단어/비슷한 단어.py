n = int(input())
word1 = list(input())

answer = 0
for _ in range(n-1):
  word2 = list(input())
  if len(word1) == len(word2):
    arr = []
    for i in word1:
      if i in word2:
        arr.append(i)
        word2.remove(i)
    if len(arr) >= len(word1) - 1:
      answer += 1
  elif abs(len(word1) - len(word2)) == 1:
    arr = []
    tmp = min(len(word1), len(word2))
    for i in word1:
      if i in word2:
        arr.append(i)
        word2.remove(i)
    if len(arr) == tmp:
      answer += 1

print(answer)