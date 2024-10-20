from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        queue = deque(skill)
        is_tree = True
        for s in tree:
            if s in skill:
                if s == queue[0]:
                    queue.popleft()
                else:
                    is_tree = False
                    break
        if is_tree:
            answer += 1
                    
    return answer