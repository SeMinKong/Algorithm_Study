class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, M = map(int, input().split())
        Lname = [input().strip() for _ in range(N)]
        Sname = [input().strip() for _ in range(M)]

        setL = set(Lname)
        setS = set(Sname)

        LSname = sorted(setL & setS)
        result = []
        for name in LSname:
            result.append(name)
        print(len(result))
        for name in result:
            print(name)


if __name__ == "__main__":
    Solve().solve()