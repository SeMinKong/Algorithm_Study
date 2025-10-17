
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        n = int(input())
        x = list(map(int, input().split()))
        ans = 0
        total = sum(x)

        for v in x:
            total -= v
            ans += v * total
        print(ans)



if __name__ == "__main__":
    Solve().solve()