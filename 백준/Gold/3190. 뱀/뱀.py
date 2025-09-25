N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]

L = int(input()) 
changes = [input().split() for _ in range(L)]
for i in range(L):
    changes[i][0] = int(changes[i][0])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, C):
    if C == "L":
        direction = (direction - 1) % 4
    else:  # "D"
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 
    board = [[0] * (N + 1) for _ in range(N + 1)]
    board[x][y] = 2
    for ax, ay in apples:
        board[ax][ay] = 1

    direction = 0
    time = 0
    idx_change = 0
    snake = [(x, y)]
    
    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                tail_x, tail_y = snake.pop(0)
                board[tail_x][tail_y] = 0
            board[nx][ny] = 2
            snake.append((nx, ny))
            x, y = nx, ny
        else:
            time += 1
            break

        time += 1
        if idx_change < L and time == changes[idx_change][0]:
            direction = turn(direction, changes[idx_change][1])
            idx_change += 1
            
    return time

print(simulate())