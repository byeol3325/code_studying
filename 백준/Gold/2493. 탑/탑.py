import sys

def solution(towers: list):
    """
    N개 높이가 서로 다른 탑을 수평 직선 왼쪽부터 오른쪽 방향으로 차례로 세우기. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신 가능
    :param towers:
    :return:
    """
    N = len(towers)
    stack = [0]
    answers = [0]

    for i in range(1, N):
        while stack and towers[stack[-1]] < towers[i]:
            stack.pop()
        if not stack:
            answers.append(0)
        else:
            answers.append(stack[-1]+1)
        stack.append(i)

    print(*answers)
    return None

if __name__ == "__main__":
    # sys.stdin = open("2493.txt")
    N = int(input())
    towers = list(map(int, input().split()))
    solution(towers)