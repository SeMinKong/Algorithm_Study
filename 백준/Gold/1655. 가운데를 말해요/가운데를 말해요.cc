#include <iostream>

using namespace std;

const int mxN = 20000;
int tree[mxN * 4 + 4];

int N;

void update(int node, int start, int end, int val) {
	if (val < start || val > end) return;

	tree[node] += 1;

	if (start == end) return;

	int mid = (start + end) / 2;
	update(node * 2, start, mid, val);
	update(node * 2 + 1, mid + 1, end, val);
}

int query(int node, int start, int end, int k) {
	if (start == end) return start;

	int mid = (start + end) / 2;

	if (tree[node * 2] >= k) {
		return query(node * 2, start, mid, k);
	}
	else {
		return query(node * 2 + 1, mid + 1, end, k - tree[node * 2]);
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N;


	for (int i = 1; i <= N; i++) {
		int num;
		cin >> num;

		update(1, 0, mxN, num + 10000);

		int k = (i + 1) / 2;
		int ans = query(1, 0, mxN, k);

		cout << ans - 10000 << '\n';
	}

	return 0;
}