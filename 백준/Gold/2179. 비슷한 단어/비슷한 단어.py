class Solve:
    def __init__(self):
        pass

    def lcp_len(self, a: str, b: str) -> int:
        cnt = 0
        for x, y in zip(a, b):
            if x == y:
                cnt += 1
            else:
                break
        return cnt

    def solve(self):
        import sys
        input = sys.stdin.readline

        N = int(input().strip())
        words = [input().strip() for _ in range(N)]

        # (단어, 원래 입력 인덱스)
        arr = [(w, i) for i, w in enumerate(words)]
        arr.sort(key=lambda x: x[0])  # 사전순 정렬

        # 인접 LCP 배열과 최대값 M
        lcp = [0] * (N - 1)
        M = 0
        for i in range(N - 1):
            l = self.lcp_len(arr[i][0], arr[i + 1][0])
            lcp[i] = l
            if l > M:
                M = l

        # LCP >= M 이어지는 구간(블록)들을 훑어, 각 블록에서
        # 입력 인덱스가 가장 작은 두 단어(단 서로 다른 문자열)를 뽑는다.
        INF = 10**9
        best_s, best_t = INF, INF

        i = 0
        while i < N:
            j = i
            # lcp[j]는 arr[j]와 arr[j+1]의 LCP이므로, lcp[j] >= M이면 같은 블록
            while j < N - 1 and lcp[j] >= M:
                j += 1
            # 블록 = arr[i..j] (양끝 포함)
            if j - i + 1 >= 2:
                # 블록 안에서 입력 인덱스 오름차순으로 정렬
                block = sorted(((arr[k][1], arr[k][0]) for k in range(i, j + 1)))
                # 서로 "다른 문자열"을 만족하는 가장 앞선 두 개를 선택
                first_idx, first_word = None, None
                s = t = None
                for orig_idx, w in block:
                    if first_idx is None:
                        first_idx, first_word = orig_idx, w
                    else:
                        if w != first_word:  # 같은 문자열은 제외
                            s, t = first_idx, orig_idx
                            break
                if s is not None:
                    #출력 조건 입력순순
                    if (s < best_s) or (s == best_s and t < best_t):
                        best_s, best_t = s, t
            i = j + 1

        print(words[best_s])
        print(words[best_t])


if __name__ == "__main__":
    Solve().solve()
