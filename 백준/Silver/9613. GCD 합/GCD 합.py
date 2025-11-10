from collections import defaultdict, deque
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys, math
        input = sys.stdin.readline

        t = int(input().strip())

        for _ in range(t):
            data = list(map(int, input().split()))
            n, arr = data[0], data[1:]
            total = 0
            for i in range(n):
                ai = arr[i]
                for j in range(i + 1, n):
                    total += math.gcd(ai, arr[j])
            print(total)

if __name__ == "__main__":
    Solve().solve()