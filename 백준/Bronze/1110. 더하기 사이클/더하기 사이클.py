from collections import defaultdict, deque
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())

        start = N
        cnt = 0
        cur = N

        while True:
            a = cur // 10
            b = cur % 10
            c = (a + b) % 10
            cur = b * 10 + c
            cnt += 1
            if cur == start:
                break

        print(cnt)



if __name__ == "__main__":
    Solve().solve()