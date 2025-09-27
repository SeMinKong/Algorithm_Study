from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def rotate_45(self, X):
        n = len(X)

        rotated = [row[:] for row in X]

        middle_col = n // 2
        for i in range(n):
            rotated[i][middle_col] = X[i][i]

        for i in range(n):
            rotated[i][n - 1 - i] = X[i][middle_col]

        middle_row = n // 2
        for i in range(n):
            rotated[middle_row][n - 1 - i] = X[i][n - 1 - i]

        for i in range(n):
            rotated[i][i] = X[middle_row][i]
        
        return rotated


    def solve(self):
        import sys
        input = sys.stdin.readline

        T = int(input())
        for _ in range(T):
            n, d = map(int, input().split())
            X = []
            for _ in range(n):
                row = list(map(int, input().split()))
                X.append(row)
            
            rotate = d // 45
            if rotate == 1 or rotate == -7:
                X = self.rotate_45(X)
            elif rotate == 2 or rotate == -6:
                cnt = 2
                while(cnt != 0):
                    X = self.rotate_45(X)
                    cnt -=1
            elif rotate == 3 or rotate == -5:
                cnt = 3
                while(cnt != 0):
                    X = self.rotate_45(X)
                    cnt -=1
            elif rotate == 4 or rotate == -4:
                cnt = 4
                while(cnt != 0):
                    X = self.rotate_45(X)
                    cnt -=1
            elif rotate == 5 or rotate == -3:
                cnt = 5
                while(cnt != 0):
                    X = self.rotate_45(X)
                    cnt -=1
            elif rotate == 6 or rotate == -2:
                cnt = 6
                while(cnt != 0):
                    X = self.rotate_45(X)
                    cnt -=1
            elif rotate == 7 or rotate == -1:
                cnt = 7
                while(cnt != 0):
                    X = self.rotate_45(X)
                    cnt -=1
            elif rotate == 8 or rotate == 0:
                pass
            
            for row in X:
                print(*row)
        
if __name__ == "__main__":
    Solve().solve()
