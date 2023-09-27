from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons):
        nk = k
        total = 0
        for data in dungeon:
            if data[0] <= nk:
                total += 1
                nk -= data[1]
        answer = max(answer, total)
        
    return answer