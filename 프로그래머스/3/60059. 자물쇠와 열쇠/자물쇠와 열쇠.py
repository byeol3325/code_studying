# key M*M
# lock N*N     M <= N
import numpy as np
import copy

def compare(key, b, x, y, M, N):
    board = copy.deepcopy(b)
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]
    
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True 

def solution(key, lock):
    answer = True
    N = len(lock); M = len(key)
    
    board = [[0]*(M*2+N) for _ in range(M*2+N)]
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    
    for _ in range(4):
        key = (np.rot90(key, k=3)).tolist()
        
        for i in range(N+M):
            for j in range(N+M):
                result = compare(key, board, i, j, M, N)
                if result:
                    return True
        
    return False