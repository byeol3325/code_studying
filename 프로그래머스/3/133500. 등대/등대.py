from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def make_graph(lighthouse: list) -> dict:
    graph = defaultdict(lambda:[])
    for u,v in lighthouse:
        graph[u-1].append(v-1) # 1번부터 시작이라 -1 해줬음
        graph[v-1].append(u-1)
    return graph

def solution(n: int, lighthouse:list) -> int:
    answer = 0
    graph = make_graph(lighthouse)
    #print(graph)
    
    DP = [[0,0] for _ in range(n)]
    visited = [0] * n
    
    def dfs(s: int) -> None:
        visited[s] = 1
        for v in graph[s]:
            if visited[v] == 0:
                dfs(v)
        
        DP[s][0] += 1 # s가 켜진 경우
        
        for v in graph[s]:
            DP[s][0] += min(DP[v]) # s가 켜진 경우
            DP[s][1] += DP[v][0] # s가 꺼진 경우, 좌우가 켜져있어야함
        return None
    
    dfs(0)
    
    return min(DP[0])