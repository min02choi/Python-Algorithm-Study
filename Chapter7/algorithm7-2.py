"""
    [피보나치 수열(테이블화 이용)]
"""


def fib_dp_tab(n):
    f = [None] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    
    return f[n]

n = 8
print(fib_dp_tab(n))
