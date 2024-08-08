def solution(array: str)->int:
    answer = 0
    stack = []
    for i in range(len(array)):
        if array[i] == "(" or array[i] == "[":
            stack.append([array[i], 1])
        else:
            if len(stack) == 0:
                return 0

            value = 2 if array[i] == ")" else 3
            if value == 2 and stack[-1][0] != "(":
                return 0

            if value == 3 and stack[-1][0] != "[":
                return 0

            _, v = stack.pop()

            if len(stack) == 0:
                answer += v*value
                continue

            if stack[-1][1] != 1:
                stack[-1][1] += v*value
            else:
                stack[-1][1] = v*value

    if len(stack) != 0:
        return 0
    return answer
   

N = input()
result = solution(N)
print(result)