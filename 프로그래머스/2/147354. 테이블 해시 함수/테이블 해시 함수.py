def solution(data, col, row_begin, row_end):
    answer = -1
    data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        bitwise = 0
        for d in data[i-1]:
            bitwise += d%i
        
        if answer == -1:
            answer = bitwise
        else:
            answer = answer ^ bitwise
    return answer