# 문제 18(2)
# 음? 뭐야 왜 이렇게 어려워
# 미완

class Node:
    def __init__ (self, data, next=None):
        self.data = data
        self.link = next

def printList(head, msg = "생성된 연결 리스트:"):
    print(msg, end = "")
    n = head
    while (n != None):
        print(n.data, end = "->")
        n = n.link
    print()

head = None     # 어디로 연결?
tail = None     # 데이터 저장 본체

n = int(input("노드의 개수: "))

for i in range(n):
    data = int(input("노드 #%d 데이터: " %(i + 1)))

    temp = Node(data, None)
    if (head == None):
        head = tail = n
    else:
        tail.link = n
        tail = n

printList(head)
