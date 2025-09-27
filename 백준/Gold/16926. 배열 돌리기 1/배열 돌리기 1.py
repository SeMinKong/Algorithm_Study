from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def rotate(self, X, R):
        N, M = len(X), len(X[0])
        rotated_X = [row[:] for row in X]
        layers = min(N, M) // 2

        for d in range(layers):
            top, left = d, d
            bottom, right = N - 1 - d, M - 1 - d

            pos = []
            # 상단 (left -> right)
            for j in range(left, right + 1):
                pos.append((top, j))
            # 오른쪽 (top+1 -> bottom-1)
            for i in range(top + 1, bottom):
                pos.append((i, right))
            # 하단 (right -> left)
            if bottom > top:
                for j in range(right, left - 1, -1):
                    pos.append((bottom, j))
            # 왼쪽 (bottom-1 -> top+1)
            if right > left:
                for i in range(bottom - 1, top, -1):
                    pos.append((i, left))

            ring = [X[i][j] for i, j in pos]
            L = len(ring)
            k = R % L #한바퀴

            for idx, (i, j) in enumerate(pos):
                rotated_X[i][j] = ring[(idx + k) % L]

        return rotated_X

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, M, R = map(int, input().split())
        X = []
        for _ in range(N):
            row = list(map(int, input().split()))
            X.append(row)

        X = self.rotate(X, R)

        for row in X:
            print(*row)
        
if __name__ == "__main__":
    Solve().solve()
