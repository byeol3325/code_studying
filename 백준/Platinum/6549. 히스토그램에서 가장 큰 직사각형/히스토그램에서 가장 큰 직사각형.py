def solution(histogram):
    histogram = histogram[1:]
    histogram.append(0)  # 끝에 높이 0을 추가하여 남은 모든 막대를 처리하게 합니다.
    stack = []
    max_area = 0

    for i in range(len(histogram)):
        while stack and histogram[stack[-1]] > histogram[i]:
            height = histogram[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1: # 끝!
        break

    print(solution(arr))