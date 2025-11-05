from collections import defaultdict, deque
class Solve:
    def __init__(self):
        pass
        
    def solve(self):
        import sys
        input = sys.stdin.readline

        def bfs(a, b):
            if a == b:
                return 0
            q = deque([(a, 0)])
            visited = set()
            visited.add(a)
            while q:
                start, distance = q.popleft()
                for v in family[start]:
                    if v in visited:
                        continue
                    if v == b:
                        return distance + 1
                    visited.add(v)
                    q.append((v, distance + 1))
            return -1


        total = int(input().strip())
        a, b = list(map(int, input().split()))
        m = int(input().strip())
        family = defaultdict(list)
        for _ in range(m):
            x, y = list(map(int, input().split()))
            family[x].append(y)
            family[y].append(x)

        print(bfs(a, b))
        

        
        

if __name__ == "__main__":
    Solve().solve()