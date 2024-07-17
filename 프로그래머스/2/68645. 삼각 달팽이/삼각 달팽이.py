def show_matrix(matrix: list):
    for i in range(len(matrix)):
        print(matrix[i])
    return None

def solution(n):
    triangle = [[0]*i for i in range(1, n+1)]
    
    start = [0, 0]
    num = 1
    while True:
        if n < 0:
            break
        
        for i in range(n): # 왼 대각선
            triangle[start[0]+i][start[1]+0] = num
            num += 1
        for i in range(1, n): # 오른 대각선
            triangle[start[0]+n-1][start[1]+i] = num
            num += 1
        for i in range(1, n-1): # 아래
            triangle[start[0]+n-1-i][start[1]+n-1-i] = num
            num += 1
        
        n -= 3
        start[0] += 2
        start[1] += 1
    
    answer = []
    for i in range(len(triangle)):
        answer += triangle[i]
    return answer