from collections import deque
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input())
        num = deque(range(1, N + 1))

        while(len(num) != 1):
            num.popleft()
            num.append(num.popleft())

        print(num[0])

if __name__ == "__main__":
    Solve().solve()