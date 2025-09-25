#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
	int N, X;
	string command;
	stack<int> s;
	vector<int> ans;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> command;
		if (command == "push") {
			cin >> X;
			s.push(X);
		}
		else if (command == "pop") {
			if (s.empty() == 0) {
				ans.push_back(s.top());
				s.pop();
			}
			else
				ans.push_back(-1);
		}
		else if (command == "size") {
			ans.push_back(s.size());
		}
		else if (command == "empty") {
			if (s.empty() == 0) {
				ans.push_back(0);
			}
			else
				ans.push_back(1);
		}
		else if (command == "top") {
			if (s.empty() == 0) {
				ans.push_back(s.top());
			}
			else
				ans.push_back(-1);
		}
	}
	for (auto& i : ans) {
		cout << i << endl;;
	}
	return 0;
}