"""
    [거듭제곱(축소 정복 기법)]
    순환을 반복할수록 문제의 크기가 1/2 비율로 줄어들음
"""

def power(x, n):
    if (n == 0):
        return 1
    elif (n % 2 == 0):
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)

print(power(3, 7))