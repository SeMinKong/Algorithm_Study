#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    int N;

    cin >> N;

    for (int i = 0; i < 2 * N - 1; ++i) {
        if (i < N) {
            for (int j = N; j > i + 1; --j) {
                cout << ' ';
            }
            for (int j = 0; j < 2 * i + 1; ++j) {
                cout << '*';
            }
        }
        else {
            for (int j = 0; j <= i - N; ++j) {
                cout << ' ';
            }
            for (int j = 2 * N; j > 2 * i - (2 * N - 3)  ; --j) {
                cout << '*';
            }
        }
        cout << '\n';
    }
    return 0;
}
