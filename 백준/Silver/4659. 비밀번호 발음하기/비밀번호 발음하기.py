class Solve:
    def __init__(self):
        pass

    def condition(self, password) -> bool:
        vowels = set("aeiou")

        #모음 포함 여부
        if not any(ch in vowels for ch in password):
            return False

        #모음3개 자음 3개 연속오면 안됨
        vcount = 0
        ccount = 0
        for ch in password:
            if ch in vowels:
                vcount += 1
                ccount = 0
            else:
                ccount += 1
                vcount = 0
            if vcount >= 3 or ccount >= 3:
                return False

        #같은 글자 연속
        for i in range(1, len(password)):
            if password[i] == password[i - 1]:
                #ee, oo 체크
                pair = password[i - 1 : i + 1]
                if pair not in ("ee", "oo"):
                    return False

        return True

    def solve(self):
        import sys

        for line in sys.stdin:
            s = line.strip()
            if s == "end":
                break
            result = "acceptable" if self.condition(s) else "not acceptable"
            print(f"<{s}> is {result}.")


if __name__ == "__main__":
    Solve().solve()