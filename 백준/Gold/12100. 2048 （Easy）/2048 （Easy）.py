import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def move(board, direction):
    new_board = [[0] * n for _ in range(n)]

    if direction == 0:
        for c in range(n):
            stack = []
            for r in range(n):
                if board[r][c] != 0:
                    stack.append(board[r][c])
            idx = 0
            while stack:
                num = stack.pop(0)
                if new_board[idx][c] == 0:
                    new_board[idx][c] = num
                elif new_board[idx][c] == num:
                    new_board[idx][c] *= 2
                    idx += 1
                else:
                    idx += 1
                    new_board[idx][c] = num

    elif direction == 1:
        for c in range(n):
            stack = []
            for r in range(n-1, -1, -1):
                if board[r][c] != 0:
                    stack.append(board[r][c])
            idx = 0
            while stack:
                num = stack.pop(0)
                if new_board[n-1-idx][c] == 0:
                    new_board[n-1-idx][c] = num
                elif new_board[n-1-idx][c] == num:
                    new_board[n-1-idx][c] *= 2
                    idx += 1
                else:
                    idx += 1
                    new_board[n-1-idx][c] = num

    elif direction == 2:
        for r in range(n):
            stack = []
            for c in range(n):
                if board[r][c] != 0:
                    stack.append(board[r][c])
            idx = 0
            while stack:
                num = stack.pop(0)
                if new_board[r][idx] == 0:
                    new_board[r][idx] = num
                elif new_board[r][idx] == num:
                    new_board[r][idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    new_board[r][idx] = num

    else:
        for r in range(n):
            stack = []
            for c in range(n-1, -1, -1):
                if board[r][c] != 0:
                    stack.append(board[r][c])
            idx = 0
            while stack:
                num = stack.pop(0)
                if new_board[r][n-1-idx] == 0:
                    new_board[r][n-1-idx] = num
                elif new_board[r][n-1-idx] == num:
                    new_board[r][n-1-idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    new_board[r][n-1-idx] = num

    return new_board

answer = 0

def dfs(board, depth):
    global answer

    if depth == 5:
        for r in range(n):
            for c in range(n):
                answer = max(answer, board[r][c])
        return

    for dir in range(4):
        new_b = move(deepcopy(board), dir)
        dfs(new_b, depth + 1)

dfs(board, 0)

print(answer)
