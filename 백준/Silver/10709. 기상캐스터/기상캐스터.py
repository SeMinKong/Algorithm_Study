class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        H, W = map(int, (sys.stdin.readline().split()))
        cloud = [list(map(str, sys.stdin.readline().strip())) for _ in range(H)]
        ans = [[-1] * W for _ in range(H)]
        for i in range(H):
            dist = -1
            for j in range(W):
                if cloud[i][j] == 'c':
                    dist = 0
                    ans[i][j] = 0
                elif dist != -1:
                    dist += 1
                    ans[i][j] = dist
                    
        for row in ans:
            print(' '.join(map(str, row)))

        

if __name__ == "__main__":
    Solve().solve()
