class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys

        word = sys.stdin.readline().strip()
        bomb_word = sys.stdin.readline().strip()
        final_word = []
        len2check = len(bomb_word)
        bomb_list = list(bomb_word)
        last_char = bomb_word[-1]

    #문자열 순회중(문자를 final_word에 append하면서) bomb_word 발견시 bomb_word 삭제. 이후 뒤에 문자열 모두 추가.
        for ch in word:
            final_word.append(ch)
            if ch == last_char and len(final_word) >= len2check:
                ok = True
                base = len(final_word) - len2check
                for i in range(len2check):
                    if final_word[base + i] != bomb_word[i]:
                        ok = False
                if ok:
                    del final_word[-len2check:] 

        if final_word:
            print(''.join(final_word))
        else:
            print("FRULA")

if __name__ == "__main__":
    Solve().solve()
