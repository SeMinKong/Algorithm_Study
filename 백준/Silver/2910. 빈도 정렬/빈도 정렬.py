from collections import defaultdict
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N, C = map(int, input().split())
        nums = defaultdict(int)

        num = list(map(int, input().split()))
        for i in range(len(num)):
            nums[num[i]] += 1 

        nums = sorted(nums.items(), key=lambda x:(-x[1], list(nums.keys()).index(x[0])))
        for k, v in nums:
            print((str(k)+ ' ') * v, end= '')


if __name__ == "__main__":
    Solve().solve()