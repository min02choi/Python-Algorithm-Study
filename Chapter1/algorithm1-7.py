# 알고리즘 1.7
# 최대 공약수를 구하는 유클리드 알고리즘
# 01.16

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


print(gcd(60, 28))
