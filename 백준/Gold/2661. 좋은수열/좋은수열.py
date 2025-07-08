def is_good(seq):
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def dfs(seq):
    global found, n
    if found:
        return
    if len(seq) == n:
        print(seq)
        found = True
        return
    for num in '123':
        new_seq = seq + num
        if is_good(new_seq):
            dfs(new_seq)

n = int(input())
found = False
dfs('')
