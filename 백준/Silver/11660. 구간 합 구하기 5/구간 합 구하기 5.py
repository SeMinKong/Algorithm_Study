
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, M = list(map(int, input().split()))
        arr = []
        for _ in range(N):
            arr.append(list(map(int, input().split())))

        ps = [[0] * (N + 1) for _ in range(N + 1)]
        for r in range(1, N + 1):
            for c in range (1, N + 1):
                ps[r][c] = arr[r - 1][c - 1] + ps[r][c - 1] + ps[r - 1][c] - ps[r - 1][c - 1]

        for _ in range(M):
            x1, y1, x2, y2 = list(map(int, input().split()))
            ans = 0
            ans += ps[x2][y2] - ps[x1 - 1][y2] - ps[x2][y1 - 1] + ps[x1 - 1][y1 - 1]

            print(ans)

if __name__ == "__main__":
    Solve().solve()