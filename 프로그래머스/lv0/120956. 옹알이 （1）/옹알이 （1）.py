from itertools import permutations

def solution(babbling):
    answer = 0
    data = []
    for i in range(4):
        data.append(list(permutations(["aya", "ye", "woo", "ma"], i + 1)))
        
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = ''.join(list(data[i][j]))
            
    for b in babbling:
        for i in range(len(data)):
            if b in data[i]:
                answer += 1
    
    return answer