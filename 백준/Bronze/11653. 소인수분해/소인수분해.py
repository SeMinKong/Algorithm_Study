from collections import defaultdict, deque
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input())

        i = 2
        while i * i <= N:
            while N % i == 0:
                print(i)
                N //= i
            i += 1

        if N > 1:
            print(N)


if __name__ == "__main__":
    Solve().solve()