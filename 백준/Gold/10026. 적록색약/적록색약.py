from collections import deque
from re import L
class Solve:
    def __init__(self):
        pass
        
    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())
        painting = [list(input().strip()) for _ in range(N)]
        curColor = "R"
        visited = set()
        area = 0
        areaBlind = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if 0 <= r+dr < N and 0 <= c+dc < N and painting[r+dr][c+dc] == curColor and (r+dr, c+dc) not in visited:
                        visited.add((r+dr, c+dc))
                        q.append((r+dr, c+dc))
                    
        for r in range(N):
            for c in range(N):
                if( painting[r][c] in ("R", "G", "B") and 
                    (r, c) not in visited):
                    curColor = painting[r][c]
                    bfs(r, c)
                    area += 1

        visited.clear()

        for r in range(N):
            for c in range(N):
                if(painting[r][c] == "G"):
                    painting[r][c] = "R"

        for r in range(N):
            for c in range(N):
                if( painting[r][c] in ("R", "B") and 
                    (r, c) not in visited):
                    curColor = painting[r][c]
                    bfs(r, c)
                    areaBlind += 1
        
        print(f"{area} {areaBlind}")

if __name__ == "__main__":
    Solve().solve()