
#### Sxx 구하기 #####################
def get_sxx():
    a = float(input())
    b = float(input())
    n = int(input())

    first = a
    sec = (b * b) / n

    print(first - sec)
    return first - sec

###############################

# 2.1.2) k 구하기
def get_k():
    a = float(input())
    b = float(input())
    n = int(input())

    sxx = float(input())
    # sxx = float(get_sxx())

    temp = a - b / n

    print("x-xbar: ", temp)
    print("sxx: ", sxx)
    print("answer: ", temp / sxx)


# a = float(input())
# print(-1.02 + 0.05138 * a)  # 2.3.1

def question1():
    x_each = [ 116.37, 82.77, 110.68, 97.50, 115.88, 80.19, 125.24, 116.15, 117.36, 93.31, 107.46, 122.30 ]
    y_each = [ 5.6, 3.2, 4.5, 4.2, 5.2, 2.7, 4.8, 4.9, 4.7, 4.1, 4.4, 5.4 ]

    y_chu = []  # y의 추정량 총 12개
    e = []      # y_each - y_chu

    # [2.1.3] y의 추정량 구하기
    for i in range(12):
        y_chu.append(-1.02 + 0.05138 * x_each[i])

    # [2.1.3] 오차값(y값 - y의 추정량) 구하기
    for i in range(12):
        e.append(y_each[i] - y_chu[i])
    # print("y_chu: ", y_chu)
    # print("e:", e)

    # [2.1.3] SSE구하기(오차 제곱의 합)
    e_square = []
    for i in range(12):
        e_square.append(e[i]**2)
    print(sum(e_square))

    # [2.1.4] SSE 구하기
    # print(7.98249 - 0.05138 * 129.56525)

    # [2.1.5] 표준편차 추정량의 제곱 구하기
    # print(1.326 / (12 - 2))

    # [2.1.6] 오차의 합(= 0)
    print(sum(e))


####################################################
def question2_3_1():
    # [2.3.1] 다 구하기
    # Sxx구하기
    sxx = 700759 - 3450.2**2 / 2
    sxy = 86735.5 - 3450.2 * 426 / 2
    syy = 10821 - 426**2 / 2

    # print(sxx, sxy)
    beta1 = sxy / sxx
    # print(beta1)

    x = [ 194.5, 212.2 ]
    y = [ 20.79, 30.06 ]

    x_avg = sum(x) / len(x)
    y_avg = sum(y) / len(y)

    beta0 = y_avg - beta1 * x_avg
    # print(beta0)
    # print(syy)

    sse = syy - beta1 * sxy
    # print(sse)

    y_chu = []
    for i in range(2):
        y_chu.append(beta0 + beta1 * x[i])
    print(y_chu)

    e = [y[i] - y_chu[i] for i in range(2)]
    print(e)


import math

# [2.3.2] 다 구하기
# Sxx구하기
sxx = 700759 - 3450.2**2 / 2
syy = 331751.6 - 2373.29**2 / 2
sxy = 482141.5 - 3450.2 * 2373.29 / 2
print("Sxx:", sxx, " Syy:", syy, " Sxy:", sxy)

beta1 = sxy / sxx
print("beta1:", beta1)

x = [ math.log10(194.5), math.log10(212.2) ]    # log값
y = [ 20.79, 30.06 ]

x_avg = sum(x) / len(x)
y_avg = sum(y) / len(y)
print("x_avg:", x_avg)
print("y_avg:", y_avg)

beta0 = y_avg - beta1 * x_avg
print("beta0:", beta0)
# print(syy)

sse = syy - beta1 * sxy
print("SSE:", sse)

y_chu = []
for i in range(2):
    y_chu.append(beta0 + beta1 * x[i])
print("y의 추정량:", y_chu)

e = [y[i] - y_chu[i] for i in range(2)]
print("잔차(e):", e)
