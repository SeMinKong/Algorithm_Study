#include <iostream>

using namespace std;

int arr[1000000];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, min = 0, max = 0;

    cin >> N;


    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
        if (i == 0) {
            max = arr[i];
            min = arr[i];
            continue;
        }
        if (arr[i] > max)
            max = arr[i];
        else if (arr[i] < min)
            min = arr[i];
    }

    cout << min << " " << max;
    return 0;
}