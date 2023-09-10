from collections import deque

def solution(board):
    answer = -1
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i, j, 0))
                
    while queue:
        x, y, cnt = queue.popleft()
        if board[x][y] == 'G':
            answer = cnt
            break
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[1]) and board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    
    return answer