#include <iostream>
#include <deque>

using namespace std;

int main() {
	int N;
	string command;
	deque<int> d;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> command;
		if (command == "push_front") {
			int X;
			cin >> X;
			d.push_front(X);
		}
		else if (command == "push_back") {
			int X;
			cin >> X;
			d.push_back(X);
		}
		else if (command == "pop_front") {
			if (!d.empty()) {
				cout << d.front() << endl;;
				d.pop_front();
			}
			else
				cout << -1 << endl;
		}
		else if (command == "pop_back") {
			if (!d.empty()) {
				cout << d.back() << endl;;
				d.pop_back();
			}
			else
				cout << -1 << endl;
		}
		else if (command == "size") {
			cout << d.size() << endl;
		}
		else if (command == "empty") {
			if (d.empty()) {
				cout << 1 << endl;
			}
			else
				cout << 0 << endl;
		}
		else if (command == "front") {
			if (!d.empty()) {
				cout << d.front() << endl;
			}
			else
				cout << -1 << endl;
		}
		else if (command == "back") {
			if (!d.empty()) {
				cout << d.back() << endl;
			}
			else
				cout << -1 << endl;
		}
	}
	return 0;
}