"""
    [축소 정복 기법을 이용한 k번쨰 작은 수 찾기]
"""

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]

    while(low <= high):     # low와 high의 역전 전까지
        while (low <= right and A[low] < pivot):
            low += 1
        while (high >= left and A[high] > pivot):
            high -= 1
        if (low < high):    # 진전이 끝나면 항목 교환
            A[low], A[high] = A[high], A[low]
    
    A[left], A[high] = A[high], A[left]     # 피벗은 A[left]에 들어있음

    return high

def quick_select(A, left, right, k):    # 배열, 왼쪽 인덱스, 오른쪽 인덱스, 찾는 번째 수
    pos = partition(A, left, right)     # 피벗의 위치(인덱스)

    if (pos + 1 == left + k):       # 피벗이 k번째 찾는 수 일때(일치)
        return A[pos]
    elif (pos + 1 > left + k):      # 피벗이 찾는 수보다 클 경우 --> 답은 왼쪽 부분리스트에
        return quick_select(A, left, pos - 1, k)
    else:                           # 피벗이 찾는 수보다 작을 경우 --> 답은 오른쪽 부분리스트에
        return quick_select(A, pos + 1, right, k - (pos + 1 - left))


array = [ 12, 3, 5, 7, 4, 19, 26, 23, 15 ]
print("입력 테스트: ", array)

n = len(array)

print("[정렬기법] 3번째 작은 수: ", quick_select(array, 0, n - 1, 3))
print("[정렬기법] 6번째 작은 수: ", quick_select(array, 0, n - 1, 6))