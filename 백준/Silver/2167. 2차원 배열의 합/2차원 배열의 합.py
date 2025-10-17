
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

        K = int(input().strip())
        prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
        for r in range(1, N + 1):
            for c in range(1, M + 1):
                prefix_sum[r][c] = (arr[r - 1][c - 1] +
                                    prefix_sum[r - 1][c] +
                                    prefix_sum[r][c - 1] -
                                    prefix_sum[r - 1][c - 1])
        for _ in range(K):
            i, j, x, y = list(map(int, input().split()))

            result = (prefix_sum[x][y] - prefix_sum[i - 1][y] -
                      prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1])
            print(result)

if __name__ == "__main__":
    Solve().solve()