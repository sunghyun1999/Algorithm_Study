from itertools import combinations
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for data in combinations(nums, 3):
        if is_prime_number(sum(data)):
            answer += 1

    return answer