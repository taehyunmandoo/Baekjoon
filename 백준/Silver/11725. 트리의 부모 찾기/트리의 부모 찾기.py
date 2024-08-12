import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
 
# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited = [False]*(N+1) 
 
def dfs(node):
    for i in graph[node]:
        if not(visited[i]): 
            visited[i] = node 
            dfs(i)
 
dfs(1)
 
for x in range(2, N+1):
    print(visited[x]) 
