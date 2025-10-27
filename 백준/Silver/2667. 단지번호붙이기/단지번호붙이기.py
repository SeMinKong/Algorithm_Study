
class Solve:
    def __init__(self):
        pass
    
    def dfs(self, r, c, houses, visited):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = [(r, c)]
        visited[r][c] = True
        size = 0
        while stack:
            r, c = stack.pop()
            size += 1
            for dr, dc in directions:
                nxtr, nxtc = dr+r, dc+c
                if 0 <= nxtr < len(visited) and 0 <= nxtc < len(visited):
                    if not visited[nxtr][nxtc] and houses[nxtr][nxtc] == 1:
                        visited[nxtr][nxtc] = True
                        stack.append((nxtr, nxtc))
        
        return size
            

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())
        houses = [list(map(int, list(input().strip()))) for _ in range(N)]
        
        sizes = []
        visited = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if houses[r][c] == 1 and not visited[r][c]:
                    sizes.append(self.dfs(r, c, houses, visited))
        
        sizes.sort()
        print(len(sizes))
        for i in range(len(sizes)):
            print(sizes[i])
        

if __name__ == "__main__":
    Solve().solve()