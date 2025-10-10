from collections import defaultdict
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        total = 0
        trees = defaultdict(int)
        for line in sys.stdin:
            tree = line.strip()
            if tree == '':
                break
            trees[tree] += 1
            total += 1

        for tree in sorted(trees.keys()):
            print(f"{tree} {(trees[tree] / total) * 100:.4f}")
        
if __name__ == "__main__":
    Solve().solve()