from collections import deque, defaultdict

def make_graph(roads: list) -> dict:
    graph = defaultdict(lambda: [])
    for u,v in roads:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def make_dist(n: int, graph: list, dest: int):
    dist_dict = defaultdict(lambda:-1)
    dist_dict[dest] = 0
    
    visited = [False] * (n+1)
    q = deque()
    q.append(dest); visited[dest] = True
    dist = 0
    while True:
        next_q = deque()
        for _ in range(len(q)):
            now = q.popleft()
            dist_dict[now] = dist
            for next_ in graph[now]:
                if visited[next_] == False:
                    next_q.append(next_)
                    visited[next_] = True
        if len(next_q) == 0:
            break
        dist += 1
        q = next_q
    return dist_dict

def solution(n, roads, sources, destination):
    """
    params n: 각 지역. 1~n까지
    params roads: 두 지역 왕복할 수 있는 길. (방향성 X, a,b있으면 b,a는 주어지지않음. 중복해서 주는거 없음)
    params sources: 각 부대원이 위치한 서로 다른 지역들
    params destination: 주어진 sources의 원소 순서대로 강철부대로 
    """
    answer = [0] * len(sources)
    graph = make_graph(roads)
    dist_dict = make_dist(n, graph, destination)
    
    for i, s in enumerate(sources):
        answer[i] = dist_dict[s]

    return answer