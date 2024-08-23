import sys

def solution(N: int, L: int, info: list):
    """
    N개 물 웅덩이 (웅덩이는 겹치지 않아요!)
    :param N: N개 웅덩이
    :param L: 널빤지 길이
    :param info: 웅덩이 정보
    :return: print 최소 널빤지 갯수
    """
    cnt = 0
    info.sort()

    e = 0
    for i in range(N):
        if e <= info[i][0]:
            e = ((info[i][1]-info[i][0])//L) * L + info[i][0] if (info[i][1]-info[i][0])%L == 0 else ((info[i][1]-info[i][0])//L+1) * L + info[i][0]
            cnt += (info[i][1]-info[i][0])//L if (info[i][1]-info[i][0])%L == 0 else (info[i][1]-info[i][0])//L+1
            #print(s, e, cnt)
        elif info[i][0] <= e <= info[i][1]:
            #print(e, end=" ")
            cnt += (info[i][1] - e) // L if (info[i][1] - e) % L == 0 else (info[i][1] - e) // L + 1
            e = ((info[i][1]-e)//L) * L + e if (info[i][1]-e)%L == 0 else ((info[i][1]-e)//L+1) * L + e
            #print(e, cnt, )
        #print(e)
    print(cnt)
    return None

if __name__ == "__main__":
    #sys.stdin = open("1911.txt")
    N, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    solution(N, L, info)