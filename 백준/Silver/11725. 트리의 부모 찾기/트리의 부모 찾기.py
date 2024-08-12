import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

# 그래프 생성
graph =[[] for i in range(N+1)]

# 그래프 연결
for i in range(N-1):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
parents = [False]* (N + 1)
    
def dfs(node):
    for i in graph[node]:
        if parents[i] == 0:
            parents[i] = node
            dfs(i)
dfs(1)

for i in range(2, N+1):
    print(parents[i])