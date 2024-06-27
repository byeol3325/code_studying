n, m = map(int, input().split())

s = []
visited = [False] * (n+1)
def backtracking():
    global n, m, s, visited
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        backtracking()
        s.pop()
        #print(s)
        #print(visited)
        visited[i] = False

backtracking()