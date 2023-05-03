n = int(input())
pinary = [0, 1, 1]

for i in range(3, n+1):
  pinary.append(pinary[i-1] + pinary[i-2])

print(pinary[n])