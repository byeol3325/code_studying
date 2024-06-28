# 실내공조 제어 시스템. 차내에 승객이 탑승 중일 때, 쾌적한 실내온도 t1 ~ t2 유지할 수 있도록.
# 희망온도는 에어컨의 전원이 켜져있는 동안 원하는 값으로 변경 가능
# 실내 온도와 희망온도가 다르다면 1분 뒤 실내온도가 희망온도와 같아지는 방향으로 1도 상승 또는 하강
# 실내 == 희망. 에어컨 켜져 있으면 실내온도 변화X

# 에어컨 끄면, 실외온도와 같아지는 방향으로 1분 상승 / 하강
# 실내 == 실외, 실내 변화 X

# 소비전력. 실내온도에 따라 달라짐. 희망온도와 실내온도가 다르면 매분 전력 a만큼 소비 / 같으면 b만큼 소비
# 꺼져있으면 전력소비 X
# 에어컨 on/off는 시간/전력 0
# 승객이 탑승 중인 시간에 쾌적한 실내온도를 유지하기 위한 최소 소비 전력을 return
def solution(temperature: int, t1: int, t2: int, a: int, b: int, onboard: list) -> int:
    """
    :param temperature: 실외 온도
    :param t1: 희망온도 t1
    :param t2: 희망온도 t2
    :param a: 희망온도와 실내온도가 다를 때 1분당 소비전력
    :param b: 희망온도와 실내온도가 같을 때 1분당 소비전력
    :param onboard: [i]는 0/1. [0]=0, 1일 경우 
    :return: 최소 전력
    """
    MAX_ = 10**(2+3)
    t1 += 10
    t2 += 10
    temperature += 10
    DP = [[MAX_]*(53) for _ in range(len(onboard))] # [time][temp] = e / time에서 temp 온도로 만드는데 드는 e 에너지
    
    in_temp = temperature
    DP[0][in_temp] = 0
    n = len(onboard)
    
    on_aircon = 0 # 에어컨 키면 진행되는 방향. 0이면 t1 ~ t2 사이
    if (temperature - t1) * (temperature - t2) > 0:
        on_aircon = (temperature - t1) // abs(temperature - t1) # temp > t1 이면 에어컨 키면 내려감 켜지면 -on_aircon
        
    if on_aircon == 0: # 에어컨 가동할 필요가 없음
        return 0
    
    
    for time in range(1, n):
        for temp in range(51):
            # [time][temp]
            next_min = []
            if onboard[time] == 0 or (onboard[time] == 1 and t1 <= temp <= t2): # 승객이 탔을 때
                if 0 <= temp + on_aircon <= 50:
                    next_min.append(DP[time-1][temp+on_aircon] + a) # 에어컨 ON로 왔음
                if 0 <= temp - on_aircon <= 50:
                    next_min.append(DP[time-1][temp-on_aircon]) # 에어컨 OFF로 왔어
                if temp == temperature:
                    next_min.append(DP[time-1][temp])
                if t1 <= temp <= t2:
                    next_min.append(DP[time-1][temp] + b) # 에어컨 STAY로 왔어
            
            if next_min == []: # 굳이 계산할 필요 없음
                continue
            else: # 계산해야지 반드시 계산해야지
                DP[time][temp] = min(next_min)
        
    return min(DP[n-1])