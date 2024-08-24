import sys
import heapq

def solution(n: int, lines: list, d: int):
    # 모든 선분을 집과 사무실의 위치로 정렬
    valid_lines = []
    for h, o in lines:
        start, end = min(h, o), max(h, o)
        if end - start <= d:  # 길이가 d 이하인 경우에만 고려
            valid_lines.append((start, end))

    if len(valid_lines) <= 1: # 1개 이하면 끝
        print(len(valid_lines))
        return None

    # 끝점을 기준으로 정렬
    valid_lines.sort(key=lambda x: x[1])

    max_count = 0
    current_heap = []
    
    for start, end in valid_lines:
        # 현재 힙에서 가장 시작점이 작은(=가장 멀리 떨어져있음) 애가 d거리 이상 차이남
        while current_heap and current_heap[0] < end - d:
            heapq.heappop(current_heap)
        
        # 현재 선분을 힙에 추가함
        heapq.heappush(current_heap, start)
        
        # 최대 인원 수 갱신
        max_count = max(max_count, len(current_heap))

    print(max_count)
    return None
if __name__ == "__main__":
    #sys.stdin = open("13334.txt")
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    d = int(input())
    solution(n, lines, d)