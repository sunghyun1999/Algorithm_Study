def solution(n):
    answer = []
    array = [[0] * n for _ in range(n)]
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    size = n * (n+1) // 2
    direction = 0
    x = y = 0
    cnt = 1
    
    while cnt <= size:
        array[y][x] = cnt
        cnt += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < n and array[ny][nx] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 3
            x += dx[direction]
            y += dy[direction]

    for i in range(n):
        for j in range(i+1):
            answer.append(array[i][j])
            
    return answer