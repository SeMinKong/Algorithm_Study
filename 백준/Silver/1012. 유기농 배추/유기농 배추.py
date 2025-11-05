from collections import defaultdict, deque
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            graph[x][y] = 0
            while q:
                x, y = q.popleft()
                directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dr, dc in directions:
                    if  0 <= x+dr < row and 0 <= y+dc < col and graph[x+dr][y+dc] == 1:
                        graph[x+dr][y+dc] = 0
                        q.append((x+dr, y+dc))


        T = int(input().strip())
        for _ in range(T):
            col, row, cabbage= list(map(int, input().split()))
            graph = [[0]*col for _ in range(row)]
            for _ in range(cabbage):
                x, y = list(map(int, input().split()))
                graph[y][x] = 1

            ans = 0
            for r in range(row):
                for c in range(col):
                    if graph[r][c] == 1:
                        bfs(r, c)
                        ans += 1
            
            print(ans)

if __name__ == "__main__":
    Solve().solve()