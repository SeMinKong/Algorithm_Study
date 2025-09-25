#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string S;
    int N;

    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> S;
        cout << S.front() << S.back() <<'\n';
    }

    return 0;
}