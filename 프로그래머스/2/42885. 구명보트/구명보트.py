def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    boat = [people[start], people[end]]
    while start <= end:
        if sum(boat) <= limit:
            start += 1
            end -= 1
            boat[0] = people[start]
            boat[1] = people[end]
            answer += 1
        else:
            end -= 1
            if start == end:
                boat[1] = 0
            else:
                boat[1] = people[end]
            answer += 1
            
    return answer