import copy

def change_row(matrix, idx):
    for i in range(len(matrix[0])):
        matrix[idx][i] = (matrix[idx][i] + 1) % 2

def change_col(matrix, idx):
    for i in range(len(matrix)):
        matrix[i][idx] = (matrix[i][idx] + 1) % 2

def check_row_flip_needed(beginning, target, row):
    return beginning[row][0] != target[row][0]

def check_col_flip_needed(beginning, target, col):
    return beginning[0][col] != target[0][col]

def solution(beginning, target):
    n, m = len(target), len(target[0])
    original_beginning = copy.deepcopy(beginning)

    min_flips = float('inf')
    
    # 초기 행의 모든 경우의 수를 시도
    for row_flip in [True, False]:
        beginning = copy.deepcopy(original_beginning)
        flips = 0
        
        if row_flip:
            change_row(beginning, 0)
            flips += 1
        
        for i in range(1, n):
            if check_row_flip_needed(beginning, target, i):
                change_row(beginning, i)
                flips += 1
        
        for j in range(m):
            if check_col_flip_needed(beginning, target, j):
                change_col(beginning, j)
                flips += 1
        
        if beginning == target:
            min_flips = min(min_flips, flips)
    
    # 초기 열의 모든 경우의 수를 시도
    for col_flip in [True, False]:
        beginning = copy.deepcopy(original_beginning)
        flips = 0
        
        if col_flip:
            change_col(beginning, 0)
            flips += 1
        
        for i in range(n):
            if check_row_flip_needed(beginning, target, i):
                change_row(beginning, i)
                flips += 1
        
        for j in range(1, m):
            if check_col_flip_needed(beginning, target, j):
                change_col(beginning, j)
                flips += 1
        
        if beginning == target:
            min_flips = min(min_flips, flips)

    return min_flips if min_flips != float('inf') else -1