import sys

def dfs(u):
    stack = [u]
    visited[u] = True

    while stack:
        u = stack.pop()
        for i in range(1, N+1):
            if graph[u][i] == 1 and visited[i] == False:
                visited[i] = True
                stack.append(i)

input = sys.stdin.readline

N, M = list(map(int, input().split()))

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u][v] = graph[v][u] = 1

ans = 0

for i in range(1, N+1):
    if visited[i] == False :
        dfs(i)
        ans += 1

print(ans)