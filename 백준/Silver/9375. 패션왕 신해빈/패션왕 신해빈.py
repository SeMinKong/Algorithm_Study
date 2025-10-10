class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        case = int(input().strip())
        for _ in range(case):
            n = int(input().strip())
            clothes = {}
            ans = 1
            for _ in range(n):
                cloth = input().split()
                clothes.setdefault(cloth[1], []).append(cloth[0])

            for k, v in clothes.items(): 
                ans *= len(v) + 1
            
            print(ans - 1)
                

        
if __name__ == "__main__":
    Solve().solve()