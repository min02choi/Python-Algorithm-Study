"""
    [최근접 쌍의 거리(억지기법)]
    이중루프를 사용하여 가능한 모든 점의 쌍에 대해서 거리 계산
"""

import math

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


p = [ (2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4) ]
print("최근접 거리: ", closest_pair(p))