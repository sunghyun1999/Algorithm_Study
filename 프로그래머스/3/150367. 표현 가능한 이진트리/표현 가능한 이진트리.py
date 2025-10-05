def solution(numbers):
    def valid(tree_str: str) -> bool:
        if len(tree_str) == 1:
            return True
        mid = len(tree_str) // 2
        root = tree_str[mid]
        left = tree_str[:mid]
        right = tree_str[mid + 1:]
        if root == '0' and ('1' in left or '1' in right):
            return False
        return valid(left) and valid(right)
    
    answer = []
    
    for n in numbers:
        b = bin(n)[2:]
        h = 1
        nodes = (2 ** h) - 1
        while nodes < len(b):
            h += 1
            nodes = (2 ** h) - 1
            
        padded = '0' * (nodes - len(b)) + b
        
        answer.append(1 if valid(padded) else 0)
    
    return answer