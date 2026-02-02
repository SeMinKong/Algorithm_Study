#include <iostream>

using namespace std;

int input, wall_up[500001], wall_down[500001];
int psum_up[500001], psum_down[500001];
int ans[500001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, H;
	cin >> N >> H;

	int min_val = 200000;
	int cnt = 0;

	for (int i = 0; i < N; i++)
	{
		cin >> input;
		if (i % 2 == 0) {
			wall_up[input]++;
		}
		else {
			wall_down[input]++;
		}
	}


	for (int i = H - 1; i > 0; i--) {

		psum_up[H] = wall_up[H];
		psum_up[i] += psum_up[i + 1] + wall_up[i];

		psum_down[H] = wall_down[H];
		psum_down[i] += psum_down[i + 1] + wall_down[i];

	}

	for (int i = 0; i < H; i++) {
		ans[i] = psum_down[i + 1] + psum_up[H - i];
		if (ans[i] < min_val) min_val = ans[i];
	}

	for (int i = 0; i < H; i++) {
		if (ans[i] == min_val) {
			cnt++;
		}
	}

	cout << min_val << " " << cnt;

	return 0;
}