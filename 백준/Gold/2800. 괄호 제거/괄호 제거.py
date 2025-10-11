
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        equation = input().strip()
        stack = []
        pairs = []
        for i, ch in enumerate(equation):
            if ch =='(':
                stack.append(i)
            elif ch == ')':
                open_idx = stack.pop()
                pairs.append((open_idx, i))

        ans = set()
        m = len(pairs)

        for mask in range(1, 1 << m):
            to_remove = set()
            for j in range(m):
                if mask & (1 << j):
                    o, c = pairs[j]
                    to_remove.add(o)
                    to_remove.add(c)

            buf = []
            for i, ch in enumerate(equation):
                if i in to_remove:
                    continue
                buf.append(ch)
            ans.add("".join(buf))

        for line in sorted(ans):
            print(line)
if __name__ == "__main__":
    Solve().solve()