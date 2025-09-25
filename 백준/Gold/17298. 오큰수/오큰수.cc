#include <iostream>
#include <stack>

using namespace std;

int a[1000000], NGE[1000000];

int main() {
    int N;
    cin >> N;

    stack<int> s;

    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }

    for (int i = N - 1; i >= 0; --i) {

        while (!s.empty() && a[s.top()] <= a[i]) {
            s.pop();
        }

        NGE[i] = s.empty() ? -1 : a[s.top()];

        s.push(i);
    }

    for (int i = 0; i < N; ++i) {
        cout << NGE[i] << ' ';
    }

    return 0;
}
