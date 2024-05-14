import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split())) # N nums

q = deque()
for i in range(N):
    num = nums[i]
    while q and q[-1] > num:
        q.pop()
    q.append(num)
    if i >= L and q[0] == nums[i-L]:
        q.popleft()
    print(q[0], end=' ')