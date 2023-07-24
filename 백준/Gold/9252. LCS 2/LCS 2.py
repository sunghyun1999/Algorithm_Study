def LCS(x, y):
  dp = [['' for _ in range(len(y)+1)] for _ in range(len(x)+1)]
  for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
      if x[i-1] == y[j-1]:
        dp[i][j] = dp[i-1][j-1] + x[i-1]
      else:
        if len(dp[i-1][j]) >= len(dp[i][j-1]):
          dp[i][j] = dp[i-1][j]
        else:
          dp[i][j] = dp[i][j-1]

  if len(dp[len(x)][len(y)]) == 0:
    print(0)
  else:
    print(len(dp[len(x)][len(y)]))
    print(dp[len(x)][len(y)])

a = input()
b = input()
LCS(a, b)