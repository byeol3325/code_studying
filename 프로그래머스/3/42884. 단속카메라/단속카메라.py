# 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한번은 만나도록 설치
# 최소 몇 대의 카메라를 설치 해야하는지 return을
# routes에는 이동 경로가 포함됨. routes[i][0]에는 i번째 차량이 고속도로에 진입한 시점, routes[i][1]에는 i 번째 차량이 고속도로에서 나간 지점.

def solution(routes):
    answer = 0
    n = len(routes)
    if n == 1:
        return 1
    cameras = []
    routes.sort()
    
    s = routes[0][0]; e = routes[0][1]; answer += 1
    for i in range(1, n):
        if e < routes[i][0]: # 겹치는 구간이 없음, 바로 카메라 추가
            s = routes[i][0]; e = routes[i][1]; answer += 1
        else:
            s = max(routes[i][0], s)
            e = min(routes[i][1], e)
    
    return answer