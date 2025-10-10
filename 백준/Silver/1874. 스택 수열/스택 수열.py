
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        n = int(input().strip())
        key = []
        stack = []
        occ = 0
        count = 0
        ans = []
        for _ in range(n):
            key.append(int(input()))

        for i in range(n + 1):
            while(len(stack) != 0 and stack[len(stack) - 1] == key[occ]): 
                stack.pop()
                occ += 1
                ans.append('-')
            if count != n:
                stack.append(i + 1)
                ans.append('+')
                count += 1

        if len(stack) == 0:
            print('\n'.join(map(str, ans)))
        else:
            print("NO")

if __name__ == "__main__":
    Solve().solve()