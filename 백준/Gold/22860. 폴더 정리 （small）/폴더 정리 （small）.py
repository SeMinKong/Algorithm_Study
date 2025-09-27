class Solve:
    def __init__(self):
        pass

    def get_all_files(self, folder, items):
        files = set()
        total_count = 0
        queue = [folder]
        
        while queue:
            current_folder = queue.pop(0)
            if current_folder in items:
                for name, is_folder in items[current_folder]:
                    if is_folder:
                        queue.append(name)
                    else:
                        files.add(name)
                        total_count += 1
        
        return files, total_count

    def solve(self):
        import sys
        input = sys.stdin.readline
        N, M = map(int, input().split())
        items = {}
        for _ in range(N + M):
            P, F, C = input().strip().split()
            C = int(C)
            if P not in items:
                items[P] = []
            items[P].append((F, C))

        Q = int(input())
        for _ in range(Q):
            query = input().strip()
            target_folder = query.split('/')[-1]

            file_types, total_files = self.get_all_files(target_folder, items)
            print(f"{len(file_types)} {total_files}")

if __name__ == "__main__":
    Solve().solve()