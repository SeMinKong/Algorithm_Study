from collections import defaultdict, deque
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        n = int(input())
        for _ in range(n):
            a, b = map(int, input().split())
            print(a * b // gcd(a, b))




if __name__ == "__main__":
    Solve().solve()