"""
    [최근접 쌍의 거리]
"""

import math

# 3.4장 알고리즘
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(p):
    n = len(p)
    mindest = float("inf")

    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = distance(p[i], p[j])
            if (dist < mindest):
                mindest = dist

    return mindest


def strip_closest(P, d):
    n = len(P)
    d_min = d
    P.sort(key=lambda point: point[1])      # y좌표를 기준으로 정렬

    for i in range(n):
        j = i + 1

        while (j < n and (P[j][i] - P[i][1]) < d_min):
            dij = distance(P[i], P[j])
            if (dij < d_min):
                d_min = dij
            j += 1
    
    return d_min

def closest_pair_dist(P, n):
    if (n <= 3):
        return closest_pair(P)      # 3.4장 알고리즘
    mid = n // 2
    mid_x = P[mid][0]

    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n - mid)
    d = min(dl, dr)     # 좌, 우 중 더 짧은 거리

    Pm = []     # x좌표가 d이내인 점의 좌표들의 집합
    for i in range(n):
        if (abs(P[i][0] - mid_x) < d):
            Pm.append(P[i])

    ds = strip_closest(Pm, d)
    return min(d, ds)


p = [ (2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4) ]
p.sort(key=lambda point: point[0])

print("가장 가까운 두 점의 거리: ", closest_pair_dist(p, len(p)))