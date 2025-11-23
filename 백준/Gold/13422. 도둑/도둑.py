import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ans = 0
    n, m, k = map(int, input().split())
    money = list(map(int, input().split()))

    if n == m:
        print(1 if sum(money) < k else 0)
        continue

    money.extend(money[:m-1])
    
    window_sum = sum(money[:m])
    if window_sum < k:
        ans += 1
    
    for i in range(1, n):
        window_sum -= money[i-1]
        window_sum += money[i+m-1]
        if window_sum < k:
            ans += 1

    print(ans)
