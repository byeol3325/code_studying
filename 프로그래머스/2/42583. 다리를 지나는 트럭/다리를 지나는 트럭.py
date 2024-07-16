from collections import defaultdict, deque

def solution(bridge_length, weight, truck_weights):
    """
    params bridge_length: 다리에 트럭이 최대 오를 수 있는 수 이면서 지나갈때 걸리는 시간
    params weight: 최대 무게(합)
    params truck_weights: 각 트럭 무게
    """
    answer = 0
    
    bridge = [0]*bridge_length # [weigt] 들어가는데 length 만큼 0 이 들어감
    bridge = deque(bridge)
    total_weight = 0
    
    truck_weights = deque(truck_weights)
    
    now_time = 1 # 차가 올라간 시간은 1초 부터 시작
    while truck_weights:
        total_weight -= bridge.popleft() # 0이든 차량이든 시간이 지나감
        
        if total_weight + truck_weights[0] <= weight: # 최대 무게보다 낮으면서 차량을 올릴 수 있는지
            now_truck = truck_weights.popleft()
            total_weight += now_truck
            bridge.append(now_truck)
        else: # 차량 올릴 수 없으면 바로 0 으로 시간만 떼우기
            bridge.append(0)
        
        now_time += 1 # 1초씩 시간 감
        
    return now_time + bridge_length - 1