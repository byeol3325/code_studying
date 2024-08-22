import sys

def square_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def closest_pair(points):
    if len(points) <= 3:
        min_dist = float("inf")
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                min_dist = min(min_dist, square_distance(points[i], points[j]))
        return min_dist

    mid = len(points) // 2
    mid_x = points[mid][0]

    d1 = closest_pair(points[:mid])
    d2 = closest_pair(points[mid:])
    d = min(d1, d2)

    in_strip = []
    for point in points:
        if (point[0] - mid_x) ** 2 < d:
            in_strip.append(point)

    in_strip.sort(key=lambda x: x[1])

    min_strip_dist = d
    for i in range(len(in_strip)):
        for j in range(i + 1, len(in_strip)):
            if (in_strip[j][1] - in_strip[i][1]) ** 2 >= min_strip_dist:
                break
            min_strip_dist = min(min_strip_dist, square_distance(in_strip[i], in_strip[j]))

    return min(d, min_strip_dist)

def solution(n, points):
    points = sorted(points)  # x 좌표에 따라 정렬
    return closest_pair(points)

if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    print(solution(n, points))