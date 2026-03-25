#include <iostream>
#include <vector>


using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	vector<long long> dp(N + 1);

	dp[0] = 1;

	for (int i = 1; i <= N; i++) {
		dp[i] = dp[i - 1] * i;
	}

	cout << dp[N];


	return 0;
}