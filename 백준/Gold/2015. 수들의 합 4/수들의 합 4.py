from collections import defaultdict
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, K = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        cnt = defaultdict(int)
        ps = 0
        cnt[0] = 1
        ans = 0

        for x in arr:
            ps += x
            ans += cnt[ps - K]
            cnt[ps] += 1
                
        print(ans)

if __name__ == "__main__":
    Solve().solve()