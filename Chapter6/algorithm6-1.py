"""
    [기수 정렬]
    각 버킷은 큐로 구성되어 있음
"""


from queue import Queue
import random

BUCKETS = 10        # 버킷의 수
DIGITS = 4          # 최대 자릿수

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())      # 버킷의 개수만큼 큐 삽입
    
    n = len(A)      # 항목의 수
    factor = 1      # 자릿수
    
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % 10].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= 10
        print("step", d + 1, A)


data = []

for i in range(10):
    data.append(random.randint(1, 9999))
print("Original: ", data)

radix_sort(data)
print("Radix: ", data)
