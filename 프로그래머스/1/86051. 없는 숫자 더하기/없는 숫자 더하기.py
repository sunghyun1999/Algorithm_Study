def solution(numbers):
    data = [i for i in range(10)]
    item = [num for num in data if num not in numbers]
    return sum(item)