
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())
        events = {}

        for _ in range(N):
            a, b = map(int, input().split())
            events[a] = events.get(a, 0) + 1
            events[b] = events.get(b, 0) - 1

        pts = sorted(events.keys())

        cur = 0
        target = 0

        for i, x in enumerate(pts):
            cur += events[x]
            if i + 1 < len(pts):
                if cur > target:
                    target = cur

        cur = 0
        L = R = None
        for i, x in enumerate(pts):
            cur += events[x]
            if i + 1 >= len(pts):
                break
            nx = pts[i + 1]
            if cur == target and nx > x:
                if L is None:
                    L, R = x, nx
                elif R == x:
                    R = nx
                else:
                    break
           
        print(target)
        print(L, R)
    
if __name__ == "__main__":
    Solve().solve()