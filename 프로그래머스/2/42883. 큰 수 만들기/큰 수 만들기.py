# K개 수 제거할 때 얻을 수 있는 가장 큰 수
# 1924, k=2 => 94
# 1231234, k=3 => 3234

def solution(number, k):
    answer = []
    n = len(number); end = n
    number = list(number)
    
    for i in range(n):
        if not answer :
            answer.append(number[i])
            continue
        
        while k > 0 and answer and answer[-1] < number[i]:
            answer.pop()
            k-=1
        answer.append(number[i])
        
        if k == 0:
            break
    
    answer += number[i+1:]
    if k != 0:
        answer = answer[:-k]
    answer = list(map(str, answer))
    answer = ''.join(answer)
    
    return answer