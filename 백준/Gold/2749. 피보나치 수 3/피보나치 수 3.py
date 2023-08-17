pisano = 1000000 // 10 * 15
d = [0] * (pisano)
d[1] = 1
d[2] = 1

n = int(input())
for i in range(3, pisano):
  d[i] = (d[i-2] + d[i-1]) % 1000000

print(d[n%pisano])