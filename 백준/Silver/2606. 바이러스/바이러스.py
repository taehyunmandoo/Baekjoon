import sys
n = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
visited = [False] * (n + 1)

graph = [[] for i in range(n + 1)]

# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    #print(v, end= ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for _ in range(edge):
    a,b = map(int, sys.stdin.readline().split())
    graph[a] += [b] # a에 b연결
    graph[b] += [a] # b에 a 연결 -> 양방향
    
dfs(graph, 1, visited)
print(sum(visited) - 1)