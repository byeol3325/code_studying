def possible(y, x, n, row):
    for i in range(x):
        if y == row[i]: # 같은 행에 위치
            return False
        if abs(y-row[i]) == x-i: # 같은 대각선
            return False        
    return True

def queen(x, n, row):
    if x == n:
        return 1
    count = 0
    
    for y in range(n):
        if possible(y, x, n, row):
            row[x] = y
            count += queen(x+1, n, row)
    return count

# 열 col |
def solution(n):
    answer = 0
    row = [0]*n
    
    answer = queen(0, n, row)
    return answer