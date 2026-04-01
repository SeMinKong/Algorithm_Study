#include <iostream>
#include <algorithm>

using namespace std;

int N, K, W, V;
int dp[101][100001];
int weight[100001];
int value[1001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> K;

	for (int i = 1; i <= N; i++) {
		cin >> W >> V;

		weight[i] = W;
		value[i] = V;
	}

	for (int i = 1; i <= N; i++) {
		for (int w = 1; w <= K; w++) {
			if (w >= weight[i]) {
				dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i]] + value[i]);
			}
			else dp[i][w] = dp[i - 1][w];
		}
	}

	cout << dp[N][K];

	return 0;
}