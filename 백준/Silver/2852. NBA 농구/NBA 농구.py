from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def to_sec(self, scoretime):
        m, s = map(int, scoretime.split(':'))
        return m * 60 + s

    def to_MMSS(self, sectime):
        m, s = divmod(sectime, 60)
        return f"{m:02d}:{s:02d}"

    def solve(self):
        import sys
        
        N = int(sys.stdin.readline())
        score = {1: 0, 2: 0}
        lead = {1: 0, 2: 0}  # 각 팀이 리드한 누적 초
        last_time = 0         # 직전 이벤트 시각(초)

        for _ in range(N):
            team_str, time_str = sys.stdin.readline().split()
            cur_time = self.to_sec(time_str)

            # 현재 이벤트 직전까지 리드하던 팀에 시간 누적
            if score[1] > score[2]:
                lead[1] += cur_time - last_time
            elif score[2] > score[1]:
                lead[2] += cur_time - last_time

            team = int(team_str)
            score[team] += 1
            last_time = cur_time

        end_time = self.to_sec('48:00')
        if score[1] > score[2]:
            lead[1] += end_time - last_time
        elif score[2] > score[1]:
            lead[2] += end_time - last_time

        print(self.to_MMSS(lead[1]))
        print(self.to_MMSS(lead[2]))
            
            
        
if __name__ == "__main__":
    Solve().solve()
