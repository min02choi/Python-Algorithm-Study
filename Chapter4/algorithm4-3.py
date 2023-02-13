"""
    삽입 정렬
    1. 키를 잡음
    2. 키를 정렬 된 곳에 집어넣음(왼쪽으로 정렬)
"""


def insertion_sort(A):
    n = len(A)

    for i in range(1, n):   # 키를 잡는 과정
        key = A[i]
        j = i - 1

        # 왼쪽으로 나아가면서 정렬 -> key값이 A[j]보다 적을 시 종료
        while (j >= 0 and A[j] > key):
            A[j + 1] = A[j]     # 한 칸 우측으로 이동
            j -= 1
        A[j + 1] = key


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

print("Original: ", data)
insertion_sort(data)
print("Insertion: ", data)