#include <iostream>
#include <string>
#include <stack>

using namespace std;

void print(stack <char>& sta) {
	while (!sta.empty()) {
		cout << sta.top();
		sta.pop();
	}
}

int main() {
	string str;
	stack<char> s;
	getline(cin, str);
	str += ' ';
	bool tag = false;
	for (int i = 0; i < str.length(); ++i) {
		if (str[i] == '<') {
			print(s);
			tag = true;
			cout << str[i];
		}
		else if(str[i] == '>'){
			tag = false;
			cout << str[i];
		}
		else if (tag) {
			cout << str[i];
		}
		else {
			if (str[i] == ' ') {
				print(s);
				cout << str[i];
			}
			else {
				s.push(str[i]);
			}
		}
	}
	return 0;
}