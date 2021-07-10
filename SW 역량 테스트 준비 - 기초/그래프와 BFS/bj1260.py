from collections import deque

N,M,v = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    s,t = map(int,input().split())
    graph[s].append(t)
    graph[t].append(s)


def dfs(graph,v,visited):
    visited.append(v)
    graph[v].sort()
    for node in graph[v]:
        if node not in visited:
            dfs(graph,node,visited)
    return visited


def bfs(graph,v,visited):
    que = deque([v])
    visited.append(v)
    while que:
        node = que.popleft()
        graph[node].sort()
        for n in graph[node]:
            if n not in visited:
                que.append(n)
                visited.append(n)
    return visited

visited = []
print(*dfs(graph,v,visited))
visited = []
print(*bfs(graph,v,visited))
