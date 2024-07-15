from collections import deque

def show_board(board: list):
    for i in range(len(board)):
        print(board[i])
    return None

def solution(m, n, board):
    answer = 0
    # borad[m][n]
    for i in range(m):
        board[i] = list(board[i])
    
    def one_cycle():
        nonlocal answer
        locations = []
        visited = [[0]*n for _ in range(m)]
        do = answer
        # 위치 찾기
        for i in range(m-1):
            for j in range(n-1):
                if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+1][j+1]):
                    locations.append([i,j])
        
        # 비우기
        for loc in locations:
            [y, x] = loc
            
            if board[y][x] != " ":
                board[y][x] = " "
                answer += 1
            if board[y+1][x] != " ":
                board[y+1][x] = " "
                answer += 1
            if board[y][x+1] != " ":
                board[y][x+1] = " "
                answer += 1
            if board[y+1][x+1] != " ":
                board[y+1][x+1] = " "
                answer += 1
        
        # 내리기
        for j in range(n):
            idx = -1
            for i in range(m-1, -1, -1):
                if board[i][j] == " " and idx == -1:
                    idx = i
                    continue
                
                if board[i][j] != " "  and idx != -1:
                    board[idx][j] = board[i][j]
                    board[i][j] = " "
                    idx -= 1
        
        if answer == do:
            return 0
        return 1
    
    
    while True:
        go = one_cycle()
        if go == 0:
            break
    
    return answer