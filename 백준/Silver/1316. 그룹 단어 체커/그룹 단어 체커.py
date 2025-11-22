n = int(input())
ans = 0

for _ in range(n):
    word = input()
    visited = set()
    last_char = ''

    is_group = True
    for ch in word:
        if ch != last_char:
            if ch in visited:
                is_group = False
            visited.add(ch)
        last_char = ch

    if is_group:
        ans += 1

print(ans)
