def solution(n, computers):
    visited = [-1] * n
    def dfs(v, group):
        if visited[v] == -1:
            visited[v] = group
        for i in range(n):
            if computers[v][i] == 1 and i != v and visited[i] == -1:
                dfs(i, group)
        return
    
    for i in range(n):
        dfs(i, i)
    
    return len(set(visited))