#include <iostream>

using namespace std;

int baguni[100];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, i, j;

    cin >> N >> M;

    for (int x = 0; x < N; ++x) {
        baguni[x] = x + 1;
    }

    for (int x = 0; x < M; ++x) {
        cin >> i >> j;
        for (int y = 0; y <= (j - i) / 2; ++y) {
            int temp = baguni[i + y - 1];
            baguni[i + y - 1] = baguni[j - y - 1];
            baguni[j - y - 1] = temp;
        }

    }

    for (int i = 0; i < N; ++i) {
        cout << baguni[i] << ' ';
    }

    return 0;
}