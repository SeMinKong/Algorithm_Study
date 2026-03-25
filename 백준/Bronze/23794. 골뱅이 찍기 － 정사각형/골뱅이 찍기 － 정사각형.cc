#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	for (int i = 0; i < N + 2; i++) {
		if (i == 0 || i == N + 1) {
			for (int j = 0; j < N + 2; j++) {
				cout << '@';
			}
			cout << '\n';
		}
		else {
			for (int j = 0; j < N + 2; j++) {
				if (j == 0 || j == N + 1) cout << '@';
				else cout << ' ';
			}
			cout << '\n';
		}
	}

	return 0;
}