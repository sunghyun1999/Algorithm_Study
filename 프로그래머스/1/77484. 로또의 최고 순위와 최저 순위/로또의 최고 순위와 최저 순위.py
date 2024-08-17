def solution(lottos, win_nums):
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    cnt = 0
    erased = lottos.count(0)
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
    answer.append(rank.get(cnt+erased, 6))
    answer.append(rank.get(cnt, 6))
    return answer