# 노드 n개 번호 1~n
# 1번 노드에서 가장 멀리 떨어진 노드 갯수 구하기
# 가장 멀리 떨어진 노드 = 최단 경로로 이동했을 때 간선 갯수 가장 많은 노드

# 2 <= n <= 20000
# 1 <= len(edge) <= 50000
# [a,b] 이어짐, 간선 존재

from collections import deque

def solution(n, edge):
    # 인접 리스트 초기화
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        x, y = e
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS 탐색
    visited = [False] * (n + 1)
    visited[1] = True
    q = deque([(1, 0)])  # (노드, 거리)
    max_distance = 0
    count = 0
    
    while q:
        node, distance = q.popleft()
        
        if distance > max_distance:
            max_distance = distance
            count = 1
        elif distance == max_distance:
            count += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, distance + 1))
    
    return count