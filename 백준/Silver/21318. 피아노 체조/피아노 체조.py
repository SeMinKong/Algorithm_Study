
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())
        diff = list(map(int, input().split()))
        Q = int(input().strip())
        mistake = [0] * N
        for i in range(N):
            if i == N - 1:
                mistake[i] = 0
            elif diff[i] > diff[i + 1]:
                mistake[i] = 1
            else:
                mistake[i] = 0

        ps = [0] * (N + 1)
        for i in range(1, N + 1):
            ps[0] = 0
            ps[i] = mistake[i - 1] + ps[i - 1]

        for _ in range(Q):
            x, y = list(map(int, input().split()))

            if mistake[y - 1] == 1:
                ans = ps[y] - ps[x - 1] - 1
            else:
                ans = ps[y] - ps[x - 1]

            print(ans)

if __name__ == "__main__":
    Solve().solve()