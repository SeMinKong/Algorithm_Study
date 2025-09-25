#include <iostream>
#include <string>
#include <stack>

using namespace std;


int main() {
	int N;
	string sentence;
	stack<char> s;
	cin >> N;
	cin.ignore();

	while (N--) {
		getline(cin, sentence);
		sentence += ' ';

		for (int i = 0; i < sentence.size(); ++i) {
			if (sentence[i] == ' ') {
				while (!s.empty()) {
					cout << s.top();
					s.pop();
				}
				cout << ' ';
			}
			else
				s.push(sentence[i]);
		}
		cout << endl;
	}
	
	return 0;
}