class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline
        
        A = input().strip()
        B = input().strip()
        C = input().strip()

        print(int(A) + int(B) - int(C))
        print(int(A + B) - int(C))

if __name__ == "__main__":
    Solve().solve()