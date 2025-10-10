
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, M = map(int, input().split())
        words = set()
        ans = 0
        for _ in range(N):
            words.add(input().strip())

        for _ in range(M):
            check = input().strip()
            if check in words:
                ans += 1
        
        print(ans)


if __name__ == "__main__":
    Solve().solve()