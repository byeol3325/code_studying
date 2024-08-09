def solution(food_times, k):
    if sum(food_times) <= k:  # 모든 음식을 다 먹을 수 있다면
        return -1
    
    sorted_food_times = sorted((time, idx + 1) for idx, time in enumerate(food_times))
    prev_time = 0
    length = len(food_times)
    
    for i, (time, idx) in enumerate(sorted_food_times):
        # 현재 음식까지 먹는 데 걸리는 시간
        current_time = (time - prev_time) * (length - i)
        
        if k < current_time:
            k %= (length - i)
            remaining_food = sorted(sorted_food_times[i:], key=lambda x: x[1])
            return remaining_food[k][1]
        
        k -= current_time
        prev_time = time
    
    return -1