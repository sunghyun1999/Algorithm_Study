def solution(m, n, puddles):
    MOD = 1000000007
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    
    for puddle in puddles:
        x, y = puddle
        dp[y][x] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                continue
            if i > 1 and dp[i-1][j] != -1:
                dp[i][j] += dp[i-1][j]
            if j > 1 and dp[i][j-1] != -1:
                dp[i][j] += dp[i][j-1]
        
    return dp[n][m] % MOD