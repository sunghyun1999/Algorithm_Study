from collections import deque

def solution(arr):
    answer = []
    tmp = 10
    queue = deque(arr)
    while queue:
        num = queue.popleft()
        if num != tmp:
            answer.append(num)
            tmp = num
    
    return answer