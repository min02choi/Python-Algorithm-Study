"""
    [피보나치 수열(분할 정복)]
    - 중복적인 호출이 너무 심한 문제가 있음
    - 시간 복잡도: O(2^n)
"""

def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)