#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, sum = 0;
    string S;

    cin >> N;
    cin >> S;

    for (int i = 0; i < N; ++i) {
        sum += S[i] - '0';
    }
    cout << sum;

    return 0;
}