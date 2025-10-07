N = int(input())
board = [list(input()) for _ in range(N)]

def check_max(board):
    n = len(board)
    max_len = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                max_len = max(max_len, cnt)
            else:
                cnt = 1

    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                cnt += 1
                max_len = max(max_len, cnt)
            else:
                cnt = 1

    return max_len

answer = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check_max(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i + 1 < N and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check_max(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)
