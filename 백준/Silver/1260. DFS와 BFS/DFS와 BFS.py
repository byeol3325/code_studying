import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited_DFS = [0]*(N+1)
visited_BFS = [0]*(N+1)

def DFS(v):
    visited_DFS[v] = 1
    print(v, end=" ")
    for i in range(1, N+1):
        if visited_DFS[i] == 0 and graph[v][i] == 1:
            DFS(i)

def BFS(v):
    visited_BFS[v] = 1
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N+1):
            if visited_BFS[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_BFS[i] = 1

DFS(V)
print()
BFS(V)