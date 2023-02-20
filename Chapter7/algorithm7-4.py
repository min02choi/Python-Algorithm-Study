"""
    [이항계수 계산(동적 계획법)]
"""


def bino_coef_dp(n, k):
    C = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):              # i: 0 ~ n
        for j in range(min(i, k) + 1):  # j: 0 ~ 
            if (j == 0 or j == i):
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    print(C)
    return C[i][j]

print(bino_coef_dp(5, 3))
