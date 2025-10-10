import heapq
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())
        x = []
        for _ in range(N):
            num = int(input().strip())
            if len(x) == 0 and num == 0:
                print(0)
            elif num == 0:
                print(abs(heapq.heappop(x)))
            else:
                heapq.heappush(x, -num)

if __name__ == "__main__":
    Solve().solve()