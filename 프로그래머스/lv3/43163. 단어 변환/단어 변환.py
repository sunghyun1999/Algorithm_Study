from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            if visited[i] == False:
                diff = 0
                for j in range(len(words[i])):
                    if word[j] != words[i][j]:
                        diff += 1
                if diff == 1:
                    visited[i] = True
                    queue.append((words[i], cnt+1))
    
    return answer