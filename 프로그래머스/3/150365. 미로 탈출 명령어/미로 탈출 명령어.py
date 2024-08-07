from collections import deque

PATH_directions = [[1, 0], [0, -1], [0, 1], [-1, 0]] # d l r u
PATH = ['d', 'l', 'r', 'u']
DICT_directions = {'d': [1,0], 'l': [0, -1], 'r': [0, 1], 'u':[-1, 0]}

def check_cango(point1, point2, cnt):
    distance = abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
    if distance > cnt: # too far to go in cnt step
        return False
    
    if abs(distance - cnt)%2 == 1: # can't go in cnt step
        return False
    return True

def solution(n, m, x, y, r, c, k, opt='list'):
    global PATH, PATH_directions, DICT_directions
    
    q = deque()
    q.append([x, y, ""]) # x, y, path
    
    while q:
        x, y, path = q.popleft()
        for d, v in DICT_directions.items():
            nx = x + v[0];
            ny = y + v[1]
            if ny <= 0 or nx <= 0 or nx > n or ny > m:  # out of board
                continue

            if len(path) + 1 > k:  # move more
                return "impossible"

            if len(path) + 1 == k and [nx, ny] == [r, c]:  # arrive destination in k time step
                return path + d

            if check_cango([nx, ny], [r, c], k - (len(path) + 1)):  # can go destination [r, c]
                q.append([nx, ny, path + d])
                break
    return "impossible"