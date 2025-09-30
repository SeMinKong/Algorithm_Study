
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline
        
        N = int(input())
        cnt = N
        if N == 0:
            print(1)
        else:
            while(cnt > 1):
                cnt -= 1
                N *= cnt
            print(N)

        


if __name__ == "__main__":
    Solve().solve()