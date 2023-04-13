def solution(s, n):
    array = list(s)
    for i in range(len(array)):
        if array[i] == ' ':
            continue
        start = ord('A') if array[i].isupper() else ord('a')
        array[i] = chr((ord(array[i]) - start + n) % 26 + start)
    
    return ''.join(array)