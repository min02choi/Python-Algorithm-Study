sum = 0
for i in range(4):
    sum += int(input("과목 %d의 점수는?: " %(i + 1)))

print("4과목의 평균은 %0.2f점 입니다" %(sum / 4))

