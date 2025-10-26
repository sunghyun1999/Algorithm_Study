def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]
    
    while True:
        remove_set = set()
        
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == ' ':
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    remove_set |= {(i, j), (i+1, j), (i, j+1), (i+1, j+1)}
                    
        if not remove_set:
            break
            
        for i, j in remove_set:
            board[i][j] = ' '
            
        answer += len(remove_set)
        
        for j in range(n):
            empty = [' '] * m
            idx = m - 1
            for i in range(m-1, -1, -1):
                if board[i][j] != ' ':
                    empty[idx] = board[i][j]
                    idx -= 1
            
            for i in range(m):
                board[i][j] = empty[i]
    
    return answer