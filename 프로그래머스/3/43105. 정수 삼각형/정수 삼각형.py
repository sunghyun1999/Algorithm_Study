def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            left = 0 if j == 0 else triangle[i-1][j-1]
            right = 0 if j == i else triangle[i-1][j]
            triangle[i][j] += max(left, right)
    
    return max(triangle[-1])