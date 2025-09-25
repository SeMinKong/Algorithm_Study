#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;

    while (1) {
        cin >> N >> M;
        if (N == 0 && M == 0)
            break;
        cout << N + M << '\n';
   }
    return 0;
}