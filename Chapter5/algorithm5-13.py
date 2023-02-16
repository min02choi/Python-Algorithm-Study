"""
    [피보나치 수열(반복 구조)]
"""

def fib_iter(n):
    if (n < 2):
        return n
    last = 0
    current = 1

    for i in range(2, n + 1):
        temp = current
        current += last
        last = temp

    return current

print(fib_iter(8))