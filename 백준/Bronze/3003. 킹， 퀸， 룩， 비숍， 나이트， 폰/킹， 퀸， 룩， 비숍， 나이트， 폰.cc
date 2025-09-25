#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    int chess[6] = { 1, 1, 2, 2, 2, 8 };
    int current[6];

    for (int i = 0; i < 6; ++i) {
        cin >> current[i];
        chess[i] -= current[i];
    }

    for (int i = 0; i < 6; ++i) {
        cout << chess[i] << ' ';
    }
    return 0;
}
