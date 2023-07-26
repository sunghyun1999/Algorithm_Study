n, k = map(int, input().split())
temperature = list(map(int, input().split()))
prefix_sum = [0] * (n+1)

for i in range(n):
  prefix_sum[i+1] = prefix_sum[i] + temperature[i]

max_value = prefix_sum[k] - prefix_sum[0]
for i in range(k+1, n+1):
  sum_value = prefix_sum[i] - prefix_sum[i-k]
  max_value = max(max_value, sum_value)

print(max_value)