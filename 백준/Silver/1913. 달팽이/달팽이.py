from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys

        N = int(sys.stdin.readline()) 
        num = int(sys.stdin.readline()) 
        snail = [[0] * N for _ in range(N)]

        cen_x = N // 2
        cen_y = N // 2
        snail[cen_x][cen_y] = 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        i = 2 #snail 번호
        square = 3
        cnt_up = cnt_down = cnt_l = cnt_r = 0
        while cen_x != 0 or cen_y != 0:
            while i <= square * square:
                if cen_x == cen_y == N // 2:
                    cnt_up, cnt_down, cnt_l, cnt_r = square, square - 1, square - 1, square - 2
                    cen_x += dx[0]
                    cen_y += dy[0]
                    cnt_up -= 1

                elif cnt_r > 0:
                    cen_x += dx[3]
                    cen_y += dy[3]
                    cnt_r -= 1
                elif cnt_down > 0:
                    cen_x += dx[1]
                    cen_y += dy[1]
                    cnt_down -= 1
                elif cnt_l > 0:
                    cen_x += dx[2]
                    cen_y += dy[2]
                    cnt_l -= 1
                elif cnt_up > 0:
                    cen_x += dx[0]
                    cen_y += dy[0]
                    cnt_up -= 1

                snail[cen_x][cen_y] = i
                i += 1

            N -= 2 #시작점 조절
            square += 2
        

        #출력
        num_x = num_y = 0
        for i in range(len(snail)):
            print(*snail[i])
            if num in snail[i]:
                num_x = i + 1
                num_y = snail[i].index(num) + 1

        print(num_x, num_y)
        
if __name__ == "__main__":
    Solve().solve()
