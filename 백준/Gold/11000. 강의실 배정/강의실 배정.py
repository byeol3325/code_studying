import sys
import heapq as hq

def solution():
    N = int(input())
    classes = [list(map(int, input().split())) for _ in range(N)] # 강의 시간 시작 / 끝
    classes.sort()

    rooms = [classes[0][1]]
    for i in range(1, N):
        if rooms[0] <= classes[i][0]:
            hq.heappop(rooms)
        hq.heappush(rooms, classes[i][1])
        #print(rooms)

    print(len(rooms))
    return None


if __name__ == "__main__":
    #sys.stdin = open("11000.txt")
    solution()