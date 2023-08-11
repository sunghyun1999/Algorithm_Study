from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = [(idx, val) for idx, val in enumerate(priorities)]
    queue = deque(priorities)
    while queue:
        max_value = max(queue, key=lambda x: x[1])
        tmp = queue.popleft()
        if tmp[1] == max_value[1]:
            if tmp[0] == location:
                answer += 1
                break
            else:
                answer += 1
        else:
            queue.append(tmp)
    
    return answer