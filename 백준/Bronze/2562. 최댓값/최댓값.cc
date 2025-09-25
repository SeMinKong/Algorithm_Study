#include <iostream>

using namespace std;

int arr[1000000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int max = 0, idx = 1;


    for (int i = 0; i < 9; ++i) {
        cin >> arr[i];
        if (i == 0) {
            max = arr[i];
            continue;
        }
        if (arr[i] > max) {
            max = arr[i];
            idx = i + 1;
        }
    }

    cout << max << "\n" << idx;
    return 0;
}