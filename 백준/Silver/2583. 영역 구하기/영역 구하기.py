from collections import deque
class Solve:
    def __init__(self):
        pass
        
    def solve(self):
        import sys
        input = sys.stdin.readline

        #일단 직사각형 영역을 다 visited처리. 그런다음 0,0부터 bfs시작. 영역 확인. 
        grid_y, grid_x, numRect = list(map(int, input().split()))
        visited = set()
        area = 0
        sizes = []

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited.add((x, y))
            size = 1
            while q:
                x, y = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    if 0 <= x+dx < grid_x and 0 <= y+dy < grid_y and (x+dx, y+dy) not in visited:
                        visited.add((x+dx, y+dy))
                        q.append((x+dx, y+dy))
                        size += 1
            return size

        for _ in range(numRect):
            lbx, lby, rtx, rty = list(map(int, input().split()))
            for x in range(lbx, rtx):
                for y in range(lby, rty):
                    visited.add((x, y))
        
        for x in range(grid_x):
            for y in range(grid_y):
                if(x, y) not in visited:
                    sizes.append(bfs(x, y))
                    area += 1

        print(area)
        sizes.sort()
        print(*sizes)

if __name__ == "__main__":
    Solve().solve()