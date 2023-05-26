def solution(brown, yellow):
    grid = brown + yellow
    for n in range(3, int(grid**0.5)+1):
        if grid % n == 0:
            m = grid // n
            if (m-2) * (n-2) == yellow:
                return [m, n]