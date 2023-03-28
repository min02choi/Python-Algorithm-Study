
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
a = float(input())
b = float(input())
n = int(input())

sxx = float(input())
# sxx = float(get_sxx())

temp = a - b / n

print("x-xbar: ", temp)
print("sxx: ", sxx)
print("answer: ", temp / sxx)

