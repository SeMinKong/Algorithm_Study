
class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        input = sys.stdin.readline

        pensioner, numTvChannel, initialChannel = list(map(int, input().split()))

        hateToFav = {}
        currentChannel = initialChannel
        visited = set()
        count = 0

        for _ in range(pensioner):
            favoriteChannel, hatedChannel = list(map(int, input().split()))
            if hatedChannel not in hateToFav:
                hateToFav[hatedChannel] = favoriteChannel

        while True:
            if currentChannel not in hateToFav:
                print(count)
                return
            if currentChannel in visited:
                print(-1)
                return
            visited.add(currentChannel)

            currentChannel = hateToFav[currentChannel]
            count += 1
    

if __name__ == "__main__":
    Solve().solve()