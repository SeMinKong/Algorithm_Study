#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, price, coin[4] = { 25, 10, 5, 1 };

    cin >> N;

    for (int i = 0; i < N; ++i) {
        cin >> price;
        int temp;
        for (int j = 0; j < 4; ++j) {
            temp = price / coin[j];
            cout << temp << ' ';
            price -= coin[j] * temp;
        }
        cout << '\n';
    }
    return 0;
}

