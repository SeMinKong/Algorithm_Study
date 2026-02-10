#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int N, K;
string S;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N >> K >> S;

	int lp = 0;
	int rp = S.length() - 1;

	while (K) {

		if (lp >= rp) {
			break;
		}
		if (S[lp] == 'C' && S[rp] == 'P') {
			S[lp] = 'P';
			S[rp] = 'C';
			lp++;
			rp--;
			K--;
		}
		else if (S[lp] == 'C') {
			rp--;
		}
		else {
			lp++;
		}

	}

	long long cnt = 0;
	long long p_cnt = 0;

	for (int i = 0; i < S.length(); i++) {

		if (S[i] == 'P') {
			p_cnt++;
		}
		else if (S[i] == 'C') {
			cnt += (p_cnt * (p_cnt - 1)) / 2;
		}
	}

	cout << cnt;

	return 0;
}