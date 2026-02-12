#include <iostream>
#include <algorithm>
#include <queue>

const int mxN = 21e8;

int dr[4] = { -1, 1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

using namespace std;

struct Point {
	int r, c;
};

struct Pipe {
	int id;
	bool up, down, left, right;

	Pipe(int id) : id(id), up(false), down(false), left(false), right(false){
		switch (id)
		{
		case 1:
			up = true;
			down = true;
			left = true;
			right = true;
			break;
		case 2:
			up = true;
			down = true;
			break;
		case 3:
			left = true;
			right = true;
			break;
		case 4:
			up = true;
			right = true;
			break;
		case 5:
			down = true;
			right = true;
			break;
		case 6:
			down = true;
			left = true;
			break;
		case 7:
			up = true;
			left = true;
			break;
		default:
			break;
		}
	}
};
	
Pipe pipes[8] = {0, Pipe(1), Pipe(2), Pipe(3) , Pipe(4) , Pipe(5) , Pipe(6) , Pipe(7) };

int map[51][51], visited[51][51];
int N, M, R, C, L, ans;

void bfs(Point p) {
	queue<Point> q;
	q.push(p);
	visited[p.r][p.c] = 1;

	while (!q.empty()) {
		Point cp = q.front();
		q.pop();
		int curPipe = map[cp.r][cp.c];

		for (int i = 0; i < 4; i++) {
			Point np = { cp.r + dr[i], cp.c + dc[i] };
			int nextPipe = map[np.r][np.c];

			if (visited[np.r][np.c] != 0 || map[np.r][np.c] == 0 || np.r >= N || np.c >= M || np.r < 0 || np.c < 0) continue;
			if (i == 0 && pipes[curPipe].up && pipes[nextPipe].down ||
				i == 1 && pipes[curPipe].down && pipes[nextPipe].up ||
				i == 2 && pipes[curPipe].left && pipes[nextPipe].right ||
				i == 3 && pipes[curPipe].right && pipes[nextPipe].left) {
				visited[np.r][np.c] = visited[cp.r][cp.c] + 1;
				q.push(np);
			}
		}
	}
}

int solve() {

	ans = 0;

	cin >> N >> M >> R >> C >> L;

	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			cin >> map[r][c];
			visited[r][c] = 0;
		}
	}

	Point start = { R, C };

	bfs(start);

	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			if(visited[r][c] >0 && visited[r][c] <= L)ans++;
		}
	}

	return ans;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		cout << '#' << tc << " " << solve() << endl;
	}
	return 0;
}