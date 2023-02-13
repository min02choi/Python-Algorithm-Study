import queue

def bfs(graph, start):
    visited = { start }     # 방문 했음
    que = queue.Queue()
    que.put(start)

    while not que.empty():
        v = que.get()
        print(v, end="")
        nbr = graph[v] - visited    # 인접정점에서 이미 방문한 접점을 제거

        for u in nbr:
            visited.add(u)
            que.put(u)
        
        print(visited)


mygraph = {
    "A" : {"B", "C"}, 
    "B" : {"A", "D"},
    "C" : {"A", "D", "E"},
    "D" : {"B", "C", "F"},
    "E" : {"C", "G", "H"},
    "F" : {"D"},
    "G" : {"E", "H"},
    "H" : {"E", "G"}
}    

print("BFS: ", end="")
bfs(mygraph, "A")
print()