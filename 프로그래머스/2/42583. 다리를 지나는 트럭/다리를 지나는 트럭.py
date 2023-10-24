def solution(bridge_length, weight, truck_weights):
    answer = 0
    arrive = []
    driving = []
    distance = []
    sum_weight = 0
    n = len(truck_weights)
    while True:
        for i in range(len(distance)):
            distance[i] -= 1
        if len(distance) > 0 and distance[0] == 0:
            sum_weight -= driving[0]
            arrive.append(driving.pop(0))
            distance.pop(0)
        if len(truck_weights) > 0 and sum_weight + truck_weights[0] <= weight:
            sum_weight += truck_weights[0]
            driving.append(truck_weights.pop(0))
            distance.append(bridge_length)
        answer += 1
        if len(arrive) == n:
            break
    
    return answer