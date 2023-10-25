from collections import defaultdict

def solution(tickets):
    answer = []
    flight = defaultdict(list)
    for ticket in tickets:
        flight[ticket[0]].append(ticket[1])
    for dest in flight.keys():
        flight[dest].sort(reverse = True)
        
    stack = ["ICN"]
    while stack:
        src = stack[-1]
        if flight[src]:
            stack.append(flight[src].pop())
        else:
            answer.append(stack.pop())
    
    return answer[::-1]