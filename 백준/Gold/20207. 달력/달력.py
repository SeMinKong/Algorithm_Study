class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input())
        calendar = [0] * 365

        for _ in range(N):
            S, E = map(int, input().split())
            
            for i in range(S - 1, E):
                calendar[i] += 1

        #calender에서 0이 아닌 연속값들을(cnt)찾아서 면적 계산 (cnt* max(calendar값))
        cnt = 0
        schedule = 0
        ans = 0
        for i in range(365):
            if calendar[i] != 0:
                cnt += 1
                schedule = max(schedule, calendar[i])
                    
            else:
                if cnt > 0:
                    ans += cnt * schedule
                schedule = 0
                cnt = 0

        if cnt > 0:
            ans += cnt * schedule

        print(ans)

        
if __name__ == "__main__":
    Solve().solve()
