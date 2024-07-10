def solution(dirs):
    answer = 0
    
    DIRECTIONS = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    roads = set() # (start_x, start_y, end_x, end_y) / (end_x, end_y, start_x, start_y)
    x,y = 0,0
    
    for d in dirs:
        nd = DIRECTIONS[d]
        nx, ny = x+nd[0], y+nd[1]
        
        if abs(ny) > 5 or abs(nx) > 5: # 격자 밖이니 패스
            continue
        
        if (x, y, nx, ny) not in roads: # 경로
            roads.add((x, y, nx, ny))
            roads.add((nx, ny, x, y))
        x, y = nx, ny
        
    return len(roads)//2