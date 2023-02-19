"""
    선형 조사법의 삽입 알고리즘
"""


# 해시 함수
def hashFn(key):
    return key % M

# 알고리즘 6.6: 삽입
def lp_insert(key):
    id = hashFn(key)    # 해당 값의 키 값을 구함
    count = M

    while (count > 0 and (table[id] != None and table[id] != 1)):  # 테이블이 차 있는 경우
        id = (id + 1 + M) % M
        count -= 1
    
    if (count > 0):
        table[id] = key
    
    return

# 알고리즘 6.7: 탐색
def lp_search(key):
    id = hashFn(key)
    count = M

    while (count > 0):
        if (table[id] == None):
            return None
        if (table[id] == key and table[id] != -1):
            return table[id]
        id = (id + 1 + M) % M
        count -= 1
    
    return None

# 알고리즘 6.8: 삭제
def lp_delete(key):
    id = hashFn(key)
    count = M

    while (count > 0):
        if (table[id] == None):
            return
        if (table[id] != -1 and table[id] == key):
            table[id] = -1      # 삭제한 버킷을 -1로 처리
            return
        id = (id + 1 + M) % M
        count -= 1



M = 13
table = [None] * M

arr = [45, 27, 88, 9, 71, 60, 46, 38, 24]

for i in arr:
    lp_insert(i)
    print(i, "삽입:", table)

lp_delete(60)
print("60 삭제: ", table)

print("46 탐색:", lp_search(46))
