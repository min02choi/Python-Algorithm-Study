# 문제 2.3

def binary_digit(n):
    cnt = 0
    while (n > 0):
        cnt += 1
        n //= 2
    return cnt

num = int(input())

print(binary_digit(num))