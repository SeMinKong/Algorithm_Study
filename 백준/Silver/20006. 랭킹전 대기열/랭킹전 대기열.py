from collections import Counter, defaultdict

class Solve:
    def __init__(self):
        pass

    def solve(self):
        import sys
        
        p, m= map(int, sys.stdin.readline().split())
        rooms = []
        for _ in range(p):
            l, n = map(str, sys.stdin.readline().split())
            l = int(l)

            placed = False

            for room in rooms:
                if len(room['users']) < m and abs(l - room['base']) <= 10:
                    room['users'].append((l,n))
                    placed = True
                    break
            if not placed:
                rooms.append({'base': l, 'users': [(l, n)]})

        for room in rooms:
            print('Started!' if len(room['users']) == m else 'Waiting!')
            for l, n in sorted(room['users'], key=lambda x:x[1]):
                print(l, n)

        
if __name__ == "__main__":
    Solve().solve()
