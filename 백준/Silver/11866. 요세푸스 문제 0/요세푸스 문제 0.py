n, k = map(int, input().split())
circle = [i + 1  for i in range(n)]
pos = 0
answer = []

while circle:
    target = pos + k - 1
    if target >= len(circle):
        target = target % len(circle)
    answer.append(circle.pop(target))
    pos = target

print('<' + ', '.join(map(str, answer)) + '>')
