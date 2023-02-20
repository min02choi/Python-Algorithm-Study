"""
    [피보나치 수열(메모이제이션 이용)]
"""

def fib_dp_mem(n):
    mem = [None] * (n + 1)
    if (mem[n] == None):
        if (n < 2):
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n - 1) + fib_dp_mem(n - 2)
    return mem[n]


n = 8
print(fib_dp_mem(n))