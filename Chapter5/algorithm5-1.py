"""
    병합 정렬
"""

def merge(A, left, mid, right):
    k = left
    i = left        # 왼쪽 리스트의 인덱스
    j = mid + 1     # 오른쪽 리스트의 인덱스

    while (i <= mid and j <= right):
        if (A[i] <= A[j]):
            sorted[k] = A[i]
            k += 1
            i += 1
        else:
            sorted[k] = A[j]
            k += 1
            j += 1
    
    # 부분 리스트에 남은 원소 처리
    if (i > mid):       # ?
        sorted[k : k+right-j+1] = A[j : right+1]
    else:
        sorted[k : k+mid-i+1] = A[i : mid+1]
    
    A[left : right+1] = sorted[left : right+1]


def merge_sort(A, left, right):
    if (left < right):
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)


data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
sorted = [0] * len(data)
print("Original: ", data)

merge_sort(data, 0, len(data) - 1)
print("MergeSort: ", data)