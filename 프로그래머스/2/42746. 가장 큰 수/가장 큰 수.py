def solution(numbers):
    answer = ''
    
    numbers = sorted(numbers, reverse=True, key=lambda x:str(x)*3)
    
    for num in numbers:
        answer += str(num)
    return str(int(answer))