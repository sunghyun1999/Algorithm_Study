def solution(friends, gifts):
    answer = 0
    n = len(friends)
    
    gift_log = [[0] * n for _ in range(n)]
    
    for gift in gifts:
        a, b = gift.split()
        gift_log[friends.index(a)][friends.index(b)] += 1
        
    gift_index = []
    
    for i in range(len(friends)):
        give = sum(gift_log[i])
        take = sum(row[i] for row in gift_log)
        gift_index.append(give - take) 
        
    next_gift = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if gift_log[i][j] != gift_log[j][i]:
                if gift_log[i][j] > gift_log[j][i]:
                    next_gift[i] += 1
                else:
                    next_gift[j] += 1

            elif gift_index[i] != gift_index[j]:
                if gift_index[i] > gift_index[j]:
                    next_gift[i] += 1
                else:
                    next_gift[j] += 1
    
    return max(next_gift)