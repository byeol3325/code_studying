from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for w in wires:
        [v1, v2] = w
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def count_tree(v1: int, cut_wire: set):
        nonlocal n
        q = deque()
        cnt = 0
        visited = [0]*(n+1)
        
        q.append(v1)
        visited[v1] = 1
        while q:
            v1 = q.popleft()
            cnt += 1
            for v2 in graph[v1]:
                if visited[v2] == 0 and (v1 not in cut_wire or v2 not in cut_wire):
                    visited[v2] = 1
                    q.append(v2)
        return cnt
    
    answer = float("inf")
    for w in wires:
        v1 = w[0]
        cut_wire = set(w)
        A = count_tree(v1, cut_wire)
        answer = min(answer, abs(n-2*A))
    return answer