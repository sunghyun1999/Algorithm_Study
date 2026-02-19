from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque([(i, priorities[i]) for i in range(n)])
    priorities_sorted = sorted(priorities, reverse=True)

    count = 0

    while queue:
        idx, priority = queue.popleft()

        if priority == priorities_sorted[0]:
            count += 1
            priorities_sorted.pop(0)

            if idx == m:
                print(count)
                break
        else:
            queue.append((idx, priority))
