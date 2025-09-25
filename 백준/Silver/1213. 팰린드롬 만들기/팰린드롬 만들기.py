from collections import Counter

class Solve:
    def __init__(self):
        pass   

    def palindrome(self, input):
        count = Counter(input)
        odd = sum(v % 2 for v in count.values())
        if len(input) % 2 == 0:
            return odd == 0 
        else:
            return odd == 1

    def build_palindrome(self, input):
        count = Counter(input)
        odd_ch = [ch for ch, v in count.items() if v % 2 == 1]
        mid = ''.join(odd_ch)
        front = ''.join(ch * (count[ch] // 2 ) for ch in sorted(count))
        back = ''.join(reversed(front))
        if mid:
            return print(str(front) + str(mid) + str(back))
        else:
            return print(str(front) + str(back))

    def solve(self):
        import sys

        input = sys.stdin.readline().strip()
        possible = self.palindrome(input)

        if possible:
            self.build_palindrome(input)
        else:
            print("I'm Sorry Hansoo")

if __name__ == "__main__":
    Solve().solve()