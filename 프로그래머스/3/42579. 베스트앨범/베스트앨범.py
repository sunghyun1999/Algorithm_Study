from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_dict = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_dict[g].append((p, i))
        
    genre_total = {g: sum(p for p, _ in songs) for g, songs in genre_dict.items()}
    
    sorted_genres = sorted(genre_total.keys(), key=lambda g: genre_total[g], reverse=True)
    
    for g in sorted_genres:
        songs = sorted(genre_dict[g], key=lambda x: (-x[0], x[1]))
        answer.extend(i for _, i in songs[:2])
    
    return answer