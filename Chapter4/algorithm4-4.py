"""
    위상정렬
"""


def topological_sort(graph):
    inDeg = {}          # {정점: 진입차수} 저장 딕셔너리

    # 정점을 초기화
    for v in graph:     # 딕셔너리의 키값이 나오게 됨
        inDeg[v] = 0    # 초기화

    # 진입차수 증가
    for i in graph:
        for j in graph[i]:
            inDeg[j] += 1   # 진입차수 1 증가

    vlist = []      # 진입차수가 0인 정점을 모아두는 리스트
    for v in graph:
        if inDeg[v] == 0:       # 진입차수가 0인 정점
            vlist.append(v)     # 리스트에 넣음

    while (vlist):
        v = vlist.pop()
        print(v, end=" ")

        for u in graph[v]:
            inDeg[u] -= 1       # 정점이 하나 빠졌으므로 각 정점별 진입차수 갱신
            if (inDeg[u] == 0):     # 진입차수가 0이 되었다면
                vlist.append(u)     # 리스트에 삽입



mygraph = {
    "A": {"C", "D"},
    "B": {"D", "E"},
    "C": {"D", "F"},
    "D": {"F"},
    "E": {"F"},
    "F": { },
}

print("topological sort: ")
topological_sort(mygraph)

print()