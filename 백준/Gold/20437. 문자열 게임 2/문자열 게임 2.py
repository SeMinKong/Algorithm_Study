from collections import defaultdict

class Solve:
    def __init__(self):
        pass  

    def solve(self):
        import sys

        T = int(sys.stdin.readline().strip())
        for _ in range(T):
            W = sys.stdin.readline().strip()
            K = int(sys.stdin.readline().strip())
            
            #어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다
            #키 인덱스를 증가시켜가며 min length를 찾는다.(이때 K개의 문자를 포함하는지도 검사)
            dic = defaultdict(list)
            for i, ch in enumerate(W):
                dic[ch].append(i)


            ans_3 = 99999
            ans_4 = -1

            for ch, pos in dic.items():
                if len(pos) < K:
                    continue
                else:
                    for i in range(len(pos) - K + 1):
                        cur_len = pos[i + K - 1] - pos[i] + 1
                        ans_3 = min(cur_len, ans_3)
                        ans_4 = max(cur_len, ans_4)
                        
            #어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다
            if ans_3 == 99999 and ans_4 == -1:
                print(-1)
            else:
                print(f'{ans_3} {ans_4}')



if __name__ == "__main__":
    Solve().solve()