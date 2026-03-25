#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;
	cin >> s;

	set<char> vowel, yvowel;
	vowel = { 'a','e', 'i', 'o', 'u' };
	yvowel = { 'a','e', 'i', 'o', 'u', 'y'};

	int cnt = 0;
	int ycnt = 0;

	for (int i = 0; i < s.length(); i++) {
		if (vowel.find(s[i]) != vowel.end()) cnt++;
		if (yvowel.find(s[i]) != yvowel.end()) ycnt++;
	}

	cout << cnt << ' ' << ycnt;

	return 0;
}