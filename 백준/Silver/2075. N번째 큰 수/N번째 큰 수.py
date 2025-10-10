import heapq
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input())
        heap = []
        for _ in range(N):
            nums = list(map(int, input().split()))
            for num in nums:
                heapq.heappush(heap, num)
                if len(heap) > N:
                    heapq.heappop(heap)

        print(heap[0])        
if __name__ == "__main__":
    Solve().solve()