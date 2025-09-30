from datetime import datetime


class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline
        
        print(f"{datetime.today().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    Solve().solve()