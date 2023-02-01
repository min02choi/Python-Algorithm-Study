print("Hello")

num = int(input("몇 단을 출력할까요?: "))

print(num, "단을 출력하겠습니다.")

for i in range(1, 10):
    print(num, " * ", i, " = ", num * i)

print("오 된다")

x = 1
y = 2
x1, y1 = y, x

print(x, y, x1, y1)