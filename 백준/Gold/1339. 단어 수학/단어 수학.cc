#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
	int N, result = 0;
	string words;
	int T[26] = {};
	cin >> N;

	while (N--) {
		cin >> words;
		for (int i = 0; i < words.length(); ++i) {
			T[words[words.length() - i - 1] - 'A'] += pow(10,i);
		}
	}
	sort(T, T + 26);
	reverse(T, T + 26);

	
	for (int i = 0; i < 10; ++i) {
		result += T[i] * (9 - i);
	}

	cout << result;

	return 0;
}