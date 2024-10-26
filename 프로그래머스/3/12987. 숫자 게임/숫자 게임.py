def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    for num in A:
        if num < B[i]:
            answer += 1
            i += 1
    return answer