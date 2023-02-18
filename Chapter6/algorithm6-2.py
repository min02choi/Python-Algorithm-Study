"""
    [카운팅 정렬]
"""

def counting_sort(A):
    output = [0] * len(A)
    count = [0] * MAX_VAL       # 각 숫자의 빈도를 저장

    for i in A:                 # 각 숫자별 빈도 계산
        count[i] += 1
        # print(count)
    
    for i in range(MAX_VAL):
        count[i] += count[i - 1]
        print(count)
    print()

    for i in range(len(A)):
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
        print(count)

    for i in range(len(A)):
        A[i] = output[i]


MAX_VAL = 10
data = [1, 4, 1, 2, 7, 5, 2]

print("Original: ", data)
counting_sort(data)

print("Counting: ", data)
