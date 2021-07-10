from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    s,t = map(int,sys.stdin.readline().split())
    graph[s].append(t)
    graph[t].append(s)

count = 0
comp = [i for i in range(1,N+1)]
visited = [0]*(N+1)

def bfs(graph,v,visited):
    que = deque([v])
    visited[v] = 1
    while que:
        node = que.popleft()
        graph[node].sort()
        for n in graph[node]:
            if visited[n] != 1:
                que.append(n)
                visited[n] = 1

for i in range(1,N+1):
    if visited[i] == 0:
        bfs(graph,i,visited)
        count += 1

print(count)
