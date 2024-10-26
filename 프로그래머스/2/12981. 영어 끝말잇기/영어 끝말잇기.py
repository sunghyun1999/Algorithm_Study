def solution(n, words):
    answer = [0, 0]
    chain = [words[0]]
    
    for i in range(1, len(words)):
        if words[i][0] == chain[-1][-1] and words[i] not in chain:
            chain.append(words[i])
        else:
            answer = [i%n+1, i//n+1]
            break

    return answer