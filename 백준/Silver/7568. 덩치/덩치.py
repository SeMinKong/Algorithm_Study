import re


class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        N = int(sys.stdin.readline().strip())
        pairs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
        rank = [1] * N

        for i in range(N):
            w_i, h_i = pairs[i]
            for j in range(N):
                if i == j:
                    continue
                w_j, h_j = pairs[j]
                if w_j > w_i and h_j > h_i:
                    rank[i] += 1

        print(' '.join(map(str, rank)))

if __name__ == "__main__":
    Solve().solve()
