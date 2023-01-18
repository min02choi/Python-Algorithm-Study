# 문제 18(1)

n = int(input("노드의 개수: "))
nums = []

for i in range(1, n + 1):
    nums.append(int(input("노드 #%d 데이터: " %i)))

print("리스트의 내용", nums)