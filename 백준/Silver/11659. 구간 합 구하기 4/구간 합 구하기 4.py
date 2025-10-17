
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, M = list(map(int, input().split()))
        num = list(map(int, input().split()))

        prefix_sum = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix_sum[0] = 0
            prefix_sum[i] = prefix_sum[i - 1] + num[i - 1]
        
        for _ in range(M):
            i, j = list(map(int, input().split()))
            ans = 0
            ans += prefix_sum[j] - prefix_sum[i - 1]
            print(ans)
        

if __name__ == "__main__":
    Solve().solve()