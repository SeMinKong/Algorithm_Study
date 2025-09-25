#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int N, A[1000000], F[1000000], NGF[1000000];

int main() {
	stack<int> s;

	cin >> N;

	for (int i = 0; i < N; ++i) {
		cin >> A[i];
		F[A[i] - 1]++;
	}

	for (int i = 0; i < N; ++i) {
		while (!s.empty() && (F[A[s.top()] - 1] < F[A[i] - 1])){
			NGF[s.top()] = A[i];
			s.pop();
		}
		s.push(i);
	}
	while (!s.empty()) {
		NGF[s.top()] = -1;
		s.pop();
	}

	for (int i = 0; i < N; ++i) {
		cout << NGF[i] << ' ';
	}
	return 0;
}