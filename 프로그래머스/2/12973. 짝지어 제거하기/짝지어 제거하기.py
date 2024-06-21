# 짝지어 제거하기.
# 소문자로 이루어진 문자열.
# 같은 알파벳이 2개 붙어 있는 짝 찾고 지우고 앞뒤로 붙임. 
# baabaa -> bbaa -> aa -> 모두 제거할 수 있으면 1 / 0
def solution(s):
    answer = 0
    stack = []
    n = len(s)
    
    for i in range(n):
        if not stack:
            stack.append(s[i])
            continue
        
        if s[i] == stack[-1]:
            stack.pop()
            continue
        else:
            stack.append(s[i])
            continue

    if stack:
        return 0
    else:
        return 1
    return answer