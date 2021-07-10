from collections import deque
import sys

K = int(sys.stdin.readline())
answer = ["" for _ in range(K)]

def bfs(graph,v,visited):
    que = deque([v])
    visited[v] = 1
    while que:
        node = que.popleft()
        graph[node].sort()
        for n in graph[node]:
            if visited[n]==0:
                que.append(n)
                visited[n] = (-1)*visited[node]
            else:
                if visited[n]==visited[node]:
                    return True
    return False

def solution(k):
    N,M = map(int,sys.stdin.readline().split())
    visited = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    answer[k] = "YES"
    for i in range(M):
        s,t = map(int,sys.stdin.readline().split())
        graph[s].append(t)
        graph[t].append(s)
    for i in range(1,N+1):
        if visited[i] == 0:
            if bfs(graph,i,visited):
                answer[k] = "NO"
                break

for i in range(K):
    solution(i)

print('\n'.join(answer))