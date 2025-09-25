#include <iostream>

using namespace std;

void multishow(int a, int b) {
	while (b > 0) {
		int temp = b;
		temp %= 10;
		cout << a * temp << endl;
		b /= 10;
	}
}

int main() {
	int a, b;
	cin >> a >> b;
	multishow(a, b);
	cout << a * b;
	return 0;
}
