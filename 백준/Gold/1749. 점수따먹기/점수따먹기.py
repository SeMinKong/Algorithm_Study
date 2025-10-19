
from re import L


class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, M = list(map(int, input().split()))
        arr = [list(map(int, input().split())) for _ in range(N)]
        ps = [[0] * (M + 1) for _ in range(N + 1)]
        ans = -10**18
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                ps[r][c] = arr[r - 1][c - 1] + ps[r - 1][c] + ps[r][c - 1] - ps[r - 1][c - 1]

        for xi in range(1, N + 1):
            for yi in range(1, M + 1):
                for xj in range(xi, N + 1):
                    for yj in range(yi, M + 1):
                        cur = ps[xj][yj] - ps[xj][yi - 1] - ps[xi - 1][yj] + ps[xi - 1][yi - 1]
                        ans = max(ans, cur)
        print(ans)
if __name__ == "__main__":
    Solve().solve()