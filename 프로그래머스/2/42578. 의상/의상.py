from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    for cloth in clothes:
        clothes_dict[cloth[1]].append(cloth[0])
    
    for category in clothes_dict.keys():
        answer *= len(clothes_dict[category]) + 1
    
    return answer - 1