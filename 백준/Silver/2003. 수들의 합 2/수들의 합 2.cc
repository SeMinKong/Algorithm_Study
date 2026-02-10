#include <iostream>

using namespace std;

#define ll long long

int N;
ll M;
int A[10001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	int lp, rp;
	lp = 0;
	rp = 0;
	int cnt = 0;
	int curSum = A[0];

	while (rp < N - 1) {
		if (curSum < M) {
			rp++;
			curSum += A[rp];
		}
		else if (curSum > M) {
			curSum -= A[lp];
			lp++;
		}
		else if (curSum == M)
		{
			cnt++;
			rp++;
			curSum += A[rp];
		}
	}

	while (curSum >= M) {
		if (curSum == M) {
			cnt++;
		}
		curSum -= A[lp];
		lp++;
	}

	cout << cnt;
	return 0;

}
