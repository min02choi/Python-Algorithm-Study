# algorithm 3-6 깊이 우선 탐색

def dfs(graph, start, visited):
    if (start not in visited):
        visited.add(start)
        print(start, end="")
        nbr = graph[start] - visited    # 차집합 연산
        # print(nbr)

        for v in nbr:
            dfs(graph, v, visited)


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

print("DFS: ", end="")
dfs(mygraph, "A", set())
print()