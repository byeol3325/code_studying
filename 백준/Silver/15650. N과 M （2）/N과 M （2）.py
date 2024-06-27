n, m = map(int, input().split())

s = []
visited = [False] * (n+1)

def backtracking():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        if s == [] or s[-1] < i:
            s.append(i)
            backtracking()
            s.pop()
        else:
            continue

backtracking()