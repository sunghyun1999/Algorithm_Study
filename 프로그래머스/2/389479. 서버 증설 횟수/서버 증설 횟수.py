from collections import deque

def solution(players, m, k):
    answer = 0
    running_servers = deque()
    
    for time in range(24):
        while running_servers and running_servers[0] <= time:
            running_servers.popleft()
        
        if players[time] < m:
            needed = 0
        else:
            needed = players[time] // m
            
        active = len(running_servers)
        
        need_to_add = max(0, needed - active)
        for _ in range(need_to_add):
            running_servers.append(time + k)
        answer += need_to_add
    
    return answer