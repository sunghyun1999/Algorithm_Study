import sys
input = sys.stdin.readline

answer = 0
n = int(input())
m = int(input())

material = list(map(int, input().split()))

material.sort()
left = 0 
right = len(material) - 1

while left < right:
    if material[left] + material[right] == m:
        answer += 1
        left += 1
        right -= 1
    elif material[left] + material[right] > m:
        right -= 1
    else:
        left += 1

print(answer)