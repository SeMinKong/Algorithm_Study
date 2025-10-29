from collections import deque
class Solve:
    def __init__(self):
        pass
        
    def solve(self):
        import sys
        input = sys.stdin.readline

        def bfs(i):
            q = deque()
            visited.add(i)
            q.append(i)
            order = {}
            seq = []
            while q:
                i = q.popleft()
                if i not in order:
                    order[i] = len(seq)
                    seq.append(i)

                if nums[i-1] not in visited:
                    visited.add(nums[i-1])
                    q.append(nums[i-1])
                else:
                    if nums[i-1] in order:
                        cycleNodes = seq[order[nums[i-1]]:]
                        inCycle.update(cycleNodes)

        N = int(input().strip())
        nums = []
        visited = set()
        inCycle = set()

        for _ in range(N):
            nums.append(int(input().strip()))
        
        for i in range(1, N+1):
            if i not in visited:
                bfs(i)
        
        ans = sorted(inCycle)
        print(len(ans))
        print(*ans, sep="\n")

if __name__ == "__main__":
    Solve().solve()