"""
    [0-1 배낭 채우기 알고리즘(동적 계획법)]
    이해하기 어렵다
"""


def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]   # 배낭 초기화(기반상황 포함)

    for i in range(1, n + 1):
        for w in range(1 + W + 1):
            if (wt[i - 1] > w):     # 물건의 무게가 가방 용량 초과
                A[i][w] = A[i - 1][w]
            else:                   # 물건의 무게가 가방 용량 초과 X
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][W]


W = 18                                  # 가방의 용량
wt = [2, 5, 8, 4, 7, 6]                 # 물건의 무게
val = [60, 100, 190, 120, 200, 150]     # 물건의 가치
n = len(val)                            # 물건의 개수

print("0-1 배낭문제(동적 계획): ", knapSack_dp(W, wt, val, n))
