from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys

        H, W= map(int, sys.stdin.readline().split())
        block_H = list(map(int, sys.stdin.readline().split()))
        
        l_max = [0] * W
        r_max = [0] * W

        mx = 0
        for i in range(W):
            mx = max(mx, block_H[i])
            l_max[i] = mx
        
        mx = 0
        for i in range(W - 1, -1, -1):
            mx = max(mx, block_H[i])
            r_max[i] = mx
        
        ans = 0
        for i in range(W):
            water = min(l_max[i], r_max[i]) -  block_H[i]
            if water > 0:
                ans += water

        print(ans)

        
if __name__ == "__main__":
    Solve().solve()
