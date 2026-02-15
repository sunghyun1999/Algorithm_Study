n, new_score, p = map(int, input().split())

if n > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

if n == 0:
    print(1)

else:
    rank = 1

    for score in scores:
        if score > new_score:
            rank += 1
        else:
            break

    if n == p and scores[-1] >= new_score:
        print(-1)
    else:
        print(rank)
