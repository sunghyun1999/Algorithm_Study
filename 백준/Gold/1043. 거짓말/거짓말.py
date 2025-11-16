import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

n, m = map(int, input().split())
truth = list(map(int, input().split()))

truth_cnt = truth[0]
truth_people = truth[1:] if truth_cnt > 0 else []

parent = [i for i in range(n + 1)]

parties = []

for _ in range(m):
    info = list(map(int, input().split()))
    cnt = info[0]
    people = info[1:]
    parties.append(people)

    for i in range(1, cnt):
        union(people[0], people[i])

truth_roots = set(find(p) for p in truth_people)

answer = 0

for party in parties:
    can_lie = True
    for person in party:
        if find(person) in truth_roots:
            can_lie = False
            break
    if can_lie:
        answer += 1

print(answer)
