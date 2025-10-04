from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]
    
    for comb in product(discounts, repeat=len(emoticons)):
        plus_cnt = 0
        total_sales = 0
        
        for rate, limit in users:
            cost = 0
            for emo_price, discount in zip(emoticons, comb):
                if discount >= rate:
                    cost += emo_price * (100 - discount) // 100
            if cost >= limit:
                plus_cnt += 1
            else:
                total_sales += cost
                
        if plus_cnt > answer[0] or (plus_cnt == answer[0] and total_sales > answer[1]):
            answer = [plus_cnt, total_sales]
    
    return answer