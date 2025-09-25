#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    int check[30];

    for (int i = 0; i < 30; ++i) {
        check[i] = i + 1;
    }

    for (int i = 0; i < 28; ++i) {
        cin >> n;
        check[n - 1] -= n;
    }
    
    for (int i = 0; i < 30; ++i) {
        if (check[i] != 0)
            cout << check[i] << '\n';
    }
    return 0;
}