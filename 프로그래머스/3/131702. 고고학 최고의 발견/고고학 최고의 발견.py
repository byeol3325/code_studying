from copy import deepcopy

DIRECTIONS = {-1:[0,0], 0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]} # 0 ~ 3, 12시 ~ 9시. 시계방향

def product(arr: list, n: int):
    result = []
    one = []
    def make(array: list):
        nonlocal arr, n
        for i in range(len(arr)):
            array.append(arr[i])
            if len(array) == n:
                result.append(deepcopy(array))
            else:
                make(array)
            array.pop()
    make(one)
    return result

def turn(board: list, loc: list, cnt: int):
    global DIRECTIONS
    n = len(board)
    for k, v in DIRECTIONS.items():
        dr, dc = v
        nr, nc = loc[0] + dr, loc[1] + dc
        if (0 <= nr < n) and (0 <= nc < n):
            board[nr][nc] = (board[nr][nc] + cnt)%4
    return None
    
def solution(clockHands):
    answer = 8 * 8 * 3 # 최대 돌렸을 때
    n = len(clockHands)
    
    end_board = [[0]*n for _ in range(n)]
    for one_case in product([0,1,2,3], n): # 첫 줄 돌리는 방법
        cnt = 0
        one_board = deepcopy(clockHands)
        
        for j, one_turn in enumerate(one_case):
            turn(one_board, [0, j], one_turn)
            cnt += one_turn
        
        for i in range(1, n):
            for j in range(n):
                if one_board[i-1][j] != 0:
                    needed_turn = (4-one_board[i-1][j])%4
                    turn(one_board, [i,j], needed_turn)
                    cnt += needed_turn
        
        if all(x == 0 for x in one_board[-1]):
            answer = min(answer, cnt)
    
    # 최소한 조작으로 해결
    return answer