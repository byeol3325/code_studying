def solution(n):
    #answer = 1

    factorial = [1 for i in range(2*n+1)]

    for i in range(2, 2*n+1):
        factorial[i] = int(factorial[i-1] * i)
    
    answer = int(factorial[2*n] / (factorial[n] * factorial[n+1]))

    return answer