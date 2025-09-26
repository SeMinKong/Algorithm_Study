from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        
        T = int(sys.stdin.readline().strip())
        for _ in range(T):
            N = int(sys.stdin.readline().strip())
            t = list(map(int, sys.stdin.readline().split()))
        
            cnt = Counter(t)
            score = defaultdict(list)
            t = [x for x in t if cnt[x] == 6]

            for i, x in enumerate(t, start=1):
                score[x].append(i)

            top4 = {x: sum(pos[:4]) for x, pos in score.items()}

            if top4:
                m4 = min(top4.values())
                tied = [k for k, v in top4.items() if v == m4]
                #동점 x
                if len(tied) == 1:
                    print(tied[0])
                else:
                    top5 = {x: sum(score[x][:5]) for x in tied}
                    m5 = min(top5.values())
                    winners = [k for k, v in top5.items() if v == m5]
                    print(winners[0])
if __name__ == "__main__":
    Solve().solve()
