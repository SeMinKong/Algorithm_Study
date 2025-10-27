
class Solve:
    def __init__(self):
        pass

    def dfs(self, node, visited, route):
        for next in range(len(visited)):
            if route[node][next] == 1 and visited[next] == 0:
                visited[next] = 1
                self.dfs(next, visited, route)


    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())

        ans = [[0] * N for _ in range(N)]

        route = [list(map(int, input().split())) for _ in range(N)]

        for i in range(N):
            visited = [0] * N
            self.dfs(i, visited, route)
            ans[i] = visited
    
        for row in ans:
            print(*row)
        

if __name__ == "__main__":
    Solve().solve()